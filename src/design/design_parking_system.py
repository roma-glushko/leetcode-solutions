class DesignParkingSystem:
    """
    Problem Link: https://leetcode.com/problems/design-parking-system/
    Complexity: Easy
    Runtime: 132ms
    Memory: 14.9MB
    """

    def __init__(self, small: int, medium: int, big: int):
        self.parking_space: tuple[int, int, int] = (small, medium, big)

    def addCar(self, car_type: int) -> bool:
        car_room: int = car_type - 1  # zero indexed car rooms

        if self.parking_space[car_room] == 0:
            return False

        self.parking_space[car_room] -= 1

        return True
