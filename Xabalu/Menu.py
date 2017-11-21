import os
import pygame
import sys

pygame.init()

folder = "img"

def menu(estado):
    #Criação
    tela = pygame.display.set_mode((600,400),0,32)

    #Fontes
    fonte1 = pygame.font.Font(None, 64)
    fonte2 = pygame.font.Font(None, 40)

    #Imagens
    imagem = pygame.image.load(os.path.join(folder, "background.jpg"))
    fundo = pygame.transform.scale(imagem,(600,400))
    
    while estado:
        # x- Sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # New Game
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 220 and x < 380) and (y > 130 and y < 155):
                        return "Jogo"
                        estado = False
            #Help
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 180 and x < 380) and (y > 170 and y < 200):
                        return "ajuda"
                        estado = False
            #Creditos        
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 215 and x < 370) and (y > 240 and y < 265):
                        return "creditos"
                        estado = False
            #Sair
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 240 and x < 340) and (y > 290 and y < 320):
                        return "sair"
                        estado = False
        
        tela.blit(fundo,(0,0))
        pygame.display.flip()

def ajuda(estado):
    #Criação
    tela = pygame.display.set_mode((600,400),0,32)

    #Fontes
    fonte1 = pygame.font.Font(None,30)
    voltar = fonte1.render("Voltar",1,(255,255,255))
    
    #Imagens
    imagem = pygame.image.load(os.path.join(folder, "Como jogar.jpg"))
    fundo = pygame.transform.scale(imagem,(600,400))
    
    while estado:
        # x - sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Sair
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 220 and x < 280) and (y > 300 and y < 320):
                        pygame.quit()
                        sys.exit()
             #Menu
            if evento.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 540 and x < 590) and (y > 370 and y < 390):
                        return "menu"
                        estado = False
                        
        tela.blit(fundo,(0,0))
        pygame.display.flip()


def creditos(estado):
    #Criação
    tela = pygame.display.set_mode((700,500),0,32)

    #Fontes
    fonte1 = pygame.font.Font(None,30)
    voltar = fonte1.render("Voltar",1,(255,255,255))
    
    #Imagens
    imagem = pygame.image.load(os.path.join(folder, "Creditos.jpg"))
    fundo = pygame.transform.scale(imagem,(700,500))
    
    while estado:
        # x - sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Sair
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 220 and x < 280) and (y > 300 and y < 320):
                        pygame.quit()
                        sys.exit()
             #Menu
            if evento.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed() == (1,0,0):
                    x,y = pygame.mouse.get_pos()
                    if (x > 595 and x < 680) and (y > 470 and y < 490):
                        return "menu"
                        estado = False

        tela.blit(fundo,(0,0))
        pygame.display.flip()

#def jogo(estado):


        

porta = "menu"

while porta == "menu":
    porta = menu(True)
    if porta == "sair":
        pygame.quit()
        sys.exit()
    while porta == "ajuda":
        porta = ajuda(True)
    while porta == "jogo":
        porta = jogo(True)
    while porta == "creditos":
        porta = creditos(True)
