# Observatório Financeiro (Plotly)

Dashboard estático com **gráficos interativos em Plotly** a partir de dados de mercado.
Atualmente publica os tickers **AAPL** e **MSFT**.

> As páginas são geradas em `docs/` e publicadas via **GitHub Pages** (branch `main`, pasta `/docs`).

---

## O que tem aqui

- **Gráficos**: Candlestick, Volume, **SMA(20)**, **RSI(14)**, **MACD(12,26,9)**, **Bandas de Bollinger**, **ATR(14)**, **Retorno acumulado** e **Heatmap mensal**.
- **Tema**: dark por padrão (visual moderno e consistente).
- **Armazenamento**: tudo em HTML estático dentro de `docs/`, ideal para Pages.

---

## Fontes de dados

Tentativa em múltiplos provedores (fall-back automático):
1. **Stooq**
2. **Yahoo** / **yfinance**
3. **CSV local** em `data/<TICKER>.csv`  
   (colunas: `Date,Open,High,Low,Close,Volume`)

> Alguns ativos podem ser bloqueados no Yahoo; o CSV local garante o fallback.

---

## Estrutura do repositório

projeto_financeiro_plotly/
├─ docs/ # site publicado (GitHub Pages)
│ ├─ index.html # home
│ ├─ AAPL/.html # painéis por ticker
│ └─ MSFT/.html
├─ src/
│ ├─ exploracao_dados.ipynb # gerador das páginas
│ └─ main.py (opcional)
├─ data/ # CSVs opcionais de fallback
├─ requirements.txt
└─ README.md


---

## Créditos

Feito por **Jakson Pascoal** — ciência com método, arte com medida.
