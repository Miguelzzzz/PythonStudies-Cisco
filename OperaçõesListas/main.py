print("Operações em listas")

# Esta parte discreta do código descrito como [:] é capaz de produzir uma nova lista.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Fatias - índices negativos
# my_list[start:end]

# Apagando com del
my_list = [10, 8, 6, 4, 2]
del my_list[:]  # Exclui todos os valores da lista
print(my_list)

# Operadores in e not in
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)  # false
print(5 not in my_list)  # true
print(12 in my_list)  # true

# Exemplo pratico
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)