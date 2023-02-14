from src.expression.Expr import Expr
from src.expression.Func import Func

class While(Expr):
    type: str
    condition: Expr
    body: Expr

    def __init__(self, condition: Expr, body: Expr):
        self.type = "While"
        self.condition = condition
        self.body = body
    
    def evaluate(self, env: dict[str, int | Func]) -> int:
        ret = 0
        while self.condition.evaluate(env):
            ret = self.body.evaluate(env)
        return ret
        
    def __str__(self):
        return "While(condition:%s, body:%s)" % (str(self.condition), str(self.body))