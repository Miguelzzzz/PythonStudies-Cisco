print("Funções")

# Exemplo pratico:
def message():
    print("Entre um valor: ")

print("Começamos aqui.")
message()  # Ira imprimir a mensagem da função nesse local
print("terminamos aqui.")

# Funções com parametros:
# def function(parameter):
# Exemplo pratico:
def message(what, number):
    print("Entrar", what, "número", number)

message("telefone", 11)
message("preço", 5)
message("número", "número")

# Exemplo pratico:
def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

# Com string
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


# Passagem de parametro por palavra-chave:
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")