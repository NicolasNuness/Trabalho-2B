from .nlp_rules import nl_to_cpc_rule_based
from .parser_cpc import parse_cpc, ast_to_nl

def nl_to_cpc(text, mapping_text_to_symbol):
    return nl_to_cpc_rule_based(text, mapping_text_to_symbol)

def cpc_to_nl(formula, mapping_symbol_to_text):
    expr = parse_cpc(formula)
    return ast_to_nl(expr, mapping_symbol_to_text)