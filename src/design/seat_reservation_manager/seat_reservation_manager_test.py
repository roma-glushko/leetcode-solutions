from .seat_reservation_manager import SeatManager


def test__default_input() -> None:
    man = SeatManager(5)

    for exp_seat in range(1, 3):
        seat = man.reserve()
        assert seat == exp_seat

    man.unreserve(2)

    for exp_seat in range(2, 6):
        seat = man.reserve()
        assert seat == exp_seat

    man.unreserve(5)
