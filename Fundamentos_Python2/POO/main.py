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

# SubClasses: Uma função chamada issubclass(Class_1, Class_2) é capaz de determinar se Class_1 é uma subclasse de Class_2
# Exemplo pratico:
class Mouse:
    pass

class LabMouse(Mouse):
    pass

print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse))

# Uma função chamada isinstance(Object, Class) verifica se um objeto é proveniente de uma classe indicada
# Exemplo pratico:
class Mouse:
    pass

class LabMouse(Mouse):
    pass

mickey = Mouse()
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))

# Uma função sem parâmetro chamada super() retorna uma referência à superclasse mais próxima da classe
# Exemplo pratico:
class Mouse:
    def __str__(self):
        return "Mouse"

class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()

doctor_mouse = LabMouse()
print(doctor_mouse)