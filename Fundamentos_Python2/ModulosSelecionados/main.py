print("Modulos Selecionados")

# A função dir() ira revelar todos os nomes fornecidos pelo modulo para uso
# Exemplo pratico
import math

for name in dir(math):
    print(name, end="∖t")

# Existe o modulo random pra criar dados aleatorios
# O módulo random agrupa mais de 60 entidades projetadas para ajudá-lo a usar números pseudo-aleatórios. Não se esqueça do prefixo “aleatório”, pois não existem números aleatórios reais quando se trata de gerá-los usando os algoritmos do computador.





# O módulo platform contém aproximadamente 70 funções que permitem mergulhar nas camadas básicas do SO e do hardware. Usá-las permite que você aprenda mais sobre o ambiente em que seu código é executado.
# O módulo platform permite acessar os dados dos bastidores da plataforma, por exemplo, informações sobre hardware, sistema operacional e versão do interpretador.
# Exemplo pratico - Ela retorna uma string que descreve o ambiente, portanto, sua saída é mais voltada para pessoas do que para processamento automatizado 
from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))
# Ou se quiser saber apenas o nome generico do processador que executa seu SO
from platform import machine

print(machine())
# A função processor() retorna uma string que contém o nome real do processador
from platform import processor

print(processor())
# A função chamada system() retorna o nome genérico do SO como string.
from platform import system

print(system())
# A função version() fornece a versão do SO como uma string.
from platform import version

print(version())





# Funções do match
# O módulo math agrega mais de 50 símbolos (funções e constantes) que realizam operações matemáticas (como sine(), pow(), factorial()) ou que fornecem valores importantes (como π e o símbolo de Euler e).

# sin(x) → o seno de x;
# cos(x) → o cosseno de x;
# tan(x) → a tangente de x.

# asin(x) → o arco seno de x;
# acos(x) → o arco cosseno de x;
# atan(x) → o arco tangente de x.

# pi → uma constante com valor que é uma aproximação de π;
# radians(x) → uma função que converte x de graus para radianos;
# degrees(x) → função que trabalha na direção oposta (de radianos para graus)

# sinh(x) → o seno hiperbólico;
# cosh(x) → o cosseno hiperbólico;
# tanh(x) → a tangente hiperbólica;
# asinh(x) → o arco seno hiperbólico;
# acosh(x) → o arco cosseno hiperbólico;
# atanh(x) → o arco tangente hiperbólico.

# e → uma constante com valor que é uma aproximação do número de Euler (e)
# exp(x) → descobre o valor de ex;
# log(x) → logaritmo natural de x
# log(x, b) → logaritmo de x na base b
# log10(x) → logaritmo decimal de x (mais preciso que log(x, 10))
# log2(x) → logaritmo binário de x (mais preciso que log(x, 2))
# pow(x, y) → descobre o valor de xy (atenção aos domínios)

# ceil(x) → o teto de x (o menor número inteiro maior ou igual a x)
# floor(x) → o piso de x (o maior inteiro menor ou igual a x x)
# trunc(x) → o valor do truncamento de x em número inteiro (atenção: não é equivalente a ceil ou floor)
# factorial(x) → retorna x! (x precisa ser um número natural, não pode ser negativo)
# hypot(x, y) → retorna o comprimento da hipotenusa de um triângulo retângulo com lados iguais a x e y (o mesmo que sqrt(pow(x, 2) + pow(y, 2)) mas mais preciso)