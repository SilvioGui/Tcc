import  pymysql.cursors
import PySimpleGUI as sg
from datetime import datetime
from tkinter import Button, Image
import buttons

from auth import getConnection 
#conexão com o banco#
Banco_de_Dados = getConnection()
cursor=Banco_de_Dados.cursor()
#conexão com o banco#

class Tela_Viabilidade:

    def __init__(self):
        self.DADOS_Viabilidade=[]

    def Layout(self):
        sg.theme('Reddit')
        
        layout = [
        [sg.Text("Digite seu Protocolo ou CNPJ :",sg.theme_background_color=='red')],
        [sg.InputText(key="vb_dados") ],
        [sg.Text("Selecione um Orgão")],
        [sg.Spin(["São Paulo"], key="vb_orgao", )],
        [sg.Text("Periodo")],
        [sg.Text("Início"),sg.InputText(key="Data inicio", size=(20,1), ), 
        sg.Button('', image_data=buttons.button_calender_base64, key='Data Inicio', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Text("Final"), sg.InputText(key="Data fim", size=(20,1)), 
        sg.Button('', image_data=buttons.button_calender_base64, key='Data Fim', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), 
        sg.Button('', image_data=buttons.button_x_base64, key='PS_Viabilidade', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
        sg.Button("Limpar", key= "Limpar Viabilidade")],
        [sg.Table( self.DADOS_Viabilidade, ['Protocolo','Situação ','Dt Solicitação', '     CNPJ     ',], num_rows=10,enable_events=True, key= "Table_Viabilidade")]  
        ]
    
        return sg.Window('Consulta de Protocolo de Viabilidade', layout, finalize=True)
    
    def Loyout_Dados_Viabilidade(self):
        sg.theme('Reddit')
        layout = [
        [sg.Text("Dados do Protocolo", font=('', 12, 'bold'))],
        [sg.Text("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")],
        [sg.Text("ID da Solicitação:", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)), 
         sg.Text("Protocolo:", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
         sg.Text("Data do Protocolo:", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
         sg.Text("Análise:", text_color= 'gray', font=('', 11, 'bold')),
        ],
        [sg.Text(key="ID_Solicitacao_viabilidade", size=(28,0)), 
         sg.Text(key="Protocolo",size=(28,0)),  
         sg.Text(key="Data_do_Protocolo",size=(28,0)),
         sg.Text(key="Analise")
        ],
        [sg.Text("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")],
        [sg.Text("Informações sobre o Estabelecimento", size=(0,0),font=('', 12, 'bold'))],
        [sg.Text("Razão Social", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
         sg.Text("CNPJ:", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
         sg.Text("Nire:", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
         sg.Text("Orgão", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
         sg.Text("Empresa Estabelecida", text_color= 'gray', font=('', 11, 'bold'), size=(25,0)),
        ], 
        [sg.Text(key="Razão_Social", size=(28,0)), 
         sg.Text(key="CNPJ", size=(28,0)),
         sg.Text(key="Nire", size=(28,0)),
         sg.Text(key="Orgao", size=(28,0)),
         sg.Text(key="Empresa_Estabelecida", size=(28,0)),
         
        ],
        [sg.Text("")],
        [sg.Text("Eventos", font=('', 12, 'bold'))],
        [sg.Text(key="Evento", size=(25,0))],
        [sg.Text("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")],
        [sg.Text("Endereço do Domiciliar",font=('', 12, 'bold'))],
        [sg.Text("Endereço indicado",text_color= 'gray',font=('', 11, 'bold'))],
        [sg.Text(key="Logradouro"), sg.Text(","),
         sg.Text(key="Numero"), sg.Text(","),
         sg.Text(key="Bairro"), sg.Text(","),
         sg.Text(key="Cidade"), sg.Text(","),
         sg.Text(key="CEP"), sg.Text(","),
         sg.Text(key="Tipo_do_Logradouro"),
        ],
        [sg.Text("")],
        [sg.Text("Complemento:",text_color= 'gray',font=('', 11, 'bold'))],
        [sg.Text(key="Complemento")], 
        [sg.Text("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Button('', image_data=buttons.button_ir_base64, key='Table_Viabilidade2', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)]
        ]

        return sg.Window('Dados completos viabilidade',layout, finalize=True)
    def Loyout_Dados_Viabilidade2(self):
        sg.theme('Reddit')
        layout = [
        [sg.Text("Atividades Econômicas",font=('', 12, 'bold'))],
        #[sg.Table(DADOS_Cnae, ['CNAE','Atividade Estabelecida no Local','Situação'], num_rows=10, key= "Table_CNAE")]
        [sg.Text("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")],
        [sg.Text("Atividades Auxiliares",font=('Arial', 12, 'bold'))],
        [sg.Text(key="Atividade Auxiliar",text_color= 'gray', font=('', 11, 'bold'))],
         #[sg.Table(DADOS_AtivAux, ['1','2 '3','4'], num_rows=10, key= "")]
        [sg.Text("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")],
        [sg.Text("Dados de Inscrição do Imóvel",font=('Arial', 12, 'bold'))],
        [sg.Text("Inscrições",text_color= 'gray', font=('', 11, 'bold'))],
        [sg.Text(key="Inscricao_do_Imovel",size=(28,0)), sg.Text("")], 
        [sg.Text("")],
        [sg.Text("Tipo de Unidade", font=('Arial', 12, 'bold'))],
        [sg.Text("Descrição:",text_color= 'gray', font=('', 11, 'bold'))],
        [sg.Text(key="Tipo_de_Unidade",size=(28,0))],
        [sg.Text("")],
        [sg.Text("Forma de Atuação", font=('Arial', 12, 'bold'))],
        [sg.Text("Descrição:",text_color= 'gray', font=('', 11, 'bold'))],
        [sg.Text(key="Forma_Atuacao",size=(28,0))],
        [sg.Text("Área Imóvel",size=(28,0), font=('Arial', 12, 'bold')),
         sg.Text("Tipo de Inscrição",size=(28,0), font=('Arial', 12, 'bold')),
         sg.Text("Área Estabelecimento", font=('Arial', 12, 'bold'))
        ],
        [sg.Text("Descrição:",size=(31,0), text_color= 'gray', font=('', 11, 'bold')),
         sg.Text("Descrição:",size=(31,0), text_color= 'gray', font=('', 11, 'bold')),
         sg.Text("Descrição:", text_color= 'gray', font=('', 11, 'bold')),
        ],
        [sg.Text(key="Area_Imovel",size=(35,0)),
         sg.Text(key="Tipo_de_Inscrição",size=(35,0)),
         sg.Text(key="Area_Estabelecimento"),
        ],
        [sg.Text("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")],
        #[sg.Text("CPF Servidor:"), 
        # sg.InputText(key="CPF_Servidor",size=(25,2))],   
        #[sg.Text("Resultado da Análise:"), 
        # sg.InputText(key="Resultado_da_Analise:",size=(25,2)), 
        # sg.Text("Resultado da Viabilidade:"), 
        # sg.InputText(key="Resultado_da_Viabilidade",size=(25,2))],
        #[sg.Text("")],
        #[sg.Text("Tempo de Andamento"), sg.InputText(key="Tempo_de_Andamento",size=(25,2))],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)]
        ]

        return sg.Window('Dados completos viabilidade 2',layout, finalize=True)

    def Limpar_Viabilidade(self,window, event, values):
        window.FindElement('vb_dados').Update('')
        window.FindElement('Data inicio').Update('')
        window.FindElement('Data fim').Update('')
        window.FindElement('Table_Viabilidade').Update('')
        
    def PS_Viabilidade(self,window, event, values):
        try:
            dados= values['vb_dados']
            orgao = values['vb_orgao']
            dataInicio = values['Data inicio']
            dataFim = values['Data fim']
        except:
            dados=''

        if dados != '':
            exibe = f"""
            select IdSolicitacao ,Analise,DataProtocolo,CNPJ 
            from viabilidade 
            where IdSolicitacao  = '{dados}' or  Cnpj= '{dados}'
            or Orgao = '{orgao}' 
            or DataProtocolo >= '{dataInicio}' AND DataProtocolo <=  '{dataFim}';"""
        else:
            exibe = f"""
            select IdSolicitacao ,Analise,DataProtocolo,CNPJ 
            from viabilidade 
            """

        cursor.execute(exibe)
        resultado = cursor.fetchall()
        
        
        self.DADOS_Viabilidade=[]
        for c in resultado :

            self.DADOS_Viabilidade.append([c['IdSolicitacao'], c['Analise'], c['DataProtocolo'], c['CNPJ']])
            window.FindElement("Table_Viabilidade").update(self.DADOS_Viabilidade)

    def Table_Viabilidade(self,window, event, values,Viabilidade_Conteudo):
        Banco_de_Dados2 = getConnection()
        cursor2=Banco_de_Dados2.cursor()
        cursor2.execute(f"""select ProtocoloOrgao from solicitacao where IdSolicitacao = {self.DADOS_Viabilidade[values['Table_Viabilidade'][0]][0]}""")
        protocolo=cursor2.fetchone()
        cursor2.execute(f"""select * from viabilidade where Protocolo  = '{protocolo['ProtocoloOrgao']}';""")
        viabilidade = cursor2.fetchall()
        print(self.DADOS_Viabilidade[values['Table_Viabilidade'][0]][0])
        


        Viabilidade_Conteudo.find_element('ID_Solicitacao_viabilidade').Update(viabilidade[0]['IdSolicitacao']) # placeholder
        Viabilidade_Conteudo.find_element('Protocolo').Update(viabilidade[0]['Protocolo'])
        Viabilidade_Conteudo.find_element('Data_do_Protocolo').Update(viabilidade[0]['DataProtocolo'])
        Viabilidade_Conteudo.find_element('Razão_Social').Update(viabilidade[0]['RazaoSocial'])
        Viabilidade_Conteudo.find_element('Analise').Update(viabilidade[0]['Analise'])
        Viabilidade_Conteudo.find_element('Orgao').Update(viabilidade[0]['Orgao'])
        Viabilidade_Conteudo.find_element('Empresa_Estabelecida').Update(viabilidade[0]['EmpresaEstabelecida'])
        Viabilidade_Conteudo.find_element('CNPJ').Update(viabilidade[0]['CNPJ'])
        Viabilidade_Conteudo.find_element('Cidade').Update('Novo Horizonte')
        Viabilidade_Conteudo.find_element('Logradouro').Update(viabilidade[0]['Logradouro'])
        Viabilidade_Conteudo.find_element('Tipo_do_Logradouro').Update(viabilidade[0]['TipoLogradouro'])
        Viabilidade_Conteudo.find_element('Numero').Update(viabilidade[0]['Numero'])
        Viabilidade_Conteudo.find_element('CEP').Update(viabilidade[0]['Cep'])
        Viabilidade_Conteudo.find_element('Bairro').Update(viabilidade[0]['Bairro'])
        Viabilidade_Conteudo.find_element('Complemento').Update(viabilidade[0]['Complementos'])
        
    def Table_Viabilidade2(self,window, event, values,Viabilidade_Conteudo2):
        Banco_de_Dados2 = getConnection()
        cursor2=Banco_de_Dados2.cursor()
        cursor2.execute(f"""select ProtocoloOrgao from solicitacao where IdSolicitacao = {self.DADOS_Viabilidade[values['Table_Viabilidade'][0]][0]}""")
        protocolo=cursor2.fetchone()
        cursor2.execute(f"""select * from viabilidade where Protocolo  = '{protocolo['ProtocoloOrgao']}';""")
        viabilidade = cursor2.fetchall()


        Viabilidade_Conteudo2.find_element('Tipo_de_Unidade').Update(viabilidade[0]['TipoUnidade'])
        Viabilidade_Conteudo2.find_element('Inscricao_do_Imovel').Update(viabilidade[0]['NumeroInscricaoImovel'])
        Viabilidade_Conteudo2.find_element('Tipo_de_Inscrição').Update(viabilidade[0]['TipoInscricaoImovel'])
        Viabilidade_Conteudo2.find_element('Atividade Auxiliar').Update(viabilidade[0]['AtividadeAuxiliar'])
        Viabilidade_Conteudo2.find_element('Area_Estabelecimento').Update(viabilidade[0]['AreaEstabelecimento'])
        Viabilidade_Conteudo2.find_element('Forma_Atuacao').Update(viabilidade[0]['FormaAtuacao'])
        Viabilidade_Conteudo2.find_element('Area_Imovel').Update(viabilidade[0]['AreaImovel'])

    def Table_CNAE(self,window, event, values,Viabilidade_Conteudo):
        idsolicitacao = values['ID_Solicitacao_viabilidade']
        protocolo = values['Protocolo']
        dtprotocolo = values['Razão_Social']
        razaosocial = values['Data inicio']
        cnpj = values['CNPJ']
        nire = values['Nire']
        empresaestabelecida = values['Empresa_Estabelecida']
        orgao = values['Orgao']
        logradouro = values['Logradouro']
        numero = values['Numero']
        bairro = values['Bairro']
        cidade = values['Cidade']
        cep = values['CEP']
        tipodoLogradouro = values['Tipo_do_Logradouro']
        complemento = values['Complemento']
        tipodeUnidade = values['Tipo_de_Unidade']
        cpf_Servidor = values['CPF_Servidor']
        ativauxiliar = values['Ativ_Auxiliar']
        inscricaodoImovel = values['Inscricao_do_Imovel']
        analise = values['Analise']

        cursor = Banco_de_Dados.cursor()
        
        exibe = f"""
            select Cnae, Area_Estabelecimento, Resultado_da_Analise, Tipo_de_Inscricao
            from viabilidade 
            where Cnae  = '{cnpj}' or  Tipo_de_inscricao= '{orgao}'
            or Resultado_da_Analise = '{protocolo}';"""

        cursor.execute(exibe)
        resultado = cursor.fetchall()

        DADOS_Cnae=[]
        for g in resultado :
            DADOS_Cnae.append([g[0], g[1], g[2]])
            window.FindElement("Table_CNAE").update(DADOS_Cnae)







class Viabilidade:

    def __init__(self):
        self.msg=''
        self.idSolicitação=''
        self.Banco_de_Dados = getConnection()
        self.cursor=self.Banco_de_Dados.cursor()


#! =>   SOLICITAÇÃO
    def Solicitacao(self,idSolicitação):
        
        self.cursor.execute(f"""select ProtocoloOrgao from solicitacao where IdSolicitacao = {idSolicitação}""")
        protocolo=self.cursor.fetchone()
        self.idSolicitação=idSolicitação
        if self.cursor.execute("select * from solicitacao where IdSolicitacao = {} and situacaoSolicitacao ='Aguardando'".format(idSolicitação)):
            self.Confirmar_IPTU(idSolicitação)
        elif self.cursor.execute(f"""select * from viabilidade where Protocolo  = '{protocolo['ProtocoloOrgao']}';"""):
            self.msg='Solicitação já foi Deferida'
        else:
            self.msg='Solicitação Não Encontrada'
        self.Resposta()
            

#@ =>   IMOVEL 
    def Confirmar_IPTU(self,idSolicitação):
        """Verifica o tipo do cadastro do imovel, se for IPTU, vai comparar com os dados da solicatação, caso seja aprovado, chama o metodo Plano_Diretor"""

        if self.cursor.execute("select * from solicitacao where IdSolicitacao = {} and situacaoSolicitacao = 'aguardando'".format(idSolicitação)):
            INSCRICAO = self.cursor.fetchone()
            if INSCRICAO["TipoInscricaoImovel"].upper() == "IPTU" :
                if self.cursor.execute("select * from imoveis where Cadastro = {}".format(INSCRICAO["NumeroInscricaoImovel"])):
                    IPTU = self.cursor.fetchone()
                    if IPTU['Logradorou']==INSCRICAO['Logradouro'] and IPTU['Bairro']==INSCRICAO['Bairro'] and IPTU['Area_Construida']==INSCRICAO['AreaImovel'] and IPTU['numero'] == INSCRICAO['NumeroLogradouro']:
                        self.Plano_diretor(INSCRICAO)
                        
                    else:
                        self.msg='Dados não batem com os do Imovel'
                        self.InserirBanco_de_Dados("Indeferida",INSCRICAO)
                else:
                    self.msg='Numero De IPTU incorreto'
                    self.InserirBanco_de_Dados("Indeferida",INSCRICAO)
            elif INSCRICAO["TipoInscricaoImovel"].upper() == "RURAL":
                self.msg='Imovel Rural não foi Implementado'
            else:
                self.msg='Imovel sem Regularização apenas via processo administrativo'
                self.InserirBanco_de_Dados("Indeferida",INSCRICAO)
        else:
            self.msg='Numero de Inscrição Incorreto'
            self.InserirBanco_de_Dados("Indeferida",INSCRICAO)


#* =>   PLANO DIRETOR
    def Plano_diretor(self,INSCRICAO):
        stringResult='Deferida'
        self.msg='Deferida'
        for cnae in INSCRICAO['Cnae'].split(','):
            if self.cursor.execute("select * from plano_diretor where Cnae = '{}'".format(cnae)):
                retricao = self.cursor.fetchone()
                if retricao['Simbolo'] == '=' and INSCRICAO[retricao['Tipo_Dado']] != retricao['Condicao']:
                    self.msg='Plano Diretor Não Permite, atividade por logradouro não permitida'
                    print('aqui')
                    stringResult='Indeferida'
                    break
        
        
        self.InserirBanco_de_Dados(stringResult,INSCRICAO)


#& =>   SALVAR ANALISE
    def InserirBanco_de_Dados(self,resposta,INSCRICAO=0):

        if resposta == 'Deferida':  
	        status='Deferida'
        elif resposta == 'Indeferida':
            status='Indeferida'
        
        self.cursor.execute(f"update solicitacao set situacaoSolicitacao = '{status}' where IdSolicitacao = '{self.idSolicitação}'")
        print(f"INSERT INTO viabilidade VALUES('{self.idSolicitação}','{INSCRICAO['ProtocoloOrgao']}','{status}','{INSCRICAO['Nire']}','{INSCRICAO['CNPJ']}','{INSCRICAO['EmpresaEstabelecida']}','{INSCRICAO['Cnae']}','{INSCRICAO['AtividadeAuxiliar']}','{INSCRICAO['DataProtocolo']}','{str(datetime.now())[0:19]}','{INSCRICAO['TempoAndamento']}','{INSCRICAO['Cep']}','{INSCRICAO['TipoInscricaoImovel']}','{INSCRICAO['NumeroInscricaoImovel']}','{INSCRICAO['TipoLogradouro']}','{INSCRICAO['Logradouro']}','{INSCRICAO['NumeroLogradouro']}','{INSCRICAO['Bairro']}','{INSCRICAO['Complementos']}','{INSCRICAO['TipoUnidade']}','{INSCRICAO['FormaAtuacao']}','{INSCRICAO['Municipio']}','{INSCRICAO['RazaoSocial']}','{INSCRICAO['Orgao']}','{INSCRICAO['AreaImovel']}','{INSCRICAO['AreaEstabelecimento']}');")
        self.cursor.execute(f"INSERT INTO viabilidade VALUES('{self.idSolicitação}','{INSCRICAO['ProtocoloOrgao']}','{status}','{INSCRICAO['Nire']}','{INSCRICAO['CNPJ']}','{INSCRICAO['EmpresaEstabelecida']}','{INSCRICAO['Cnae']}','{INSCRICAO['AtividadeAuxiliar']}','{INSCRICAO['DataProtocolo']}','{str(datetime.now())[0:19]}','{INSCRICAO['TempoAndamento']}','{INSCRICAO['Cep']}','{INSCRICAO['TipoInscricaoImovel']}','{INSCRICAO['NumeroInscricaoImovel']}','{INSCRICAO['TipoLogradouro']}','{INSCRICAO['Logradouro']}','{INSCRICAO['NumeroLogradouro']}','{INSCRICAO['Bairro']}','{INSCRICAO['Complementos']}','{INSCRICAO['TipoUnidade']}','{INSCRICAO['FormaAtuacao']}','{INSCRICAO['Municipio']}','{INSCRICAO['RazaoSocial']}','{INSCRICAO['Orgao']}','{INSCRICAO['AreaImovel']}','{INSCRICAO['AreaEstabelecimento']}');")
        self.Resposta()


#? =>   RESPOSTA DA ANALISE
    def Resposta(self):      
        self.Banco_de_Dados.commit()
        return(self.msg)





