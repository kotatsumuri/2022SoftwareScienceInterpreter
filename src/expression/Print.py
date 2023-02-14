from src.expression.Expr import Expr

class Print(Expr):
    type: str
    body: Expr

    def __init__(self, body: Expr):
        self.type = "Print"
        self.body = body
    
    def evaluate(self, env: dict[str, int | Expr]) -> int:
        ret = self.body.evaluate(env)
        print(ret)
        return ret