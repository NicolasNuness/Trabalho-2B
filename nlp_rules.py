import re

def normalize_text(t):
    return ' '.join(t.lower().strip().split())

def nl_to_cpc_rule_based(text, mapping):
    # text: frase em português
    # mapping: dict texto->símbolo, ex: {'chover':'P', 'a grama ficará molhada':'Q'}
    text_norm = normalize_text(text)
    # condicional: se X, então Y
    m = re.search(r'se (.*?)(?:, )?ent(ã|a)o (.*)', text_norm)
    if m:
        a = m.group(1).strip().rstrip(' .')
        b = m.group(3).strip().rstrip(' .')
        Pa = mapping.get(a)
        Pb = mapping.get(b)
        if not Pa or not Pb:
            return None
        return f'({Pa} -> {Pb})'
    # conjunção simples: "X e Y"
    m2 = re.search(r'(.+?) e (.+)', text_norm)
    if m2:
        a = m2.group(1).strip().rstrip(' .')
        b = m2.group(2).strip().rstrip(' .')
        Pa = mapping.get(a)
        Pb = mapping.get(b)
        if Pa and Pb:
            return f'({Pa} & {Pb})'
    # negação simples: "não X"
    m3 = re.search(r'não (.+)', text_norm)
    if m3:
        a = m3.group(1).strip().rstrip(' .')
        Pa = mapping.get(a)
        if Pa:
            return f'(~{Pa})'
    return None