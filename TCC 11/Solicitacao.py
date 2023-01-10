import  pymysql.cursors
import PySimpleGUI as sg
from tkinter import Button, Image
import buttons
from Viabilidade import Viabilidade
from Licenciamento import Licenciamento
from Inferencia import Inferencia
from auth import getConnection2,getConnection
#conexão com o banco#
Banco_de_Dados = getConnection2()
cursor=Banco_de_Dados.cursor()
#conexão com o banco#

class Tela_Solicitacao:
    def __init__(self):
        self.DADOS_Solicitacao=[]
        self.Viabilidade = Viabilidade()
        self.Licenciamento = Licenciamento()
        self.Inferencia = Inferencia()
        self.IdSolicitacao= None
        self.CNPJ=None
    def Layout(self):

        sg.theme('Reddit')
        layout = [
        [sg.Text("Digite seu Protocolo:")],
        [sg.InputText(key="vb_dados") ],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), 
        sg.Button('', image_data=buttons.button_x_base64, key='PS_Solicitacao', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
        sg.Button("Limpar", key= "Limpar Solicitação")],
        [sg.Table( self.DADOS_Solicitacao, ['Protocolo','Situação ', '   CNPJ   ',], num_rows=10,enable_events=True, key= "Table_Solicitacao")]            
        ]
        return sg.Window('Procurar Empresa ', layout, finalize=True)
    
    def Layout_Inferencia(self):
        sg.theme('Reddit')
        layout = [
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), 
        sg.Button("Analise Vibilidade", key= "Analisar Vibilidade"),
        sg.Button("Analise Licenciamento", key= "Analisar Licenciamento"),
        sg.Button("Analise Inferencia", key= "Analisar Inferencia")],     
        ]
        return sg.Window('Inferencia', layout, finalize=True)

    def Layout_Documento(self):
        sg.theme('Reddit')
        layout = [
        [sg.Text("Digite numero do Protocolo:")],
        [sg.InputText(key="numero_protocolo") ],
        [sg.Text("Digite data do Protocolo:")],
        [sg.InputText(key="data_protocolo") ],
        [sg.Spin(["Deferida","Indeferida"], key="dc_status", )],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), 
        sg.Button("Enviar", key= "Envio Documento")],     
        ]
        
        return sg.Window('Documento', layout, finalize=True)

    def Layout__Envio_documento(self):
        sg.theme('Reddit')
        layout = [
        [sg.Text("Digite Numero da Licença:")],
        [sg.InputText(key="numero_licenca") ],
        [sg.Text("Digite data da Liberação:")],
        [sg.InputText(key="data_liberacao") ],
        [sg.Text("Digite data do Vencimento:")],
        [sg.InputText(key="data_vencimento") ],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), 
        sg.Button("Enviar", key= "Envio Documento Deferida")],        
        ]
        return sg.Window('Envio Documento', layout, finalize=True)
        
    def PS_Solicitacao(self,window,event,values):
        
        self.DADOS_Solicitacao=[]
        dados= values['vb_dados']
        cursor = Banco_de_Dados.cursor()
        Banco_de_Dados.commit()
        if dados != '':
            exibe = f"""
            select IdSolicitacao ,situacaoSolicitacao ,CNPJ 
            from solicitacao 
            where IdSolicitacao  = '{dados}'  or  Cnpj= '{dados}' and situacaoSolicitacao != 'Indeferida';"""
        else:
            exibe = f"""
            select IdSolicitacao ,situacaoSolicitacao ,CNPJ 
            from solicitacao where  situacaoSolicitacao != 'Indeferida';"""

        cursor.execute(exibe)
        resultado = cursor.fetchall()
        

        for c in resultado :
            self.DADOS_Solicitacao.append([c[0], c[1], c[2]])
            self.CNPJ=c[2]
            window.FindElement("Table_Solicitacao").update(self.DADOS_Solicitacao)
        Banco_de_Dados.commit()

    def Limpar_Solicitacao(self,window,event,values):
        window.FindElement('vb_dados').Update('')
        window.FindElement('Table_Solicitacao').Update('')


    def Analisar_Vibilidade(self,window,event,values,row):

        cursor = Banco_de_Dados.cursor()
        cursor.execute(f"""select * from viabilidade where Protocolo  = '{self.DADOS_Solicitacao[row][0]}';""")
        result = cursor.fetchall()

        if  len(result) == 0:
            self.Viabilidade.Solicitacao(self.DADOS_Solicitacao[row][0])
            sg.popup(self.Viabilidade.Resposta())
        else:
            sg.popup('Viabilidade já analisada')

        Banco_de_Dados.commit()
       
    def Analisar_Licenciamento(self,window,event,values,row):
        cursor = Banco_de_Dados.cursor()
        cursor.execute(f"""select ProtocoloOrgao from solicitacao where IdSolicitacao = {self.DADOS_Solicitacao[row][0]}""")
        protocolo=cursor.fetchone()
        cursor.execute(f"""select * from viabilidade where Protocolo  = '{protocolo[0]}';""")
        result = cursor.fetchall()
        if  len(result) != 0:
            Banco_de_Dados.commit()
            cursor.execute(f"""select * from licenciamento where Protocolo  = '{protocolo[0]}';""")
            result = cursor.fetchall()

            if  len(result) == 0:
                
                self.Licenciamento.Solicitacao(self.DADOS_Solicitacao[row][0],protocolo[0])
                return True
            else:
                sg.popup('Licenciamento já Analisado')
                return False
        else:
            sg.popup('Viabilidade ainda não analisada')
        Banco_de_Dados.commit()

    def Envio_Documento(self,window,event,values,row):
        if values['data_protocolo'] != '' or values['numero_protocolo'] != '':
            if values['dc_status'] =='Deferida':
                
                self.Licenciamento.data_protocolo=values['data_protocolo']
                self.Licenciamento.numero_protocolo=values['numero_protocolo']
                self.Licenciamento.dc_status=values['dc_status']             
                self.Licenciamento.risco='Alto'     
                return 'Deferida'

            else:
                self.Licenciamento.risco='Alto'
                self.Licenciamento.dc_status=values['dc_status'] 
                self.Licenciamento.InserirBanco_de_Dados()
                sg.popup('Liceniamento Indeferido') 
                Banco_de_Dados.commit()
        else:
            sg.popup('Favor Preencher as informações') 

    def Envio_Documento_Deferida(self,window,event,values,row):
        if values['data_vencimento'] != '' or values['data_liberacao'] != '' or values['numero_licenca'] != '':
            self.Licenciamento.data_vencimento=values['data_vencimento'] 
            self.Licenciamento.data_liberacao=values['data_liberacao'] 
            self.Licenciamento.numero_licenca=values['numero_licenca']
            self.Licenciamento.Atividade_Servico()
            sg.popup('Licenciamento concluido')
        else:
            sg.popup('Favor Preencher as informações') 

    def Envio_Baixo_Risco(self,window,event,values,row):
        self.Licenciamento.Atividade_Servico()


    def Analisar_Inferencia(self,window,event,values,row):
        Banco_de_Dados.commit()
        cursor.execute(f"""select ProtocoloOrgao from solicitacao where IdSolicitacao = {self.DADOS_Solicitacao[row][0]}""")
        protocolo=cursor.fetchone()
        cursor.execute(f"""select * from licenciamento where Protocolo  = '{protocolo[0]}';""")
        result = cursor.fetchall()
        self.IdSolicitacao=self.DADOS_Solicitacao[row][0]
        if  len(result) == 0:
            sg.popup('Licenciamento não Analisado')
            return True
        else:
            self.Inferencia.Iniciar_Inferencias(self.DADOS_Solicitacao[row][0])
            return False

    def Exportar_Dados(self):

        cursor.execute(f"update solicitacao set Finalizado = '0' where CNPJ = '{self.CNPJ}'")
        print(self.IdSolicitacao)
        Banco_de_Dados.commit()
        cursor.execute(f"update solicitacao set Finalizado = '1' where IdSolicitacao = '{self.IdSolicitacao}'")
        Banco_de_Dados.commit()
