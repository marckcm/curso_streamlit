# Estudos de Streamlit

Repositório de aprendizado com [Streamlit](https://streamlit.io/) em Python. O projeto usa **uv** para dependências e um ambiente virtual local (`.venv`).

## Requisitos

- Python **3.13+** (conforme `pyproject.toml`)
- [uv](https://docs.astral.sh/uv/) instalado

## Configuração do ambiente

Na pasta raiz do projeto (`curso_streamlit`):

```powershell
uv sync
```

Isso cria/atualiza o `.venv` e instala as dependências definidas em `pyproject.toml` / `uv.lock`.

Para adicionar pacotes no futuro:

```powershell
uv add nome-do-pacote
```

## Executar um app

Exemplo com o script da primeira aula:

```powershell
uv run streamlit run aula_01.py
```

Com o ambiente já ativado (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run aula_01.py
```

O navegador abre na URL indicada no terminal (em geral `http://localhost:8501`).

## Estrutura do repositório

| Item | Descrição |
|------|-----------|
| `aula_01.py` | Primeiros passos: textos, títulos e Markdown |
| `pyproject.toml` | Metadados do projeto e dependências |
| `uv.lock` | Versões fixas das dependências (gerado pelo uv) |
| `requirements.txt` | Referência opcional; o fluxo principal é `uv` |

## Cursor / VS Code e imports

Abra esta pasta **como raiz do workspace** (`curso_streamlit`), para o interpretador apontar para `.venv` e o Pylance reconhecer o Streamlit.

O `pyproject.toml` inclui `[tool.pyright]` com `venvPath` e `venv` para alinhar a análise estática ao `.venv`, inclusive em subpastas que você for criando.

## Referências

- [Documentação do Streamlit](https://docs.streamlit.io/)
- [Documentação do uv](https://docs.astral.sh/uv/)
