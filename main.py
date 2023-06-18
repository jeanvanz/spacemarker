import pygame
from tkinter import simpledialog
pygame.init()
tamanho=(1280,720)
branco=(255,255,255)
tela=pygame.display.set_mode(tamanho)
clock=pygame.time.Clock()
fundo=pygame.image.load('bg.jpg')
tela.blit(fundo,(0,0))
icon=pygame.image.load('space.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Space Marker')
pygame.mixer.music.load('soundtrack.mp3')
pygame.mixer.music.play(-1)
fonte=pygame.font.Font(None,20)
running=True
estrelas=[]
nomeestrelas=[]
coordenadas=[]
while running:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            quit()
        elif evento.type==pygame.MOUSEBUTTONUP:
            posicao=pygame.mouse.get_pos()
            estrelas.append(posicao)
            nome=simpledialog.askstring('Space','Nomeie o ponto selecionado:')
            nomeestrelas.append(nome)
            print(nomeestrelas)
            print(posicao)
            if nome==None:
                item='desconhecido'+str(posicao)
            coordenadas.append((nome,posicao))
    tela.blit(fundo,(0,0))
    for nome, posicao in coordenadas:
        textoestrela=fonte.render(nome,True,branco)
        tela.blit(textoestrela,posicao)
    pygame.display.update()
    clock.tick(60)
pygame.quit()