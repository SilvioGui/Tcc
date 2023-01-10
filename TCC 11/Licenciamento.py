import  pymysql.cursors
import PySimpleGUI as sg
from tkinter import Button, Image
import buttons
from auth import getConnection 
#conexão com o banco#
Banco_de_Dados = getConnection()
cursor=Banco_de_Dados.cursor()
#conexão com o banco#

class Tela_Licenciamento:

    def __init__(self):
        self.DADOS_Licenciamento=[]

    def Layout(self):
        sg.theme('Reddit')
        layout = [

        [sg.Text("Digite seu CNPJ ou Protocolo")],
        [sg.InputText(do_not_clear=False, key = "dados_licenciamento"), 
         sg.Button('', image_data=buttons.button_x_base64, key='PS_Licenciamento', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
        sg.Button ("limpar", key= "Limpar Licenciamento")],
        [sg.Table(self.DADOS_Licenciamento, ['Id Licenciamento',' Protocolo ',' Situação ', '     CNPJ     '], num_rows=10,enable_events=True,  key= "Table_Licenciamento")]
        ]
        return sg.Window('Consulta Licenciamento', layout, finalize=True)

    def janela_Dados_completos_licenciamento(self):
        sg.theme('Reddit')
        layout = [
        [sg.Text("Solicitar Licenciamento", font=('', 16, 'bold'),justification='c', expand_x=True)],
        [sg.Text("")],
        [sg.Button('', image_data=buttons.button_museup_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Text("Informações", font=('', 12, 'bold'))],
        [sg.Text("Confira a classificação de risco e acompanhe o andamento da solicitação", text_color= 'gray', font=('', 11, 'bold'))],
        [sg.Text("")],
        [sg.Button('', image_data=buttons.button_museup_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Text("Solicitação", font=('', 12, 'bold'))],
        [sg.Text("Protocolo:", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
         sg.Text("Data da Solicitação", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
         sg.Text("Status Solicitação", text_color= 'gray', font=('', 11, 'bold')),
        ],
        [sg.Text(key="ProtocoloLicenca", size=(28,0)), 
         sg.Text(key="DataSolicitacaoLicenciamento", size=(28,0)),  
         sg.Text(key="SituacaoLicenca"),    
        ],
        [sg.Text("", size=(5))],
        [sg.Button('', image_data=buttons.button_museup_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Text("Atividades Auxiliares", font=('', 12, 'bold'))],
        #A linha abaixa (sg.table), tem que puxar do banco de dados, foi apenas um exemplo feito
        [sg.Table([['Garagem','Sim']], ['Descrição','Selecionada para Licenciamento',],num_rows=2)],        
        [sg.Text("")],
        [sg.Text("")],
        [sg.Button('', image_data=buttons.button_museup_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Text("Solicitante", font=('', 12, 'bold'))],
        [sg.Text("Nome", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
         sg.Text("CPF", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
         sg.Text("Email", text_color= 'gray', font=('', 11, 'bold')),
        ],
        [sg.Text("Bruno Wagner",key="", size=(28,0)), 
         sg.Text("12321312",key="", size=(28,0)),  
         sg.Text("jasiujdas@hotmail.com",key=""),    
        ],
        ##
        [sg.Text("")],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Button('', image_data=buttons.button_ir_base64, key='PG_Licenciamento', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        ]
        return sg.Window('Solicitar Licenciamento - Página 1/2',layout, finalize=True)

    def janela_Dados_completos_licenciamento2(self):

        sg.theme('Reddit')
        layout = [
            [sg.Text("Solicitar Licenciamento", font=('', 16, 'bold'),justification='c', expand_x=True)],        
            [sg.Text("")],
            [sg.Button('', image_data=buttons.button_museup_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Text("Secretaria de Estado da Segurança Pública / Corpo de Bombeiros", font=('', 12, 'bold'))],
            [sg.Text("Emissão", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
            sg.Text("Número da Licenca", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
            sg.Text("Validade", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
            sg.Text("Prazo", text_color= 'gray', font=('', 11, 'bold')),
            ],
            [sg.Text(key="DataEmissaoLicenca", size=(28,0)), 
            sg.Text(key="idLicenca", size=(28,0)),  
            sg.Text(key="DataValidadeLicenca", size=(28,0)),
            sg.Text(key="")    
            ],
            [sg.Text("Situação", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
            sg.Text("Número da Solicitação", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
            sg.Text("Risco Classificado", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
            sg.Text("CNAE", text_color= 'gray', font=('', 11, 'bold')),
            ],
            [sg.Text("")],
            [sg.Text(key="situacaoSolicitacao", size=(28,0)), 
            sg.Text(key="IdSolicitacao", size=(28,0)),  
            sg.Text(key="Risco", size=(28,0)),
            sg.Text(key="Cnae")    
            ],
            [sg.Text("Foram prestadas as seguintes declarações:", justification = 'c',font=('', 10 ,'bold'))],
            [sg.Text(key="")],
            [sg.Text("As seguintes restrições devem ser observadas:", font=('', 10 ,'bold'))],
            [sg.Text(key="")],
            [sg.Text("Irregularizações", font=('', 10 ,'bold'))],
            [sg.Text(key="")],
            [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)]
        ]

        return sg.Window('Solicitar Licenciamento - Página 2/2',layout, finalize=True)


    def Limpar_Licenciamento(self,window,event,values):        
        window.FindElement('dados_licenciamento').Update('')
        window.FindElement('Table_Licenciamento').Update('')

    def Table_Licenciamento(self,window,event,values,Licenciamento_Conteudo,row):
        print('table_Licenciamento')
        Banco_de_Dados2 = getConnection()
        cursor2=Banco_de_Dados2.cursor()
        cursor2.execute(f"""select * from licenciamento where Protocolo  = '{self.DADOS_Licenciamento[row[0]][1]}';""")
        licenciamento=cursor2.fetchone()

        Licenciamento_Conteudo.find_element('ProtocoloLicenca').Update(licenciamento['Protocolo']) 

    def PS_Licenciamento(self,window, event, values):
        try:
            dados= values['vb_dados']
            orgao = values['vb_orgao']
        except:
            dados=''

        if dados != '':
            exibe = f"""
            select idlicenciamento,Protocolo,SituacaoLicenca,Cnpj 
            from licenciamento 
            where IdSolicitacao  = '{dados}' or  Cnpj= '{dados}';"""
        else:
            exibe = f"""
            select idlicenciamento,Protocolo,SituacaoLicenca,Cnpj 
            from licenciamento 
            """

        cursor.execute(exibe)
        resultado = cursor.fetchall()
        
        
        self.DADOS_Licenciamento=[]
        for c in resultado :

            self.DADOS_Licenciamento.append([c['idlicenciamento'], c['Protocolo'], c['SituacaoLicenca'], c['Cnpj']])
            window.FindElement("Table_Licenciamento").update(self.DADOS_Licenciamento)







class Licenciamento:

    def __init__(self):
        self.msg=''
        self.numero_protocolo=''
        self.data_protocolo=''
        self.dc_status=''
        self.data_liberacao=''
        self.data_vencimento=''
        self.numero_licenca=''
        self.risco='Baixo'
        self.protocolo_solicitação=''
        print("inicializou")
        self.Banco_de_Dados = getConnection()
        self.cursor=self.Banco_de_Dados.cursor()

#! =>   SOLICITAÇÃO
    def Solicitacao(self,idSolicitacao,protocolo):
        self.idSolicitacao=idSolicitacao
        self.protocolo_solicitação=protocolo
        if self.cursor.execute(f"select Cnae from solicitacao where situacaoSolicitacao = 'Deferida' and IdSolicitacao='{idSolicitacao}'") :
            self.Cnae=self.cursor.fetchall()
            self.Consulta_risco()
        else:
            self.msg='solcitação não encontrada'
            self.Resposta()


#@ =>   CONSULTAR RISCO
    def Consulta_risco(self):

        for cnae in self.Cnae[0]['Cnae'].split(','):
            cnae2= cnae.replace('-','').replace('/','')
            if self.cursor.execute("select * from cnae where cnae ='{}'".format(cnae2)):
                self.cnae=self.cursor.fetchall()
                print('risco: ',self.cnae[0]['risco'])
                if self.cnae[0]['risco'] != 'Baixo Risco':
                    
                    self.msg='Alto Risco'   
                    self.Resposta()
                else:
                    self.Atividade_Servico()
                    
            else:
                self.msg='cnae não encontrado'
                self.Resposta()
        self.InserirBanco_de_Dados()

#* =>   ATIVIDADE
    def Atividade_Servico(self):
        string_atividade=''
        for cnae in self.Cnae[0]['Cnae'].split(','):
            cnae.replace('-','').replace('/','')
            if self.cursor.execute("select cod_servico from cnae where cnae ='{}'".format(cnae)):
                try:
                    cod_atividades=self.cursor.fetchall()[0]['cod_servico'].split(',')
                    for cod_atividade in cod_atividades:
                        if string_atividade == '':
                            string_atividade =cod_atividade
                        else:
                            string_atividade =string_atividade +','+cod_atividade
                except:
                    pass

        self.cursor.execute(f"update solicitacao set cod_atividade ='{string_atividade}' where IdSolicitacao='{self.idSolicitacao}'")
        

#& =>   SALVAR ANALISE
    def InserirBanco_de_Dados(self):
        self.cursor.execute(f"select * from viabilidade where protocolo='{self.protocolo_solicitação}'")
        INSCRICAO=self.cursor.fetchone()

        self.cursor.execute(f"insert into licenciamento values ({self.idSolicitacao},'{INSCRICAO['Protocolo']}','{self.dc_status}','{INSCRICAO['CNPJ']}','{INSCRICAO['EmpresaEstabelecida']}','{INSCRICAO['Cnae']}','{self.data_liberacao}','{self.data_vencimento}','{INSCRICAO['Orgao']}','{self.numero_protocolo}','{self.data_protocolo}','{self.numero_licenca}','sem detalhe de licença','Novo Horizonte','{self.risco}','{INSCRICAO['RazaoSocial']}','{INSCRICAO['TipoLogradouro']}','{INSCRICAO['Logradouro']}','{INSCRICAO['Numero']}','{INSCRICAO['Bairro']}','{INSCRICAO['Municipio']}','{INSCRICAO['Complementos']}','{INSCRICAO['Cep']}','{INSCRICAO['TipoInscricaoImovel']}','{INSCRICAO['NumeroInscricaoImovel']}');" )

        self.Resposta()

#? =>    
    def Resposta(self):      
        self.Banco_de_Dados.commit()
        return(self.msg)





