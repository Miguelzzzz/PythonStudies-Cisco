print("Tomada de Decisões")

# = É usado no sentido de atribuição
# == É usado no sentido de igualar um valor ao outro

var = 0 # Atribuindo 0 a var
print(var == 0)  # Resultado True

var = 1 # Atribuindo 1 a var
print(var == 0)  # Resultado False
print()

# Pode-se atribuir uma ! para mudar o sentido da resposta, sendo o contrario que não é igual
var = 0  # Atribuindo 0 a var
print(var != 0)

var = 1  # Atribuindo 1 a var
print(var != 0)
print()

# Outros tipo são
# current_velocity_mph < 85  Menor que
# current_velocity_mph <= 85  Menos que ou igual a
# current_velocity_mph > 85  Maior que
# current_velocity_mph => 85  Maior que ou igual a

# Exemplo pratico
valor = int(input("Digite um valor: "))
print(valor >= 100)
print()



# Laços de repetição
# Dando valores
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Dando um dos valores a uma variavel
NumMaior = n1

# Laços feitos para descobrir o maior numero
if n2 > NumMaior: NumMaior = n2
if n3 > NumMaior: NumMaior = n3

print("O maior número é:", NumMaior)
print()

# Como fazer o caso acima usando max ao invez do if
# Leia três números.
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

# Verifique qual dos números é o maior
# e passe-o para a variável de número_maior.
largest_numberMax = max(number1, number2, number3)
largest_numberMin = min(number1, number2, number3)
# Imprimir o resultado.
print("O maior número é:", largest_numberMax)
print("O menor número é:", largest_numberMin)
print()



# Exercicio simples com laço
dadoRecebido = input("Digite alguma coisa: ")

if dadoRecebido == "Spathiphyllum": 
    print("Sim - Spathiphyllum é a melhor fábrica de todos os tempos!")
elif dadoRecebido == "spathiphyllum":
    print("Não, eu quero um grande Spathiphyllum!")
else: 
    print("Spathiphyllum! Not[input]!")