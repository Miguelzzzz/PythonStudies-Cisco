print("Dados literais: ")

print()

print("2", "String")  # String, o 2 é um elemento textual
print(2, "Numero int")    # Int, o 2 representa um numero inteiro. Numeros desprovidos da parte fracionaria
            # Float, numero capaz de representar a parte fracionaria

print()

# Se um número inteiro for precedido por um prefixo 0O ou 0o, ele será tratado como um valor octal.
print(0o123, "Octal")  # Resultado igual a 83

# Se um número inteiro for precedido por um prefixo 0x ou 0X, ele será tratado como um valor hexadecimal .
print(0x123, "Hexadecimal")  # Resultado igual a 291

print()


# Float
    # Numero capaz de representar a parte fracionaria
        # O ponto é o elemento separador dos numeros
print(-0.5, "Float")

# Lidando com notação cietifica: 3 x 10'8 (x10 pode ser lido em float com E)
print(3E8, "Notação cietifica")
print(6.62607E-34, "Notação cietifica")

print()

# Usar aspas como string 
print("Eu gosto \"Monty Python\"  -  Barra invertida")  # Barra invertida como valvula de escape
print('Eu gosto "Monty Python"  -  Aspas simples')  # Outra forma é usar aspas simples para delimitar o texto
# Barra invertida tambem pode ser usada para apostrafo textual, sempre usar ela quando quiser que o elemento seja lido como texto

print()

# Valores booleanos
    # Valor pode ser True(1) ou False(0)
print(True > False)  # Resultado True
print(True < False)  # Resultado False

# O literal None. Esse literal é um objeto NoneType e é usado para representar a ausência de um valor