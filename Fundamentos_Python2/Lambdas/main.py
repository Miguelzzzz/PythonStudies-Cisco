print("Lambdas")

# Um iterador é um objeto de uma classe que fornece pelo menos dois métodos (sem contar o construtor):
# __iter__() é chamado uma vez quando o iterador é criado é retorna o próprio objeto do iterador;
# __next__() é chamado para fornecer o valor da próxima iteração e gera a exceção StopIteration quando a iteração chegar ao fim.

# Lambdas e a função map(), aplica a função transmitida pelo primeiro argumento a todos os elementos do segundo argumento e retorna um iterador que entrega todos os resultados subsequentes da função
# Exemplo pratico
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

# Lambdas e a função filter(), filtra seu segundo argumento enquanto é orientada pelas instruções provenientes da função especificada como o primeiro argumento
# Exemplo pratico
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

#  closure é uma técnica que permite o armazenamento de valores apesar do contexto em que foram criados não existir mais