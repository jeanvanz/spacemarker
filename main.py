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
estrela=pygame.image.load('star.png')
fonte=pygame.font.Font(None,21)
pressF10=fonte.render('Pressione F10 para Salvar os Pontos',True,branco)
pressF11=fonte.render('Pressione F11 para Carregar os Pontos',True,branco)
pressF12=fonte.render('Pressione F12 para Deletar os Pontos',True,branco)
running=True
estrelas=[]
while running:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            quit()
        elif evento.type==pygame.MOUSEBUTTONUP:
            posicao=pygame.mouse.get_pos()
            nome=simpledialog.askstring('Space','Nomeie o ponto selecionado:')
            if nome == None:
                nome='desconhecido'+str(posicao)
            estrelas.append((nome,posicao))
            print(estrelas)
        elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_F12:
            estrelas=[]
    tela.blit(fundo,(0,0))
    tela.blit(pressF10,(10,20))
    tela.blit(pressF11,(10,40))
    tela.blit(pressF12,(10,60))
    for nome, posicao in estrelas:
        posicaoestrela=(posicao[0]-estrela.get_width()//2,posicao[1]-estrela.get_height()//2)
        tela.blit(estrela,posicaoestrela)
        textoestrela=fonte.render(nome,True,branco)
        tela.blit(textoestrela,(posicao[0],posicao[1]+estrela.get_height()//2+5))
    pygame.display.update()
    clock.tick(60)
pygame.quit()