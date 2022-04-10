from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class AbstractBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        ...

    @abstractmethod
    def produce_trip_computer(self) -> None:
        ...

    @abstractmethod
    def produce_sunroof(self) -> None:
        ...

    @abstractmethod
    def produce_ac(self) -> None:
        ...

    @abstractmethod
    def produce_power_windows(self) -> None:
        ...


class ConcreteBuilder(AbstractBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Car()

    @property
    def product(self) -> Car:
        product = self._product
        self.reset()
        return product

    def produce_trip_computer(self) -> None:
        self._product.add("Trip Computer")

    def produce_sunroof(self) -> None:
        self._product.add("Sunroof")

    def produce_ac(self) -> None:
        self._product.add("AC")

    def produce_power_windows(self) -> None:
        self._product.add("Power Windows")


class Car:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Car has parts: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> AbstractBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: AbstractBuilder) -> None:
        self._builder = builder

    def build_minimal_viable_car(self) -> None:
        self.builder.produce_ac()

    def build_full_featured_car(self) -> None:
        self.builder.produce_ac()
        self.builder.produce_sunroof()
        self.builder.produce_power_windows()
        self.builder.produce_trip_computer()


if __name__ == "__main__":

    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder

    print("Standard basic Car: ")
    director.build_minimal_viable_car()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured Car: ")
    director.build_full_featured_car()
    builder.product.list_parts()

    print("\n")

    print("Custom product: ")
    builder.produce_sunroof()
    builder.produce_trip_computer()
    builder.product.list_parts()
