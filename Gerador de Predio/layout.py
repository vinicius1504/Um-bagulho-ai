import xml.etree.ElementTree as ET
import random
import requests
import PySimpleGUI
import PySimpleGUI as sg
import os
import index



layout = [
    [sg.Text('coordenada X:')],
    [sg.Input(key='coordX', size=(10,1))],
    [sg.Text('coordenada Y:')],
    [sg.Input(key='coordY', size=(10,1))], 
    [sg.Text('quantidade de UCs:')],
    [sg.Input(key='quantidade', size=(10,1))],
    [sg.Button('Gerar arquivo'), sg.Button('Sair', button_color=('red'))]
]

window = sg.Window('Gerador de arquivos XML', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Gerar arquivo':
        x = values['coordX']
        y = values['coordY']
        quantidade = values['quantidade']
        index.generate_xml_file(index.x, index.y, index.quantidade)
        
window.close()