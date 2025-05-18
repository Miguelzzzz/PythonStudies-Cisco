print("Metodos de Strings")


# Método capitalize()
print('aBcD'.capitalize())  # Retorna: Abcd


# Método center(), Centralização feita por meio da inclusão de espaços antes e depois da string
print('[' + 'alpha'.center(10) + ']') 


# Método endswith(), verifica se a string fornecida termina com o argumento especificado e retorna True ou False
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
# ex2:
t = "zeta"
print(t.endswith("a"))  # True
print(t.endswith("A"))  # False
print(t.endswith("et"))  # False
print(t.endswith("eta"))  # True


# Método find(), ele procura por uma substring e retorna o índice da primeira ocorrência desta substring
t = 'theta' 
print(t.find('eta'))  # 2
print(t.find('et'))  # 2
print(t.find('the'))  # 0
print(t.find('ha'))  # -1


# Método isalnum(), verifica se a string contém apenas dígitos ou caracteres alfabéticos (letras) e retorna True ou False
print('lambda30'.isalnum())  # True
print('lambda'.isalnum())  # True
print('30'.isalnum())  # True
print('@'.isalnum())  # False
print('lambda_30'.isalnum())  # False
print(''.isalnum())  # False


# Método isalpha(), ele se interessa apenas por letras retornando false ou true
print("Moooo".isalpha())  # True
print('Mu40'.isalpha())  # False


# Método isdigit(), utiliza apenas dígitos qualquer outra entrada produz False como resultado
print('2018'.isdigit())  # True
print("Year2019".isdigit())  # False


# Método islower(), aceita somente letras minúsculas
print("Moooo".islower())  # False
print('moooo'.islower())  # True


# Método isspace(), identifica somente os espaços em branco, ele ignora quaisquer outros caracteres (o resultado é False caso outros caracteres sejam usados)
print(' \n '.isspace())  # True
print(" ".isspace())  # True
print("mooo mooo mooo".isspace())  # False


# Método isupper(), se concentra apenas em letras maiúsculas
print("Moooo".isupper())  # False
print('moooo'.isupper())  # False
print('MOOOO'.isupper())  # True


# Método join(), o método executa uma junção, ele espera um argumento como uma lista; deve-se assegurar que todos os elementos da lista sejam strings
print(",".join(["omicron", "pi", "rho"]))  # Retorna: omicron,pi,rho


# Método lower(), faz uma cópia da string de origem, substitui todas as letras maiúsculas com suas equivalentes minúsculas e retorna a string como resultado
print("SiGmA=60".lower())  # Retorna: sigma=60


# Método lstrip(), retorna uma nova string, formada a partir da original por meio da remoção de todos os espaços em branco iniciais
print("[" + " tau ".lstrip() + "]")  # Retorna: [tau ]
print("www.cisco.com".lstrip("w."))  # Retorna: cisco.com


# Método replace(), com dois parâmetros, retorna uma cópia da string original em que todas as ocorrências do primeiro argumento foram substituídas pelo segundo argumento
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))  # Retorna: www.pythoninstitute.org
print("This is it!".replace("is", "are"))  # Retorna: Thare are it!
print("Apple juice".replace("juice", ""))  # Retorna: Apple 


# Método rfind(), iniciam suas buscas a partir do fim da string e não do início
print("tau tau tau".rfind("ta"))  # Retorna: 8
print("tau tau tau".rfind("ta", 9))  # Retorna: -1
print("tau tau tau".rfind("ta", 3, 9))  # Retorna: 4


# Método rstrip(), fazem praticamente o mesmo de lstrips, mas afetam o lado oposto da string
print("[" + " upsilon ".rstrip() + "]")  # Retorna: [ upsilon]
print("cisco.com".rstrip(".com"))  # Retorna: cis


# Método split(), divide a string e cria uma lista de todas as substrings detectadas
print("phi       chi\npsi".split())  # Retorna: ['phi', 'chi', 'psi']


# Método startswith(), verifica se uma determinada string começa com a substring especificada
print("omega".startswith("meg"))  # False
print("omega".startswith("om"))  # True


# Método strip(), o método strip() combina o efeito causado por rstrip() e lstrip() criando uma nova string sem os espaços em branco iniciais e finais
print("[" + "   aleph   ".strip() + "]")  # Retorna: [aleph]


# Método swapcase(), cria uma nova string ao inverter as letras maiúsculas para minúsculas e vice-versa
print("I know that I know nothing.".swapcase())  # Retorna: i KNOW THAT i KNOW NOTHING.


# Método title(), transforma a primeira letra de cada palavra em maiúscula e todas as outras letras em minúsculas
print("I know that I know nothing. Part 1.".title())  # Retorna: I Know That I Know Nothing. Part 1.


# Método upper(), cria uma cópia da string de origem, substitui todas as letras minúsculas com suas equivalentes maiúsculas e retorna a string como resultado
print("I know that I know nothing. Part 2.".upper())  # Retorna: I KNOW THAT I KNOW NOTHING. PART 2.