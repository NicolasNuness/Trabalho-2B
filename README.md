## 🔗 Link do Agente Online (Deploy)

Acesse o agente de IA hospedado no Streamlit Cloud aqui:

https://agente-ia-web-nupexk5mvvqgldvnsjvrrq.streamlit.app/



# Agente de IA para Web — Tradução NL ↔ CPC

Material entregue para a atividade: Agente que traduz entre **Linguagem Natural (português)** e **Cálculo Proposicional Clássico (CPC)**.

## Estrutura do repositório
```
agente-ia-web/
├─ README.md
├─ requirements.txt
├─ app.py
├─ src/
│  ├─ parser_cpc.py
│  ├─ nlp_rules.py
│  ├─ translator.py
│  └─ llm_helper.py
├─ docs/
│  └─ arquitetura.png
└─ examples/
   ├─ exemplos_nl.txt
   └─ exemplos_cpc.txt
```

## 1) Arquitetura e funcionamento (resumo)
- **Frontend (Streamlit)**: recebe entradas do usuário, modo (NL→CPC ou CPC→NL), e o mapeamento de proposições.
- **Módulo de Tradução**: contém regras NL→CPC (regex + lógica simples) e parser CPC→NL (usa SymPy).
- **Módulo de Mapeamento**: o usuário define P,Q,R,... com textos (ex: `P = chover`).
- **(Opcional) Módulo LLM**: fallback para frases complexas e sugestões de mapeamento.

## 2) Estratégia de tradução
- Regras detectam: condicional ("se ... então ..."), conjunção ("e"), disjunção ("ou"), negação ("não"), bicondicional ("se e somente se").
- Quando ambíguo, o sistema pede confirmação ou chama um LLM (opcional) para sugerir parse.

## 3) Exemplos I/O (usar em `examples/`)
- NL: `Se chover, então a grama ficará molhada.`
  - Mapping: `P=chover; Q=a grama ficará molhada`
  - CPC esperado: `P -> Q`
- CPC: `(P & Q) -> R`
  - Mapping: `P=chover; Q=fizer frio; R=aula será cancelada`
  - NL esperado: `Se chover e fizer frio, então a aula será cancelada.`

## 4) Instruções para execução local (passo a passo)
1. Crie e ative um ambiente virtual:
   - Linux/macOS: `python -m venv venv && source venv/bin/activate`
   - Windows (PowerShell): `python -m venv venv; .\venv\Scripts\Activate.ps1`
2. Instale dependências: `pip install -r requirements.txt`
3. Rode a aplicação: `streamlit run app.py`
4. Abra no navegador: `http://localhost:8501`

## 5) Checklist (arquivos que você deve subir no repositório)
- Código versionado (GitHub)
- `README.md` (este arquivo)
- `requirements.txt`
- `app.py`
- `src/` com os módulos
- `examples/` com exemplos de I/O
- Link do vídeo de demonstração (colocar no README após gravar)

## 6) Pontuação e entrega
- Ao seguir este repositório com o app funcional e o README completo, vocês cobrem todos os itens exigidos pelo enunciado.
- Para ganhar os 5 pontos adicionais, hospede a aplicação online e deixe o link no README.

---
