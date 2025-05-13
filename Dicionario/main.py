print("Dicionario")

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
phone_numbers = {'chefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# Exemplo pratico:
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
words = ['gato', 'lion', 'cavalo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "não está no dicionário")

# # Exemplo 1:
# dictionary = {
#               "gato": "chat",
#               "cachorro": "chien",
#               "cavalo": "cheval"
# }
# # Exemplo 2:
# phone_numbers = {'chefe': 5551234567,
#               'Suzy': 22657854310
# }


# Modificação e adição de valores
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}

dictionary['gato'] = 'minou'
print(dictionary)

# Removendo uma valor
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}

del dictionary['cachorro']
print(dictionary)
