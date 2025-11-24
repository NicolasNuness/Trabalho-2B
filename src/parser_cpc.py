from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols
from sympy.logic.boolalg import Implies, And, Or, Not, Equivalent
import sympy as sp

def preprocess_formula(s: str) -> str:
    # torna compatível com o parseador do sympy
    s = s.replace("->", ">>").replace("→", ">>")
    s = s.replace("<->", "==").replace("↔", "==")
    s = s.replace("∧", "&").replace("and", "&")
    s = s.replace("∨", "|").replace("or", "|")
    s = s.replace("¬", "~").replace("not", "~")
    return s

def parse_cpc(formula_str: str):
    s = preprocess_formula(formula_str)
    expr = parse_expr(s, evaluate=False)
    return expr

# Conversão simplificada de AST para linguagem natural
def ast_to_nl(expr, mapping):
    # mapping: {'P': 'chover', ...}
    from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent
    def rec(e):
        if e.func == And:
            return f"{rec(e.args[0])} e {rec(e.args[1])}" if len(e.args)==2 else ' e '.join(rec(a) for a in e.args)
        if e.func == Or:
            return f"{rec(e.args[0])} ou {rec(e.args[1])}" if len(e.args)==2 else ' ou '.join(rec(a) for a in e.args)
        if e.func == Not:
            return f"não {rec(e.args[0])}"
        if e.func == Implies:
            return f"Se {rec(e.args[0])}, então {rec(e.args[1])}"
        if e.func == Equivalent:
            return f"{rec(e.args[0])} se e somente se {rec(e.args[1])}"
        # símbolo
        name = str(e)
        return mapping.get(name, name)
    return rec(expr)