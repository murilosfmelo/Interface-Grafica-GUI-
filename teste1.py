# Introdução à GUI

import PySimpleGUI as psg

# Desenho da Interface

layout = [
    [psg.Text("Olá, Seja Bem-vindo"),psg.Text("******")],
    [psg.Button("------ Clique aqui --------")],
    [psg.Text("Primeiro Programa de Telinha"),psg.Text("******")]]


#Definir o frame

window = psg.Window("Minha Primeira Tela em Python", layout)


#Imprimir a janela na tela

while True:
    evento, valor = window.read()

    if evento == psg.WIN_CLOSED:
        break
    else:
        psg.popup("Programação Python \n botão clicado", title="Senai")
window.close()

