from __future__ import annotations
from abc import ABC, abstractmethod


class Shoes(ABC):
    @abstractmethod
    def create_adidas_shoes(self) -> AdidasShoes:
        pass

    @abstractmethod
    def create_nike_shoes(self) -> NikeShoes:
        pass


class RunningFactory(Shoes):
    def create_adidas_shoes(self) -> AdidasShoes:
        return AdidasRunningShoes()

    def create_nike_shoes(self) -> NikeShoes:
        return NikeRunningShoes()


class SkateboardingFactory(Shoes):
    def create_adidas_shoes(self) -> AdidasShoes:
        return AdidasSkateboardingShoes()

    def create_nike_shoes(self) -> NikeShoes:
        return NikeSkateboardingShoes()


class AdidasShoes(ABC):
    @abstractmethod
    def made_in_germany(self) -> str:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class AdidasRunningShoes(AdidasShoes):
    def made_in_germany(self) -> str:
        return "This is a running shoes made by Adidas in Germany."


class AdidasSkateboardingShoes(AdidasShoes):
    def made_in_germany(self) -> str:
        return "This is a skateboarding shoes made by Adidas in Germany."


class NikeShoes(ABC):
    @abstractmethod
    def supported_by_ronaldinho(self) -> None:
        pass

    @abstractmethod
    def another_supported_by_ronaldinho(self, collaborator: AdidasShoes) -> None:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class NikeRunningShoes(NikeShoes):
    def supported_by_ronaldinho(self) -> str:
        return "This is a Nike Running Shoes and Ronaldinhog like this one."

    def another_supported_by_ronaldinho(self, collaborator: AdidasShoes) -> str:
        result = collaborator.made_in_germany()
        return f"The result of the Nike Running shoes collaborating with the \
            ({result})"


class NikeSkateboardingShoes(NikeShoes):
    def supported_by_ronaldinho(self) -> str:
        return "This is a Nike Skateboarding Shoes and Ronaldinhog like this one"

    def another_supported_by_ronaldinho(self, collaborator: AdidasShoes):
        result = collaborator.made_in_germany()
        return f"The result of the Nike Skateboarding shoes collaborating with\
            the ({result})"


def client_code(factory: Shoes) -> None:
    product_a = factory.create_adidas_shoes()
    product_b = factory.create_nike_shoes()

    print(f"{product_b.supported_by_ronaldinho()}")
    print(f"{product_b.another_supported_by_ronaldinho(product_a)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(RunningFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(SkateboardingFactory())
