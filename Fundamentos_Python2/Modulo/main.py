print("Modulos Introdução")

# Posso usar a palavra import pra tornar possivel o uso de bibliotecas

# Exemplo pratico:
import math  # Importo a biblioteca
print(math.sin(math.pi/2))  # Digo o nome do modulo que vou usar "." o nome da função/entidade que quero

# Forma mais simplificada
from math import sin, pi

print(sin(pi/2))

# Essa importação ira importar tudo que contem no modulo falado
# from module import *

# Usar "as" nas importações para alterar nomes de bibliotecas/modulos
    # import math as m
    # print(m.sin(m.pi/2))
