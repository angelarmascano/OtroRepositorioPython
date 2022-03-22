# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 20:28:31 2022

@author: Compaqi5
"""

import pandas as pd

titulos = pd.read_csv('titles.csv')
print(titulos.head(10))
print("\n"*2)
elenco = pd.read_csv('cast.csv')
print(elenco.head(10))
print(titulos[titulos.title.str.contains('war')].sort_values('year'))
print(titulos[titulos.title=="Dracula"].sort_values('year'))
print(titulos[titulos.title.str.contains('Dracula')].sort_values('year'))
print(titulos[titulos.title.str.contains('Lord of the Rings')].sort_values('year'))
print(len(titulos[titulos.title.str.contains('Lord of the Rings')].sort_values('year')))