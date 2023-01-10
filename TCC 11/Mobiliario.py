import  pymysql.cursors
import PySimpleGUI as sg
from tkinter import Button, Image
import buttons
from auth import getConnection 
#conexão com o banco#
Banco_de_Dados = getConnection()
cursor=Banco_de_Dados.cursor()
#conexão com o banco#

class Tela_Mobiliario:

    def __init__(self):
        self.DADOS_Mobiliario=[]
        self.DADOS_Complementar=[]

    def Layout(self):
        sg.theme('Reddit')
        layout = [
        [sg.Text("Contribuinte",size=(77,0)), sg.Text("CPF/CNPJ") ],
        [sg.InputText( key = "Contribuinte",size=(10,2)), sg.Button('', image_data=buttons.button_x_base64, key='Pesquisa', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),sg.InputText( key = "contribuinte",size=(62,3)), sg.InputText( 'cpf',key = "cpf/cnj",size=(30,3)), sg.Button('', image_data=buttons.button_x_base64, key='Pesquisa', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        [sg.Text("RG/IE",size=(18,0)), sg.Text("Endereço",size=(76,0)), sg.Text("Numero")  ],
        [sg.InputText( key = "RG/IE",size=(20,2)), sg.InputText( key = "Endereco",size=(10,2)),sg.Button('', image_data=buttons.button_x_base64, key='Pesquisa', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),sg.InputText(key = "endereco",size=(60,3)), sg.InputText(key = "numero",size=(10,2)), sg.Button('', image_data=buttons.button_x_base64, key='Pesquisa', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        [sg.Text("Cod.mobiliario",(18,0)),sg.Text("Inscr. Municipal",(21,0)),sg.Text( "Inscr.Estadual",(22,0)),sg.Text("Nome Fantasia")],
        [sg.InputText( key = "cod.mob",size=(20,2)),sg.InputText( key = "Inscr.muni",size=(25,2)),sg.InputText( key = "Inscr.esta",size=(25,2)),sg.InputText( key = "nome.fantasia",size=(58,2))],
        [sg.Text("Atividade livre",(39,0)),sg.Text("Situação",(14,0)), sg.Text("Processo Alter",(39,0)),sg.Text("Risco CNAE"),],
        [sg.InputText( key = "Ativi.livre"), sg.Combo(["teste","teste1","teste2"],size=(14,1)),sg.InputText(key = "processo.alter"),sg.Combo(["teste","teste1","teste2"],size=(20,1))],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Button('', image_data=buttons.button_ir_base64, key='PS_Mobiliario', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        [sg.Table( self.DADOS_Mobiliario, ['  Inscrição Municipal  ','     Nome Fantasia      ','  Protocolo Abertura  ', '     CNPJ     ',], num_rows=10,enable_events=True, key= "Table_Mobiliario")]  
        ]
        return sg.Window('Mobiliario', layout, finalize=True)
    
    def Layout2(self):
                
        sg.theme('Reddit')
        layout = [  
            [sg.Text("Código", size=(18,1)), sg.Text('Tipo Cadastro',size=(32,1)), sg.Text('Tipo de Empresa ') ],
            [sg.Text(key="numero_codigo",size=(20,1)), sg.Text(size=(35,1), key="Tipo_cadastro"), sg.Text( size=(35,1), key="tipo_Empresa")],

            [sg.Text ("_________________________________________________________________________________________________________")],
            [sg.Text ('Nome Fantasia ', size=(62,1) ), sg.Text("Cadastro Imobiliario")],
            [sg.Text(size=(70,1), key="nome_fantasia"), sg.Text(size=(28,1), key="cadastro_imobiliario")],

            [sg.Text ("Escritorio/Contador", size=(50,1)), sg.Text("Fone", (12,1)), sg.Text("E-mail") ],
            [sg.Text(size=(10,1),key="escritorio_contador"),
            sg.Text(size=(39,1), key="Escritorio_contador_2"), sg.Text(size=(13,1), key="Fone"), sg.Text(size=(32,1), key="Email")],

            [sg.Text("Inscrição Est. ", size= (13,1)), sg.Text("Inscrição Est. ",size= (13,1)), sg.Text("Data Abertura",size= (13,1)),sg.Text("Processo Abert.",size= (13,1)), sg.Text("Dt.Cancel/Suspen",size= (13,1)),sg.Text("Proc. de Cancel",size= (13,1))],
            [sg.Text(size=(15,1),key="inscrição_est"),
            sg.Text(size=(15,1),key="inscrição_munic"),
            sg.Text(size=(15,1),key="data_abertura"),
            sg.Text(size=(15,1),key="Processo_Abert"),
            sg.Text(size=(15,1),key="Dt.Cancel/Suspen"), 
            sg.Text(size=(20,1),key="Proce_Cancel")   ],

            [sg.Text("Nº Junta C.", size= (13,1)), sg.Text("Data da Junta ", size= (10,1)), sg.Text("Nº Reg. P. J", size= (11,1)),
            sg.Text("Data Alteração", size= (11,1)), sg.Text("Processo de Alter", size= (13,1)), sg.Text("Pasta", size= (12,1))],
            [sg.Text(size=(15,1),key="Nº Junta C"), sg.Text(size=(12,1),key= "data_da_junta "), sg.Text(size=(12,1),key= "nº_reg"),
            sg.Text(size=(12,1),key= "data_alteracao"),sg.Text(size=(16,1),key= "processo_alter"), sg.Text(size=(29,1),key= "pasta")],

            [sg.Text("Logradouro", size= (71,1)), sg.Text("Numero", size= (9,1)), sg.Text("Lado", size= (13,1))],
            [sg.Text(size=(7,1), key= "cod"),
            sg.Text(size= (7,1), key="rua"), sg.Text(size= (10,1), key="rua2"), sg.Text(size= (45,1), key="endereco"), sg.Text(size= (10,1), key="numero"), sg.Text(size=(10,1))], 

            [sg.Text("Cep ", size= (16,1)), sg.Text("Complemento", size= (25,1)), sg.Text("Bairro", size= (12,1))],
            [sg.Text(size= (18,1), key="CEP"), sg.Text(size= (29,1), key="complemento"), sg.Text(size= (7,1), key="bairro"),
            sg.Text(size= (41,1), key="Bairro2")],

            [sg.Text("Distrito ", size= (46,1)),sg.Text("Fiscal Responsável", size= (16,1))     ],
            [sg.Text(size= (10,1), key="Distrito"),
            sg.Text(size= (35,1), key="complemento"),sg.Text(size= (10,1), key="fiscal_responsavel"),
            sg.Text(size= (35,1), key="Fiscal")],

            [sg.Text("", size=(89,1)), sg.Button("Confirmar", key="confirmar")]



        ]
        return sg.Window('Mobiliario_Conteudo1', layout, finalize=True)


    def Layout3(self):
        sg.theme('Reddit')
        layout = [  
        [sg.Text("Atiidades Livres", size=(18,1))],
        [sg.Output(size=(96,4), key="AtividadeLivre")],
        [sg.Text("Atiidades", size=(60,1)),sg.Text("Data inicio", size= (11,1)), sg.Text("Data fim", size= (11,1))],

        [sg.Input(size= (7,1), key="atividade"), sg.Input(size= (10,1), key="atividade2"),
        sg.Button('', image_data=buttons.button_x_base64, key='pesquisar_bairro', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
        sg.Input(size= (41,1), key="atividade"), sg.Input(size= (12,1), key="dt_inicio"),sg.Input(size= (12,1), key="dt_fim ")],
        [sg.Table( DADOS_Atividade, ['Cod.','Codigo ', 'Codigo de Lei','Descrição da Atividade ','Cod.','    Desdobro      ','QTDE ', 'Situação'], num_rows=10,enable_events=True, key= "Table_atividade"), ],
        [sg.Table( DADOS_Complementar, ['Exercico .','Receita ', 'Limite ini. ','Limite Fin. ','Valor ','Tipo do Cálculo','tivo do Valor', 'Região'], num_rows=10,enable_events=True, key= "Table_atividade")],
        [sg.Button("Confirmar", key="confirmar"), sg.Button("cancelar", key="cancelar")]

        ]
        return sg.Window('Cadastro', layout, finalize=True)

    def Layout4(self):
        sg.theme('Reddit')
        layout = [  
        [sg.Text("Exigibilidade do ISS", size=(37,1)),sg.Text("Processos ", size=(11,1)), sg.Text("Dt Exigibilidade", size=(18,1) )],
        [sg.Combo("Não Exigivel ", " Exigivel", size=(40,1), key="exigivel"),sg.Input(size=(13,1),key="processos"), sg.Input(size=(13,1),key="Dt_Exigibilidade")],
        [sg.Text("Regime Especial ", size=(50,1)), sg.Text("Dt inicio", size=(18,1) )],
        [sg.Combo("Possui", "Não Possui", size=(55,1), key="exigivel"), sg.Input(size=(13,1),key="DT_Inicio_Regime")],
        [sg.Text("Tipo ISSQN ", size=(50,1)), sg.Text("Dt inicio", size=(18,1) )],
        [sg.Combo("teste", 'Teste', size=(55,1), key="exigivel"), sg.Input(size=(13,1),key="Dt_ISSQN")]


        ]
        return sg.Window('Cadastro', layout, finalize=True)    
        
    def PS_Mobiliario(self,window, event, values):
        try:
            dados=''
        except:
            dados=''

        if dados != '':
            pass
        else:

            exibe = f"""
            select MB_inscricao_Municipal ,RazaoSocial,ProtocoloOrgao,CNPJ 
            from Solicitacao where Finalizado =1
            """

        cursor.execute(exibe)
        resultado = cursor.fetchall()
        
                
        self.DADOS_Mobiliario=[]
        for c in resultado :

            self.DADOS_Mobiliario.append([c['MB_inscricao_Municipal'], c['RazaoSocial'], c['ProtocoloOrgao'], c['CNPJ']])
            window.FindElement("Table_Mobiliario").update(self.DADOS_Mobiliario)
