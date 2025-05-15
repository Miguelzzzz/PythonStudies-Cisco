print("Escopos em Python")

# Exemplo pratico:
def my_function():
    print("Eu conheço aquela variável?", var)  # texto + 1

var = 1
my_function()
print(var)  # 1

# Criando variavel global:
def my_function():
    global var
    var = 2
    print("Eu conheço aquela variável?", var)  # texto + 2

var = 1
my_function()
print(var)  # 2 