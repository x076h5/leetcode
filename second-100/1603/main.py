class ParkingSystem:

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        car_types = {
            1: "big",
            2: "medium",
            3: "small",
        }

        cur_type = car_types[carType]
        value = getattr(self, cur_type)
        if not value: return False
        setattr(self, cur_type, value - 1)

        return True


if __name__ == "__main__":
    parkingSystem = ParkingSystem(1, 1, 0)
    print(parkingSystem.addCar(1))  # True
    print(parkingSystem.addCar(2))  # True
    print(parkingSystem.addCar(3))  # False
    print(parkingSystem.addCar(1))  # False
