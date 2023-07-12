import pygame
from tkinter import simpledialog
import math
import json
import sys
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
mensagemexibida=False
mensagemtempoinicial=0
mensagemduracao=3000
def salvarpontos():
    with open('db.txt', 'w') as database:
        json.dump(estrelas, database)
def calculardistancia(ponto1, ponto2): 
    return math.sqrt((ponto2[0] - ponto1[0])**2+(ponto2[1] - ponto1[1])**2)
estrelas={}
while running:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT or evento.type==pygame.KEYDOWN and evento.key==pygame.K_ESCAPE:
            salvarpontos()
            running=False
        elif evento.type==pygame.MOUSEBUTTONUP:
            posicao=pygame.mouse.get_pos()
            nome=simpledialog.askstring('Space','Nomeie o ponto selecionado:')
            if nome == None or nome == '':
                nome='desconhecido'+str(posicao)
            elif nome in estrelas:
                mensagem=fonte.render(f'Já existe um ponto cadastrado com esse nome: {nome}', True, branco)
                mensagemexibida=True
                continue
            estrelas[nome]=posicao
        elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_F12:
            estrelas={}
        elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_F11:
            try:
                with open('db.txt') as database:
                    estrelas=json.load(database)
                if not estrelas:
                    mensagem=fonte.render(f'Não há pontos salvos para carregar', True, branco)
                    mensagemexibida=True
                    continue
            except FileNotFoundError:
                mensagem=fonte.render(f'Não há pontos salvos para carregar', True, branco)
                mensagemexibida=True
                continue
            except json.decoder.JSONDecodeError:
                mensagem=fonte.render(f'Erro ao carregar os pontos', True, branco)
                mensagemexibida=True
                continue
        elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_F10:
            try:
                with open('db.txt','w') as database:
                    json.dump(estrelas,database)
                    mensagem=fonte.render(f'Pontos salvos', True, branco)
                    mensagemexibida=True
                    continue
            except:
                mensagem=fonte.render(f'Erro ao criar base de dados', True, branco)
                mensagemexibida=True
                continue
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
                pontoatual=pontos[i]
                proximoponto=pontos[i + 1]
                distancia=calculardistancia(pontoatual, proximoponto)
                distanciax=abs(proximoponto[0]-pontoatual[0])
                distanciay=abs(proximoponto[1] - pontoatual[1])
                textodistanciay=fonte.render(f"y: {distanciay:.2f}", True, branco)
                textodistancia=fonte.render(f"x: {distanciax:.2f}", True, branco)
                posicaotextodistancia=((pontoatual[0] + proximoponto[0]) // 2 - 40, (pontoatual[1] + proximoponto[1]) // 2 - 20)
                tela.blit(textodistancia,(posicaotextodistancia[0],posicaotextodistancia[1]-40))
                tela.blit(textodistanciay,(posicaotextodistancia[0],posicaotextodistancia[1]-20))
    if mensagemexibida:
        mensagemlargura=mensagem.get_width()
        mensagemaltura=mensagem.get_height()
        mensagemposicao=(tamanho[0] // 2 - mensagemlargura // 2, tamanho[1] // 2 - mensagemaltura // 2)
        mensagemtempoinicial=pygame.time.get_ticks()
        tela.blit(mensagem, mensagemposicao)
        if pygame.time.get_ticks()-mensagemtempoinicial>mensagemduracao:
            mensagemexibida=False
    pygame.display.update()
    clock.tick(60)
pygame.quit()