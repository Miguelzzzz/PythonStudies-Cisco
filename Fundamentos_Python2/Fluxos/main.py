print("Abrindo os fluxos: modos")

# r modo aberto: leitura
# o fluxo será aberto no modo de leitura;
# o arquivo associado ao fluxo deve existir e deve ser legível, caso contrário, a função open() gerará uma exceção.

# w modo aberto: gravação
# o fluxo será aberto no modo de gravação;
# o arquivo associado ao fluxo não precisa existir; se não existir, será criado; se existir, será truncado para o comprimento zero (apagado); se a criação não for possível (por exemplo, devido a permissões do sistema), a função open() gerará uma exceção.

# a modo aberto: anexação
# o fluxo será aberto no modo de anexação;
# o arquivo associado ao fluxo não precisa existir; se não existir, será criado; se existir, o cabeçote de gravação virtual será definido no final do arquivo (o conteúdo anterior do arquivo permanece inalterado).

# r+ modo aberto: leitura e atualização
# o fluxo será aberto no modo de leitura e atualização;
# o arquivo associado ao fluxo deve existir e deve ser gravável, caso contrário, a função open() gerará uma exceção;
# operações de leitura e gravação são permitidas para o fluxo.

# w+ modo aberto: gravação e atualização
# o fluxo será aberto no modo de gravação e atualização;
# o arquivo associado ao fluxo não precisa existir; se não existir, será criado; o conteúdo anterior do arquivo permanece inalterado;.
# operações de leitura e gravação são permitidas para o fluxo.


# Abrindo um fluxo
try:
    stream = open("C:\Users\User\Desktopfile.tx", "rt")
    # Processamento fica aqui.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)


# Três fluxos predefinidos já estarão abertos na inicialização do programa:
# sys.stdin – entrada padrão;
# sys.stdout – entrada padrão;
# sys.stderr – saída de erro padrão.    