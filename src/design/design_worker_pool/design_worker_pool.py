import asyncio
from dataclasses import dataclass
from typing import Callable, Any, Awaitable
import logging

logger = logging.getLogger(__name__)

JobFut = asyncio.Future[Any]
JobFn = Callable[..., Awaitable[Any]]

async def maybe_call(fn: Callable[..., Awaitable[None]] | None, *args: Any) -> None:
    if fn is None:
       return

    await fn(*args)

@dataclass
class _Job:
    fn: JobFn
    args: Any
    kwargs: Any
    fut: asyncio.Future[Any]

class AsyncWorkerPool:
    def __init__(
        self,
        workers: int = 5,
        queue_size: int = 100,
        *,
        name: str = "awpool",
        on_start: Callable[[int, Any, Any], Awaitable[None]] | None = None,
        on_stop: Callable[[int, Any, Exception | None], Awaitable[None]] | None = None,
    ) -> None:
        if workers < 1:
            raise ValueError("workers must be >= 1")

        if queue_size < 1:
            raise ValueError("queue_size must be >= 1")

        self.workers = workers
        self.queue_size = queue_size

        self.name = name

        self._started = False
        self._stopping = False

        self._queue: asyncio.Queue[_Job | None] = asyncio.Queue(maxsize=self.queue_size)
        self._worker_tasks: list[asyncio.Task[None]] = []

        self._on_start = on_start
        self._on_stop = on_stop

    async def start(self) -> None:
        if self._started:
            return

        self._started = True

        for wid in range(self.workers):
            worker_task = asyncio.create_task(self._worker_loop(wid), name=f"{self.name}-worker-{wid}")
            self._worker_tasks.append(worker_task)

    async def submit(self, fn: JobFn, *args: Any, timeout_secs: float | None = None, **kwargs: Any) -> JobFut:
        job_fut: JobFut = asyncio.get_running_loop().create_future()
        job = _Job(fn, args, kwargs, job_fut)

        try:
            add_job_fut = self._queue.put(job)

            if timeout_secs is None:
                await add_job_fut
            else:
                await asyncio.wait_for(add_job_fut, timeout=timeout_secs)
        except asyncio.TimeoutError as exc:
            raise TimeoutError("Failed to submit job within the specified timeout") from exc

        return job_fut

    async def stop(self, cancel_pending: bool = False) -> None:
        if self._stopping:
            return

        self._stopping = True

        if cancel_pending:
            while not self._queue.empty():
                job = self._queue.get_nowait()

                if job is not None and not job.fut.done():
                    job.fut.cancel()

                self._queue.task_done()

        await self._stop_workers()

        if self._worker_tasks:
            await asyncio.gather(*self._worker_tasks, return_exceptions=True)

    async def _worker_loop(self, wid: int) -> None:
        while True:
            job  = await self._queue.get()

            if job is None:
                # sentinel value to shut down the worker
                self._queue.task_done()
                break

            if job.fut.cancelled():
                continue

            job_result: Any | None = None
            job_exc: Exception | None = None

            try:
                await maybe_call(self._on_start, wid, job.args, job.kwargs)

                job_result = await job.fn(*job.args, **job.kwargs)

                if not job.fut.done():
                    job.fut.set_result(job_result)
            except Exception as e:
                job_exc = e
                if not job.fut.done():
                    job.fut.set_exception(job_exc)
            finally:
                await maybe_call(self._on_stop, wid, job_result, job_exc)
                self._queue.task_done()

    async def _stop_workers(self) -> None:
        for _ in range(self.workers):
            await self._queue.put(None)


if __name__ == "__main__":
    async def main() -> None:
        awpool = AsyncWorkerPool(workers=10, queue_size=50)

        await awpool.start()

        async def sample_job(x: int) -> int:
            await asyncio.sleep(1)
            res =  x * x

            # if res % 2 == 0:
                # Random error for demonstration
                # raise ValueError(f"Simulated error for input {x}")

            return res

        futures = [await awpool.submit(sample_job, i) for i in range(5)]
        results = await asyncio.gather(*futures)

        print("Job results:", results)

        await awpool.stop()

    asyncio.run(main())