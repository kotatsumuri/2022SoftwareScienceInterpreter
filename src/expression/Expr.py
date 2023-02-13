from abc import ABC, abstractmethod
from src.expression.Func import Func
from typing import TypeVar


class Expr(ABC):
    @abstractmethod
    def evaluate(self, env: dict[str, int | Func]) -> int:
        pass
