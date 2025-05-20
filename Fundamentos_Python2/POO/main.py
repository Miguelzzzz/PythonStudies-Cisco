print("POO")

# Criando uma class
class TheSimplestClass:
    pass

my_first_object = TheSimplestClass()  # Instancia da classe

print()

print("Conceitos de pilhas")  # Nome alternativo é LIFO
# O conceito de pilha é que o ultimo elemento a entrar é o primeiro a sair 
# push (quando um novo elemento é colocado no topo) 
# pop (quando um elemento existente é retirado do topo)

# Exemplo pratico
stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

# Coloco os valore nessa ordem, então o ultimo a entrar seria o 1 e o primeiro 3
push(3)
push(2)
push(1)
# Ele retira os valores na ordem de saida, do ultimo pro primeiro
print(pop()) # Retorna: 1
print(pop()) # Retorna: 2
print(pop()) # Retorna: 3
