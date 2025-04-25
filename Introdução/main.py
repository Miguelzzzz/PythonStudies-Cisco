# Esse é o simbolo usado pra fazer comentarios

# Imprime uma mensagem
print("Hello World")
# Pula uma linha
print()

# O \n vai quebrar a linha
print("A aranha pequenininha\nsubiu a parede.")
print()
print("e veio a chuva forte\ne a levou.")

# A "," serve para separar os argumentos(Fica invisivel)
print("A aranha pequenininha" , "subiu" , "a tromba d'água.")

# O end= vai fazer com que a mensagem abaixo fique na linha de acima onde possui o comando (só funciona em uma linha abaixo)
print("Meu nome é", "Python.", end=" ")
print("Monty Python.")

# O sep= vai criar um elemento separador, entao onde existe "," que serve pra separar os argumento vai aparecer "-" ou elemento especificado 
print("Meu", "nome", "é", "Monty", "Python.", sep="-")

    # Ambos argumentos, end e sep podem ser usados em conjunto 

# Vai usar os argumentos pra exibir o resultado "Programação***Essenciais***em...Python"
print("Programação",  "Essenciais", "em", sep="***", end="...")
print("Python")