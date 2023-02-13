from abc import ABC, abstractmethod
from typing import TypeVar

Self = TypeVar("Self", bound="Expr")


class Expr(ABC):
    @abstractmethod
    def evaluate(self, env: dict[str, int | Self]) -> int:
        pass
