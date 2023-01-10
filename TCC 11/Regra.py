import  pymysql.cursors
import PySimpleGUI as sg
from tkinter import Button, Image
import buttons
from auth import getConnection2
#conexão com o banco#
Banco_de_Dados = getConnection2()
cursor=Banco_de_Dados.cursor()
#conexão com o banco#

class Tela_Regra:

    def __init__(self):
        self.DADOS_Regras=[]


    def Layout(self):
        sg.theme('Reddit')
        layout = [
        [sg.Text("Numero:                           "),sg.Text("Ordem:     "),],
        [sg.InputText(key="rg_numero",size=(20,2)),sg.InputText(key="rg_ordem",size=(10,2))],
        [sg.Text("Dado:                           "),sg.Text("Condição:     "),sg.Text("Resultado:                    "),sg.Text("Conclusão:")],
        [sg.InputText(key="rg_dado",size=(20,2)),sg.Spin(["==","!=",">","<"], key="rg_condicao",size=(10,2)), sg.InputText(key="rg_resultado",size=(20,2)),sg.InputText(key="rg_conclusao",size=(20,2))],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), 
        sg.Button('', image_data=buttons.button_x_base64, key='PS_Regras', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
        sg.Button('', image_data=buttons.button_confirmar_base64, key='Adicionar_Regra', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        [sg.Table( self.DADOS_Regras, ['Numero','Ordem ', '  Dado  ','Condição','Resultado','  Conclusão  '], num_rows=30,enable_events=True, key= 'excluir_Regra')]
        ]
        return sg.Window('Regras', layout, finalize=True)


    def Layout2(self):
        sg.theme('Reddit')
        layout = [
        [sg.Text("Deseja excluir está regra?")],
        [sg.Button('Sim', key='Exclusao'),
        sg.Button('Não', key='Voltar')]]
        return sg.Window('Excluir Regra', layout, finalize=True)
        
    def PS_Regras(self,window,event,values):

        cursor = Banco_de_Dados.cursor()
        cursor.execute('SELECT * FROM condicoes')
        resultado = cursor.fetchall()
        
        
        self.DADOS_Regras=[]
        for c in resultado :
            self.DADOS_Regras.append([c[1], c[2], c[3], c[4], c[5], c[6]])
            window.FindElement('excluir_Regra').update(self.DADOS_Regras)
        Banco_de_Dados.commit()

    def Adicionar_Regra(self,values):
        cursor = Banco_de_Dados.cursor()

        cursor.execute(f"INSERT INTO `teste`.`condicoes`(`numeroRegra`,`ordem`,`variavelA`,`condicao`,`variavelB`,`conclusao`)VALUES('{values['rg_numero']}','{values['rg_ordem']}','{values['rg_dado']}','{values['rg_condicao']}','{values['rg_resultado']}','{values['rg_conclusao']}');")
        Banco_de_Dados.commit()

    def exclusao(self, rows):
        cursor = Banco_de_Dados.cursor()
        cursor.execute("SET sql_safe_updates=0")
        cursor.execute("DELETE FROM condicoes WHERE numeroRegra = {} and ordem = {}".format(self.DADOS_Regras[rows][0], self.DADOS_Regras[rows][1]))
        Banco_de_Dados.commit()
        pass
 