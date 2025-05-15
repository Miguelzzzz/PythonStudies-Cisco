print("Listas")

numbers = [10, 5, 7, 2, 1]  # Conteudo inicial
print("Conteúdos originais da lista:", numbers)  

numbers[0] = 111  # Altero o primeiro valor(0) para 111
print("\nConteúdo da lista anterior:", numbers)  

numbers[1] = numbers[4]  # Altero o segundo valor(5) para o mesmo do quinto(1)
print("Novo conteúdo da lista:", numbers)  

print(numbers[0])  # Imprime o valor especificado da posição

# função len() ira ler o comprimento de uma lista

# Posso usar del para apagar dados de uma posição especificada
del numbers[1]
print(len(numbers))
print(numbers)

# Adicionando elementos a uma lista: append() e insert()
# list.append(value) final da lista
# list.insert(location, value) pode colocar em um lugar especifico

# Exemplo pratico append
my_list = [] # Criando uma lista vazia.

for i in range(5):
    my_list.append (i + 1)

print (my_list)

# Exemplo pratico insert
my_list = []  # Criando uma lista vazia.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)
