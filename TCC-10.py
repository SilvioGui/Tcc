from ast import While
from fileinput import filename
from tkinter import Button, Image
import PySimpleGUI as sg
import mysql.connector
import buttons



con = mysql.connector.connect(host='127.0.0.1',database='teste',user='root',password='')

DADOS_Viabilidade= []
DADOSLicenciamento= []

def tela_inicial():   
    sg.theme('Reddit')
    layout = [
        #[sg.Text('',size=(8,10)), sg.Image(filename='fundo.png')],
        [sg.Text("Selecione a Categoria:")],
        #[sg.InputText(key="nome_cotacao")],
        #
        [sg.Button('', image_data=buttons.button_viabilidade_base64, key='Viabilidade', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), 
         sg.Button('', image_data=buttons.button_licenciamento_base64, key='Licenciamento', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Button('', image_data=buttons.button_mobiliario_base64, key='Mobiliario', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Button('', image_data=buttons.button_procuraremp_base64, key='Procurar Empresa', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Button('', image_data=buttons.button_addregra_base64, key='Adicionar regras', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
]

    return sg.Window('IA', layout, finalize=True)

##########################################################################

def janela_viabilidade():
    janela1.hide()     
    sg.theme('Reddit')
    
    layout = [
        [sg.Text("Digite seu Protocolo ou CNPJ :")],
        [sg.InputText(key="vb_dados") ],
        [sg.Text("Selecione um Orgão")],
        [sg.Spin(["São Paulo"], key="vb_orgao", )],
        [sg.Text("Periodo")],
        [sg.Text("Início"),sg.InputText(key="Data inicio", size=(20,1), ), 
         sg.Button('', image_data=buttons.button_calender_base64, key='Data Inicio', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Text("Final"), sg.InputText(key="Data fim", size=(20,1)), 
         sg.Button('', image_data=buttons.button_calender_base64, key='Data Fim', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), 
         sg.Button('', image_data=buttons.button_ir_base64, key='PS_Viabilidade', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
         sg.Button("Limpar", key= "Limpar Viabilidade")],
        [sg.Table( DADOS_Viabilidade, ['Protocolo','Situação ','Dt Solicitação', 'CNPJ',], num_rows=10,enable_events=True, key= "Table_Viabilidade")]
        
    ]
    
    return sg.Window('Consulta de Protocolo de Viabilidade', layout, finalize=True)

##########################################################################  

def janela_Licenciamento():
    janela1.hide()     
    sg.theme('Reddit')
    layout = [
        [sg.Text("Selecione um Orgão")],
        [sg.Spin(["São Paulo"], size=(20,1), key="orgao_licenciamento")],
        [sg.Text("Digite seu CNPJ ou Protocolo")],
        [sg.InputText(do_not_clear=False, key = "dados_licenciamento"), 
         sg.Button('', image_data=buttons.button_x_base64, key='PS_Licenciamento', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0),
        sg.Button ("limpar", key= "Limpar Licenciamento")],
        [sg.Table( DADOSLicenciamento, ['sem nome 1','sem nome 2','sem nome 3', 'sem nome 4'], num_rows=10,  key= "Table_Licenciamento")]
    ]
    return sg.Window('Consulta Licenciamento', layout, finalize=True)

##########################################################################  

def janela_Mobiliario():
    janela1.hide()     
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
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0), sg.Button('', image_data=buttons.button_ir_base64, key='Pesquisa', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
        [sg.Output(size=(133,20))]
    ]
    return sg.Window('Mobiliario', layout, finalize=True)

##########################################################################  

def janela_Procurar_Empresa():
    janela1.hide()     
    sg.theme('Reddit')
    layout = [
        [sg.Text("Pesquisar por")],
        [sg.Checkbox("CNPJ", key = "cnpj"),sg.Checkbox("Protocolo", key = "protocolo"), sg.InputText(key="Protocolo") ],
        [sg.Text("Selecione um Orgão")],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
    
    ]
    return sg.Window('Procurar Empresa ', layout, finalize=True)

##########################################################################  

def janela_Adicionar_regras():
    janela1.hide()     
    layout = [
        [sg.Text("Pesquisar por")],
        [sg.Checkbox("CNPJ", key = "cnpj"),sg.Checkbox("Protocolo", key = "protocolo"), sg.InputText(key="Protocolo") ],
        [sg.Text("Selecione um Orgão")],
        [sg.Button('', image_data=buttons.button_voltar_base64, key='Voltar', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0)],
    ]
    return sg.Window('Regras', layout, finalize=True)



##########################################################################    

janela1, janela2, janela3, janela4, janela5, janela6 = tela_inicial(), None, None, None, None, None

##########################################################################  

def FormatarData(date):
    if(not date): 
        return "ex: dd/mm/yyyy"
    else : 
        day, month, year = date[1], date[0], date[2]

        if( month < 10):
            month = '0'+ str(month)
        if(day < 10) :
            day = '0'+ str(day)
        
        return f"{day}/{month}/{year}"
        
##########################################################################

while True:
    window,event,values = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    if window == janela4 and event == sg.WIN_CLOSED:
        break
    if window == janela5 and event == sg.WIN_CLOSED:
        break
    if window == janela6 and event == sg.WIN_CLOSED:
        break

       ###Pop up para confirma se realmente quer sair, vincular com o botão "Fechar" (X)
      ##if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
     #   break
     
##########################################################################
        
    if window ==janela1 and event =='Viabilidade':  
      janela2= janela_viabilidade()
      janela2.find_element('Data inicio').Update('ex: dd/mm/yyyy') # placeholder
      janela2.find_element('Data fim').Update('ex: dd/mm/yyyy') # placeholder
    if window ==janela1 and event =='Licenciamento':
      janela3= janela_Licenciamento()
    
    if window ==janela1 and event =='Mobiliario':
      janela4= janela_Mobiliario()
      
    if window ==janela1 and event =='Procurar Empresa':
      janela5= janela_Procurar_Empresa()
   
    if window ==janela1 and event =='Adicionar regras':
      janela6= janela_Adicionar_regras()
    
##########################################################################

    if window == janela2 and event == "Voltar":
        janela2.hide()
        janela1.un_hide()
        DADOS_Viabilidade= []
          
    elif window == janela2 and event == "Data Inicio" :
        dataSelecionada = sg.popup_get_date(month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('DOM', 'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB'))
        data = FormatarData(dataSelecionada)
        window['Data inicio'].Update(data)
    elif window == janela2 and event == "Data Fim" :
        dataSelecionada = sg.popup_get_date(month_names=('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'), day_abbreviations=('DOM', 'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB'))
        data = FormatarData(dataSelecionada)
        window['Data fim'].Update(data)     

##########################################################################

    if window == janela3 and event == "Voltar":
        janela3.hide()
        janela1.un_hide()
        DADOSLicenciamento= []

    if window == janela4 and event == "Voltar":
        janela4.hide()
        janela1.un_hide()    

    if window == janela5 and event == "Voltar":
        janela5.hide()
        janela1.un_hide()

    if window == janela6 and event == "Voltar":
        janela6.hide()
        janela1.un_hide()
        
################################ Limpar tela ##############################################
    if event == 'Limpar Viabilidade':
        window.FindElement('vb_dados').Update('')
        window.FindElement('Data inicio').Update('')
        window.FindElement('Data fim').Update('')
        window.FindElement('Table_Viabilidade').Update('')


    if event == 'Limpar Licenciamento':
        window.FindElement('dados_licenciamento').Update('')
        window.FindElement('Table_Licenciamento').Update('')
       
        



########################### Pesquisas no banco de Dados Viabilidade ###############################################
    if event == 'PS_Viabilidade':
        dados= values['vb_dados']
        orgao = values['vb_orgao']
        dataInicio = values['Data inicio']
        dataFim = values['Data fim']

        cursor = con.cursor()
        exibe = f"""
        select IdSolicitacao ,Analise,DataProtocolo,CNPJ 
        from viabilidade 
        where IdSolicitacao  = '{dados}' or  Cnpj= '{dados}'
        or Orgao = '{orgao}' 
        or DataProtocolo >= '{dataInicio}' AND DataProtocolo <=  '{dataFim}';"""

        cursor.execute(exibe)
        resultado = cursor.fetchall()
        
        
        DADOS_Viabilidade=[]
        for c in resultado :
            DADOS_Viabilidade.append([c[0], c[1], c[2], c[3]])
            window.FindElement("Table_Viabilidade").update(DADOS_Viabilidade)
            
 ########################### Seleção dos itens Popup ###############################################     

    if event == 'Table_Viabilidade':
    
        selected_index = values['Table_Viabilidade'][0]
        selected_row = [selected_index]
        popup_message =selected_row[0] 
        sg.popup(popup_message)
        print(selected_row)       

 ########################### Pesquisas no banco de Dados Licenciamento ###############################################       
    if event == 'PS_Licenciamento':
        orgao_licenciamento =values ['orgao_licenciamento']
        dados_licenciamento =values ['dados_licenciamento']

        cursor = con.cursor()
        exibe = f"""
         select ProtocoloLicenca,  Orgao,situacaoSolicitacao,DataSolicitacaoLicenciamento
         from licenciamento
         where ProtocoloLicenca  = '{dados_licenciamento}' or  Cnpj= '{dados_licenciamento}' 
         or Orgao = '{orgao_licenciamento}';"""

        cursor.execute(exibe)
        resultado = cursor.fetchall()

        DADOSLicenciamento=[]
        for l in resultado :
            DADOSLicenciamento.append([l[0], l[1], l[2], l[3]])
            window.FindElement("Table_Licenciamento").update(DADOSLicenciamento)

 ########################### Seleção dos itens ###############################################    

    if event == 'Table_Licenciamento':
    
        selected_index = values['Table_Licenciamento'][0]
        selected_row = [selected_index]
        popup_message =selected_row[0] 
        sg.popup(popup_message)
        print(selected_row)  