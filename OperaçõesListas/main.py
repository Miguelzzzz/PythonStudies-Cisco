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

# Listas com operações avançadas
twos = [2 ** i for i in range(8)]  # O fragmento cria uma matriz de oito elementos que contém as oito primeiras potências de dois (1, 2, 4, 8, 16, 32, 64, 128)

# Criando uma matriz
EMPTY = "."
board = [[EMPTY for i in range(8)] for j in range(8)]
board[7][7] = "ROOK"  # Dou um valor a uma posição especifica
for row in board:
    print(" ".join(row))


# Exemplo pratico
# Cubo - uma matriz tridimensional (3x3x3)

cube = [[[':(', 'x', 'x'],
        [':)', 'x', 'x'],
        [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
        [':(', 'x', 'x'],
        [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
        [':)', 'x', 'x'],
        [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'