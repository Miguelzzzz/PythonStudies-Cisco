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