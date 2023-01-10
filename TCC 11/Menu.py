import  pymysql.cursors
import PySimpleGUI as sg
from tkinter import Button, Image
import buttons
from auth import getConnection 
#conexão com o banco#
Banco_de_Dados = getConnection()
cursor=Banco_de_Dados.cursor()
#conexão com o banco#

class Tela_Menu:

    def Layout(self):
        sg.theme('Reddit')
        layout = [
        #[sg.Text('',size=(8,10)), sg.Image(filename='fundo.png')],
        [sg.Text("Selecione a Categoria:")],
        #[sg.InputText(key="nome_cotacao")],
        #
        [sg.Button('', image_data=buttons.button_procuraremp_base64, key='Solicitacao', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
         sg.Button('', image_data=buttons.button_viabilidade_base64, key='Viabilidade', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), 
         sg.Button('', image_data=buttons.button_licenciamento_base64, key='Licenciamento', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
         sg.Button('', image_data=buttons.button_mobiliario_base64, key='Mobiliario', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
         sg.Button('', image_data=buttons.button_addregra_base64, key='regra', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        ]
        return sg.Window('IA', layout, finalize=True)
    
  