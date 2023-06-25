import pygame
from tkinter import simpledialog
import math 
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
estrelas={}
def calcular_distancia(ponto1, ponto2): 
    return math.sqrt((ponto2[0] - ponto1[0])**2+(ponto2[1] - ponto1[1])**2)    
while running:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            running=False
        elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_ESCAPE:
            pygame.quit()
        elif evento.type==pygame.MOUSEBUTTONUP:
            posicao=pygame.mouse.get_pos()
            nome=simpledialog.askstring('Space','Nomeie o ponto selecionado:')
            if nome == None or nome == '':
                nome='desconhecido'+str(posicao)
            estrelas[nome] = posicao
            print(estrelas)
        elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_F12:
            estrelas={}
        


    tela.blit(fundo,(0,0))
    tela.blit(pressF10,(10,20))
    tela.blit(pressF11,(10,40))
    tela.blit(pressF12,(10,60))
    for nome,posicao in estrelas.items():
        posicaoestrela=(posicao[0]-estrela.get_width()//2,posicao[1]-estrela.get_height()//2)
        tela.blit(estrela,posicaoestrela)
        textoestrela=fonte.render(nome,True,branco)
        tela.blit(textoestrela,(posicao[0],posicao[1]+estrela.get_height()//2+5))
        if len(estrelas)>=2:
            pontos = list(estrelas.values())
            pygame.draw.lines(tela, branco, False, pontos, 1)
            for i in range(len(pontos) - 1):
                ponto_atual = pontos[i]
                proximo_ponto = pontos[i + 1]
                distancia = calcular_distancia(ponto_atual, proximo_ponto)
                texto_distancia = fonte.render(f"{distancia:.2f}", True, branco)
                posicao_texto_distancia = ((ponto_atual[0] + proximo_ponto[0]) // 2, (ponto_atual[1] + proximo_ponto[1]) // 2)
                tela.blit(texto_distancia, posicao_texto_distancia)

    pygame.display.update()
    clock.tick(60)
pygame.quit()