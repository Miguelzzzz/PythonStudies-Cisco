print("Interação com usuario")

# Exemplo pratico 
print("Conta-me qualquer coisa...")
anything = input()  # Vai pedir uma resposta do usuario e armazenar em uma variavel
print("Hum...", anything, "... Realmente?")

anything = input("Conta-me qualquer coisa...")  #  Imprime uma mensagem para o usuario e pede uma resposta
print("Hum...", anything, "...Realmente?")

# Converto o valor da string para Float e faço as operações
anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)

# Metodo pra fazer operações na linha de impressão
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é", (leg_a**2 + leg_b**2) ** .5)

# O + serve pra concatenar e o * repetição/replicação
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# str() é uma função que permite transformar numeros em string

# Exemplo pratico
hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))
mins = mins + dura  # encontre um total de todos os minutos
hour = hour + mins // 60  # encontre um número de horas escondido em minutos e atualize a hora
mins = mins % 60  # minutos corretos para cair no intervalo (0..59)
hour = hour % 24  # horas corretas para cair no intervalo (0..23)
print(hour, ":", mins, sep='')