print("PIP")

# pip help operação – mostra uma breve descrição do pip;
# pip list – mostra uma lista dos pacotes instalados atualmente;
# pip show nome_pacote – mostra a info do nome_pacote incluindo as dependências do pacote;
# pip search anystring – busca os diretórios do PyPI por pacotes cujos nomes contenham anystring;
# pip install nome – instala nome em todo o sistema (é esperado que ocorram problemas caso você não tenha direitos administrativos);
# pip install --user nome – instala nome somente para você; nenhum outro usuário da plataforma conseguirá usá-lo;
# pip install -U nome – atualiza um pacote instalado anteriormente;
# pip uninstall nome – desinstala um pacote instalado anteriormente.

# Exemplo pratico
import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False