import pygame

#Para sortear uma posição ateatória para a Snake começar. 
from random import randint

#Códigos para cores
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
cinza = (205,193,197)

#Testando Pygame
try:
    pygame.init()
except:
    print('O Pygame não foi inicializado com sucesso.')

#Variáveis da tupla
largura=440
altura=320
tamanho = 10

#Relogio
relogio = pygame.time.Clock()

#Comando para definir altura e lagura da tela do jogo
fundo = pygame.display.set_mode((largura,altura))

#Comando para definir o título do Game e ícone(na parte superior esquerda da tela do game)
pygame.display.set_caption("Snake Evolution by Marcos Monteiro")

#Fonte
font = pygame.font.SysFont(None, 15)

def texto(msg, cor):
    texto1= font.render(msg, True, cor)
    fundo.blit(texto1, [largura/10, altura/2])

def Cobra(CobraXY):
    for XY in CobraXY:
    #Cria um retangulo, posição e tamanho dentro dos "[]"
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])

def apple(pos_x, pos_y):
    pygame.draw.rect(fundo, azul, [pos_x, pos_y, tamanho, tamanho])

def game():
    
    #Quebrar o loop do jogo
    sair = True
    gameover = False
    
    #Posição da Snake/tamanho
    pos_x = randint(0,(largura - tamanho)/10)*10
    pos_y = randint(0,(altura - tamanho)/10)*10
    apple_x = randint(0,(largura - tamanho)/10)*10
    apple_y = randint(0,(altura - tamanho)/10)*10
    velocidade_x = 0
    velocidade_y = 0
    CobraXY = []
    CobraCont = 1
    while sair:
        while gameover:
            fundo.fill(branco)
            texto("Game Over! Para continuar aperte C|S para sair", azul)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game()
                    if event.key == pygame.K_s:
                        sair = False
                        gameover = False
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False            
                
    #Condição para teclas
            if event.type == pygame.KEYDOWN:
                
    #Condição para tecla esquerda, diteita, cima e baixo.(Plano cartesiano)
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y =0
                    velocidade_x =-tamanho
                    #pos_x -= 10
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y =0
                    velocidade_x =tamanho
                    #pos_x += 10
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x =0
                    velocidade_y =-tamanho
                    #pos_y -= 10
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x =0
                    velocidade_y =tamanho
                    #pos_y += 10
                    
                    
    #Muda a cor do fundo da tela
        fundo.fill(cinza)

    #Velocidade
        pos_x += velocidade_x
        pos_y += velocidade_y

    #Inicio da cobra/adicionando blocos a snake

        CobraInicio = []
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)
        if len(CobraXY) > CobraCont:
            del CobraXY[0]

    #Condição para colisão
        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
            gameover = True
        


        
    #Chamando a função/ pegando o bloco tada vez que a snake chega em sua posição
        Cobra(CobraXY)
        if pos_x == apple_x and pos_y == apple_y:
            apple_x = randint(0,(largura - tamanho)/10)*10
            apple_y = randint(0,(altura - tamanho)/10)*10
            CobraCont += 1
        apple(apple_x,apple_y)
        pygame.display.update()

    #Relogio dentro do Loop, o valor dentro dos "()" define a velocidade da Snake
        relogio.tick(15)

    #Atravessar bordas
##        if pos_x > largura:
##            pos_x = 0
##        if pos_x < 0:
##            pos_x = largura - tamanho
##        if pos_y > altura:
##            pos_y = 0
##        if pos_y < 0:
##            pos_y= altura - tamanho

    #Quando encostar na borda o jogo fecha
        if pos_x > largura:
            gameover = True
        if pos_x < 0:
            gameover = True
        if pos_y > altura:
            gameover = True
        if pos_y < 0:
            gameover = True
game()    
#Comando para fechar a tela do game(Obs a tela abre e fecha logo em seguida)
pygame.quit()

