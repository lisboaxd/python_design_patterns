from __future__ import annotations
from abc import ABC, abstractmethod


class VehicleCreator(ABC):
    """
    The Vehicle class declares the create_vehicle factory method that is
    supposed to return an object of a Product class. The Vehicle's subclasses
    usually provide the implementation of this method.
    """

    @abstractmethod
    def create_vehicle(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def start(self) -> str:
        car = self.create_vehicle()
        result = f"Vehicle Creator based class: The same creator's code has \
just worked with {car.after_started()}"
        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class VolkwagenCreator(VehicleCreator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def create_vehicle(self) -> Car:
        return VolkswagenCar()


class FerrariCreator(VehicleCreator):
    def create_vehicle(self) -> Car:
        return FerrariCar()


class Car(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def after_started(self) -> str:
        pass


"""
Concrete Car Products provide various implementations of the Car interface.
"""


class VolkswagenCar(Car):
    def after_started(self) -> str:
        return "Volkswagen car was started using a Physical Key"


class FerrariCar(Car):
    def after_started(self) -> str:
        return "Ferrari car was started using a Digital key"


def client_code(vehicle_creator: VehicleCreator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit
    through its base interface. As long as the client keeps working with the
    creator via the base interface, you can pass it any creator's subclass.
    """

    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{vehicle_creator.start()}",
        end="",
    )


if __name__ == "__main__":
    print("App: Launched with the VolkwagenCreator.")
    client_code(VolkwagenCreator())
    print("\n")

    print("App: Launched with the FerrariCreator.")
    client_code(FerrariCreator())
