from math import fabs


class Car:
    def __init__(self, brand, model, speed, fuel):
        self.__brand = brand
        self.__model = model
        self.__speed = speed
        self.__fuel = fuel

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_speed(self):
        return self.__speed

    def get_fuel(self):
        return self.__fuel

    def set_speed(self, speed):
        if speed >= 0:
            self.__speed = speed

    def set_fuel(self, fuel):
        if fuel >= 0:
            self.__fuel = fuel


my_car = Car("Toyota", "Carolla", 100, 15)
print(my_car.get_brand())
print(my_car.get_model())
my_car.set_speed(250)
print(my_car.get_speed())
my_car.set_fuel(-5)
print(my_car.get_fuel())
