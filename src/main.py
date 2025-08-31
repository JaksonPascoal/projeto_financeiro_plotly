import pandas as pd
import plotly.graph_objects as go
import yfinance as yf

# Baixar os dados
ticker = 'AAPL'
df = yf.download(ticker, start='2024-01-01', end='2024-08-31')
df.to_csv('data/aapl_data.csv')
print("Dados salvos em data/aapl_data.csv")

# Criar o gráfico de velas (candlestick)
fig = go.Figure(data=[go.Candlestick(x=df.index,
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close'])])

# Adicionar título e rótulos
fig.update_layout(title=f'Histórico de Preços de {ticker}',
                  yaxis_title='Preço (USD)',
                  xaxis_rangeslider_visible=False)

# Exibir o gráfico no navegador
fig.show()