from unittest import TestCase

from .token_bucket_rate_limiter import TokenBucketRateLimiter


class FakeClock:
    """Controllable clock for deterministic testing."""

    def __init__(self, start: float = 0.0) -> None:
        self.now = start

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


class TokenBucketRateLimiterTest(TestCase):
    def test_allows_requests_up_to_capacity(self):
        clock = FakeClock()
        limiter = TokenBucketRateLimiter(capacity=3, refill_rate=1, clock=clock)

        self.assertTrue(limiter.allow())
        self.assertTrue(limiter.allow())
        self.assertTrue(limiter.allow())
        self.assertFalse(limiter.allow())

    def test_refills_tokens_over_time(self):
        clock = FakeClock()
        limiter = TokenBucketRateLimiter(capacity=2, refill_rate=1, clock=clock)

        # Drain the bucket
        self.assertTrue(limiter.allow())
        self.assertTrue(limiter.allow())
        self.assertFalse(limiter.allow())

        # Wait 1 second -> 1 token refilled
        clock.advance(1.0)
        self.assertTrue(limiter.allow())
        self.assertFalse(limiter.allow())

    def test_does_not_exceed_capacity(self):
        clock = FakeClock()
        limiter = TokenBucketRateLimiter(capacity=3, refill_rate=10, clock=clock)

        # Wait a long time, tokens should cap at capacity
        clock.advance(100.0)

        self.assertTrue(limiter.allow())
        self.assertTrue(limiter.allow())
        self.assertTrue(limiter.allow())
        self.assertFalse(limiter.allow())

    def test_fractional_refill_rate(self):
        clock = FakeClock()
        # 1 token every 2 seconds
        limiter = TokenBucketRateLimiter(capacity=5, refill_rate=0.5, clock=clock)

        # Drain all 5 tokens
        for _ in range(5):
            self.assertTrue(limiter.allow())
        self.assertFalse(limiter.allow())

        # After 1 second, only 0.5 tokens -> not enough
        clock.advance(1.0)
        self.assertFalse(limiter.allow())

        # After another 1 second (total 2s), 1.0 token available
        clock.advance(1.0)
        self.assertTrue(limiter.allow())
        self.assertFalse(limiter.allow())

    def test_multi_token_request(self):
        clock = FakeClock()
        limiter = TokenBucketRateLimiter(capacity=10, refill_rate=1, clock=clock)

        self.assertTrue(limiter.allow(tokens=5))
        self.assertTrue(limiter.allow(tokens=5))
        self.assertFalse(limiter.allow(tokens=1))

    def test_multi_token_request_partial_refill(self):
        clock = FakeClock()
        limiter = TokenBucketRateLimiter(capacity=10, refill_rate=2, clock=clock)

        # Drain all tokens
        self.assertTrue(limiter.allow(tokens=10))
        self.assertFalse(limiter.allow(tokens=1))

        # 3 seconds -> 6 tokens refilled
        clock.advance(3.0)
        self.assertTrue(limiter.allow(tokens=5))
        self.assertFalse(limiter.allow(tokens=2))

    def test_burst_then_steady(self):
        clock = FakeClock()
        limiter = TokenBucketRateLimiter(capacity=5, refill_rate=1, clock=clock)

        # Burst: use all 5
        for _ in range(5):
            self.assertTrue(limiter.allow())
        self.assertFalse(limiter.allow())

        # Steady: 1 request per second should always succeed
        for _ in range(10):
            clock.advance(1.0)
            self.assertTrue(limiter.allow())

    def test_empty_bucket_stays_empty_without_time(self):
        clock = FakeClock()
        limiter = TokenBucketRateLimiter(capacity=1, refill_rate=100, clock=clock)

        self.assertTrue(limiter.allow())

        # No time passes
        self.assertFalse(limiter.allow())
        self.assertFalse(limiter.allow())
        self.assertFalse(limiter.allow())
