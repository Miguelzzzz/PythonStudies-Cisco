print("Exceções")

# Usar try except
try:
    value = int (input('Insira um número natural:')) 
    print('O recíproco de', value, 'é', 1 / value) 
except ValueError:
    print('Não sei o que fazer.' ) 
except ZeroDivisionError:
    print('Divisão por zero não é permitida em nosso universo.') 
except: 
    print('algo de estranho aconteceu aqui ... Desculpe! ')

# ValueError para int e float
# TypeError é um nome adequado para descrever o problema e uma exceção adequada para gerar
# AttributeError quando você tenta ativar um método que não existe em um item com o qual está lidando
# SyntaxError quando o controle atinge uma linha de código que viola a gramática do Python
# ArithmeticError uma exceção abstrata, incluindo todas as exceções causadas por operações aritméticas como divisão por zero ou o domínio inválido de um argumento
# AssertionError uma exceção concreta gerada pela instrução assert quando o argumento for False, None, 0 ou uma string vazia
# BaseException a mais geral (abstrata) de todas as exceções do Python, todas as outras exceções estão inclusas nessa; pode-se dizer que as duas ramificaçõesexcept a seguir são equivalentes: except: e except BaseExceptio
# IndexError uma exceção concreta gerada quando se tenta acessar o elemento não existente de uma sequência (por ex., o elemento de uma lista)
# KeyboardInterrupt uma exceção concreta gerada quando o usuário usa um atalho do teclado criado para finalizar a execução de um programa (Ctrl-C na maioria dos S.O.s); se o processamento dessa exceção não levar à finalização do programa, o programa continuará sua execução
# LookupError uma exceção abstrata, incluindo todas as exceções causadas por erros resultantes de referências inválidas a diferentes coleções (listas, dicionários, tuplas, etc.)
# MemoryError uma exceção concreta, gerada quando não é possível completar uma operação por falta de memória livre.
# OverflowError uma exceção concreta, gerada quando uma operação produz um número grande demais para ser armazenado com sucesso
# ImportError uma exceção concreta, gerada quando ocorre uma falha em uma operação de importação
# KeyError  uma exceção concreta gerada quando você tenta acessar um elemento não existente em uma coleção (por ex., o elemento de um dicionário)