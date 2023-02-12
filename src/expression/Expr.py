from abc import ABC, abstractmethod


class Expr(ABC):
    type: "Expr"

    @abstractmethod
    def evaluate(self):
        pass
