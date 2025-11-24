import streamlit as st
from src.nlp_rules import nl_to_cpc_rule_based
from src.parser_cpc import parse_cpc, ast_to_nl

st.set_page_config(page_title="Agente NL ⇄ CPC", layout="centered")

st.title("Agente NL ⇄ CPC — Tradução entre Português e Lógica Proposicional")
st.markdown("Escolha o modo, defina proposições e traduza frases simples.")

mode = st.radio("Modo", ["NL → CPC", "CPC → NL"])

st.subheader("Definições de proposições (ex: P=chover; Q=a grama ficará molhada)")
mapping_input = st.text_area("Mapping (separe por `;`):", value="P=chover; Q=a grama ficará molhada")

# Parse mapping input para dict
mapping = {}
for part in mapping_input.split(';'):
    if '=' in part:
        k, v = part.split('=', 1)
        mapping[k.strip()] = v.strip()

st.write("Proposições definidas:", mapping)

text = st.text_area("Entrada (frase NL ou fórmula CPC)")
if st.button("Traduzir"):
    if mode == "NL → CPC":
        # Invert mapping (texto -> symbol) para a função de regra simples
        inverted = {v.lower(): k for k, v in mapping.items()}
        result = nl_to_cpc_rule_based(text, inverted)
        if result:
            st.success("Fórmula CPC:")
            st.code(result)
        else:
            st.error("Não consegui parsear a frase com as regras simples. Tente reescrever ou usar o LLM opcional.")
    else:
        try:
            expr = parse_cpc(text)
            st.success("Frase em NL:")
            st.write(ast_to_nl(expr, mapping))
        except Exception as e:
            st.error(f"Erro ao parsear fórmula CPC: {e}")