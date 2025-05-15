print("Lops de repetição")

print()

print("Laço com while")

# Exemplo lop infinito
# while True:
#     print("Estou preso dentro de um loop.")

print()

# Exemplo pratico do while
numeros_impares = 0
numeros_pares = 0

# Leia o primeiro número.
number = int(input("Digite um número ou digite 0 para parar: "))

# 0 termina a execução.
while number != 0:
    # Verifique se o número é ímpar.
    if number % 2 == 1:
        # Aumente o contador numeros_impares.
        numeros_impares += 1
    else:
        # Aumente o contador numeros_pares.
        numeros_pares += 1
    # Leia o número seguinte.
    number = int(input("Digite um número ou digite 0 para parar: "))

# Imprimir resultados.
print("Números ímpares contam:", numeros_impares)
print("Números pares contam:", numeros_pares)

print()

# Laço usando counter
counter = 5
while counter:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)

print()

print("Laço com for")

# Exemplo pratico do for
# Vai começar no 0 e ir ate o 9
for aux in range(10):
    print("O valor aux é atualmente", aux)

# Exemplo com dois argumentos  
# Vai começar no 2 e ir ate o 7
for aux in range(2, 8):
    print("O valor de aux é atualmente", aux)    

# Exemplo com tres argumentos 
# Vai do 2 ate o 8 de tres em tres
for aux in range(2, 8, 3):
    print("O valor de aux é atualmente", aux)    


# Break e Continue    
# break - sai do loop imediatamente e termina incondicionalmente a operação do loop; o programa começa a executar a instrução mais próxima após o corpo do loop;
# continue - se comporta como se o programa tivesse chegado ao fim do corpo; o próximo turno é iniciado e a expressão de condição é testada imediatamente.

# break - exemplo

print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")

# continue - exemplo

print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i)
print("Fora do loop.")

# exemplo pratico

while True:
    palavra = input("Insira uma palavra ou digite chupacabra para finalizar o programa: ")
    if palavra == "chupacabra":
        break

print("Você saiu do loop com sucesso!")
