#Bibliotecas 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import investpy as py

plt.style.use('fivethirtyeight')

#Buscando dados

bonds = py.get_bonds_overview(country='brazil')
#print(bonds)
print('')

#Filtrando por nome e preço de fechamento

bonds2 = py.get_bonds_overview(country='brazil')[['name', 'last_close']]
#print(bonds2)

#Visualização:

plt.figure(figsize=(12, 6));
plt.title('Curva de Juros - Brazilians bonds');
plt.errorbar(bonds2.index, bonds2.last_close, marker='o', label='Curva de juros', color='blue', linewidth=1);
#plt.xlabel('Nome');
plt.ylabel('Valores de fechamento');
plt.xticks(bonds2.index, bonds2.name);
plt.legend()
plt.show();

'''#Outra forma:

pesq_fundos = py.funds.search_funds(by='name', value='Cdi')
print(pesq_fundos.head(10))

#Escolhendo o fundo 

fundo = pesq_fundos['name'][1]
print(fundo)

#Buscando os dados 

data = py.get_fund_historical_data(fund=fundo, country='brazil', from_date='01/01/2020', to_date='30/11/2021')['Close']
print(data.head())

retorno = data.pct_change().iloc[1:]
retorno_acum = (1 + retorno).cumprod()

#Visualização

plt.figure(figsize=(12, 6));
plt.title('Curva de Juros - Brazilians bonds');
plt.errorbar(retorno_acum.index, retorno_acum, label='Curva de juros', color='blue', linewidth=1)
plt.show()'''