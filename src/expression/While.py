from src.expression.Expr import Expr

class While(Expr):
    type: str
    condition: Expr
    body: Expr

    def __init__(self, condition: Expr, body: Expr):
        self.type = "While"
        self.condition = condition
        self.body = body
    
    def evaluate(self, env: dict[str, int | Expr]) -> int:
        ret = 0
        while self.condition.evaluate(env):
            ret = self.body.evaluate(env)
        return ret
        