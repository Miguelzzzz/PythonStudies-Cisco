print("Interagindo com o SO")

# A função uname retorna um objeto que contém informações sobre o sistema operacional atual. O objeto possui os seguintes atributos:
# systemname (armazena o nome do sistema operacional)
# nodename (armazena o nome da máquina na rede)
# release (armazena a versão do sistema operacional)
# version (armazena a versão do sistema operacional)
# machine (armazena o identificador de hardware, por exemplo x86_64).

# O atributo name disponível no módulo os permite distinguir o sistema operacional. Ele retorna um dos três valores a seguir:
# posix (você obterá esse nome se usar Unix)
# nt (você obterá esse nome se usar o Windows)
# java (você obterá esse nome se seu código for escrito em algo como Jython)

# A função mkdir cria um diretório no caminho passado como seu argumento. O caminho pode ser relativo ou absoluto, por exemplo:
# import os
# os.mkdir("hello") # caminho relativo
# os.mkdir("/home/python/hello") # caminho absoluto
# Observação: se o diretório existir, uma exceção FileExistsError será lançada. Além da função mkdir , o módulo os fornece a função makedirs , que permite criar recursivamente todos os diretórios em um caminho.

# O resultado da função listdir() é uma lista que contém os nomes dos arquivos e diretórios que estão no caminho passado como argumento.
# É importante lembrar que a função listdir omite as entradas '.' e '..', que são exibidas, por exemplo, ao usar o comando ls -a em sistemas Unix. Se o caminho não for passado, o resultado será retornado para o diretório de trabalho atual.

# Para mover entre diretórios, você pode usar uma função chamada chdir(), que altera o diretório de trabalho atual para o caminho especificado. Como argumento, ele toma qualquer caminho relativo ou absoluto.
# Se você quiser descobrir qual é o diretório de trabalho atual, você pode usar a função getcwd() , que retorna o caminho para ele.

# Para remover um diretório, você pode usar a função rmdir() mas para remover um diretório e seus subdiretórios, use a função removedirs() .

# Tanto no Unix quanto no Windows, você pode usar a função do sistema, que executa um comando passado a ela como uma string, por exemplo:
# import os
# returned_value = os.system("mkdir hello")
# A função do sistema no Windows retorna o valor retornado pelo shell após a execução do comando fornecido, enquanto Unix retorna o status de saída do processo.