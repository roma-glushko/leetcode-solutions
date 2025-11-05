import time

class NoTokensAvailableError(Exception):
    def __init__(self, retry_after_secs: float) -> None:
        self.retry_after_secs = retry_after_secs

        super().__init__(f"No tokens available, retry after {retry_after_secs:.2f} seconds")

class TokenBucket:
    def __init__(self, max_tokens: float, per_seconds: float, bucket_size: float | None = None) -> None:
        self._max_tokens = max_tokens
        self._per_seconds = per_seconds

        self._bucket_size = bucket_size if bucket_size is not None else max_tokens
        self._tokens = self._bucket_size

        self._refill_rate = max_tokens / per_seconds # mint this amount tokens per second
        self._last_refilled_at = time.monotonic()

    @property
    def tokens(self) -> float:
        self._refill()
        return self._tokens

    @property
    def empty(self) -> bool:
        return self._tokens > 10e-12

    def take(self, num: float = 1.0) -> None:
        self._refill()

        if self._tokens >= num:
            self._tokens -= num
            return

        raise NoTokensAvailableError(retry_after_secs=self.time_until(num))

    def _refill(self):
        now = time.monotonic()
        elapsed_since_last_refill = now - self._last_refilled_at

        if elapsed_since_last_refill <= 0:
            # still need to wait before next refill
            return

        self._tokens = min(self._bucket_size, self._tokens + elapsed_since_last_refill * self._refill_rate)
        self._last_refilled_at = now

    def time_until(self, num: float = 1.0) -> float:
        self._refill()

        need_tokens = num - self._tokens

        if need_tokens <= 0:
            return 0.0

        return need_tokens / self._refill_rate