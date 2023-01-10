from ast import While
from fileinput import filename

from tkinter import Button, Image
import PySimpleGUI as sg
import mysql.connector
import buttons
import yaml, os
from auth import getConnection,getConnection2

from Menu import Tela_Menu
from Solicitacao import Tela_Solicitacao
from Viabilidade import Tela_Viabilidade
from Licenciamento import Tela_Licenciamento
from Mobiliario import Tela_Mobiliario
from Regra import Tela_Regra

#conexão com o banco#
Banco_de_Dados = getConnection2()
cursor=Banco_de_Dados.cursor()

Tela_Menu = Tela_Menu()
Tela_Solicitacao = Tela_Solicitacao()
Tela_Viabilidade = Tela_Viabilidade()
Tela_Licenciamento = Tela_Licenciamento()
Tela_Mobiliario = Tela_Mobiliario()
Tela_Regra = Tela_Regra()

Menu = Tela_Menu.Layout()
Solicitacao = None
Viabilidade = None
Licenciamento = None
Mobiliario = None
Regra = None
Inferencia = None
Documento = None
Envio_Documento_Deferida = None
Viabilidade_Conteudo = None
Viabilidade_Conteudo2 = None
exRegra_tela = None
Licenciamento_Conteudo = None
Mobiliario_Conteudo1 = None
while True:
    window,event,values = sg.read_all_windows()
    print(event)
    #$Abrir janelas Menu
    if window == Menu and event =='Solicitacao':
        Menu.hide()
        Solicitacao = Tela_Solicitacao.Layout()
    if window == Menu and event =='Viabilidade':
        Menu.hide()
        Viabilidade = Tela_Viabilidade.Layout()
    if window ==Menu and event =='Licenciamento':
        Menu.hide()
        Licenciamento = Tela_Licenciamento.Layout()
    if window ==Menu and event =='Mobiliario':
        Menu.hide()
        Mobiliario = Tela_Mobiliario.Layout()
    if window ==Menu and event =='regra':
        Menu.hide()
        Regra = Tela_Regra.Layout()

    #$Abrir janelas Solicitacao
    if window == Solicitacao and event =='Table_Solicitacao':
        Solicitacao.hide()
        Inferencia = Tela_Solicitacao.Layout_Inferencia()
    if window == Inferencia and event == "Envio Documento":
        Inferencia.hide()
        Documento = Tela_Solicitacao.Layout_Documento()

    #$Abrir janelas Licenciamento
    if window == Licenciamento and event == 'Table_Licenciamento':
        row = values['Table_Licenciamento']
        Licenciamento_Conteudo = Tela_Licenciamento.janela_Dados_completos_licenciamento()

    if window == Licenciamento_Conteudo and event == 'PG_Licenciamento':
        Licenciamento_Conteudo.hide()
        Licenciamento_Conteudo  = Tela_Licenciamento.janela_Dados_completos_licenciamento2()
        

    #$Abrir janelas Viabilidade
    if window == Viabilidade and event == 'Table_Viabilidade':
        Viabilidade_Conteudo = Tela_Viabilidade.Loyout_Dados_Viabilidade()
        
    if window == Viabilidade_Conteudo and event == 'Table_Viabilidade2':
        Viabilidade_Conteudo.un_hide()
        Viabilidade_Conteudo2 = Tela_Viabilidade.Loyout_Dados_Viabilidade2()
    
    #$Abrir janelas Regras
    if window == Regra and event == 'excluir_Regra':
        exRegra_tela = Tela_Regra.Layout2()

    #$Abrir janelas Mobiliario
    if window == Mobiliario and event =='Table_Mobiliario':
        Mobiliario.hide()
        Mobiliario_Conteudo1=Tela_Mobiliario.Layout2()

    #$Voltar janelas
    if window == Solicitacao and event == "Voltar":
        Solicitacao.hide()
        Menu.un_hide()
    if window == Viabilidade and event == "Voltar":
        Viabilidade.hide()
        Menu.un_hide()
    if window == Licenciamento and event == "Voltar":
        Licenciamento.hide()
        Menu.un_hide()
    if window == Mobiliario and event == "Voltar":
        Mobiliario.hide()
        Menu.un_hide()
    if window == Regra and event == "Voltar":
        Regra.hide()
        Menu.un_hide()
    if window == Inferencia and event == "Voltar":
        Inferencia.hide()
        Solicitacao.un_hide()
    if window == Documento and event == "Voltar":
        Documento.hide()
        Inferencia.un_hide()
    if window == Envio_Documento_Deferida and event == "Voltar":
        Envio_Documento_Deferida.hide()
        Inferencia.un_hide()
    if window == Viabilidade_Conteudo and event == "Voltar":
        Viabilidade_Conteudo.hide()
        Viabilidade.un_hide()
    if window == Viabilidade_Conteudo2 and event == "Voltar":
        Viabilidade_Conteudo2.hide()
        Viabilidade_Conteudo.un_hide()
    if window == exRegra_tela and event == "Voltar":
        exRegra_tela.hide()
        Regra.un_hide()
    if window == Licenciamento_Conteudo and event == "Voltar":
        Licenciamento_Conteudo.hide()
        Licenciamento.un_hide()

    #$Fechar janelas
    if window == Menu and event == sg.WIN_CLOSED:
        break
    if window == Solicitacao and event == sg.WIN_CLOSED:
        break
    if window == Viabilidade and event == sg.WIN_CLOSED:
        break
    if window == Licenciamento and event == sg.WIN_CLOSED:
        break
    if window == Mobiliario and event == sg.WIN_CLOSED:
        break
    if window == Regra and event == sg.WIN_CLOSED:
        break
    if window == Inferencia and event == sg.WIN_CLOSED:
        break
    if window == Documento and event == sg.WIN_CLOSED:
        break
    if window == Envio_Documento_Deferida and event == sg.WIN_CLOSED:
        break
    if window == Viabilidade_Conteudo and event == sg.WIN_CLOSED:
        break
    if window == Viabilidade_Conteudo2 and event == sg.WIN_CLOSED:
        break
    if window == exRegra_tela and event == sg.WIN_CLOSED:
        break
    if window == Mobiliario_Conteudo1 and event == sg.WIN_CLOSED:
        break
    if window == Licenciamento_Conteudo and event == sg.WIN_CLOSED:
        break
    #$Eventos Solicitacao
    if window == Solicitacao and event == 'PS_Solicitacao':
        Tela_Solicitacao.PS_Solicitacao(window,event,values)
    if  window == Solicitacao and  event == 'Limpar Solicitação':
        Tela_Solicitacao.Limpar_Solicitacao(window,event,values)
    if window == Solicitacao and event == 'Table_Solicitacao':
        print(values)
        try:
            row=values['Table_Solicitacao'][0]
        except:
            pass
    if window == Inferencia and  event == 'Analisar Vibilidade':
        Tela_Solicitacao.Analisar_Vibilidade(window, event, values,row)

    if window == Inferencia and event == 'Analisar Licenciamento':

        if Tela_Solicitacao.Analisar_Licenciamento(window, event, values,row):
            if Tela_Solicitacao.Licenciamento.Resposta()  =='Alto Risco':
                Inferencia.hide()
                Documento = Tela_Solicitacao.Layout_Documento()
            else:
                print('baixo risco')
                Tela_Solicitacao.Envio_Baixo_Risco(window, event, values,row)
                


    if  event == 'Envio Documento':
        Documento.hide()
        resposta = Tela_Solicitacao.Envio_Documento(window, event, values,row)
        if resposta == 'Deferida':
            Envio_Documento_Deferida = Tela_Solicitacao.Layout__Envio_documento()
        else:
            Inferencia.un_hide()    

    if event == 'Envio Documento Deferida':
        event = Tela_Solicitacao.Envio_Documento_Deferida(window, event, values,row)
        Envio_Documento_Deferida.hide()
        Inferencia.un_hide()

        
    if window == Inferencia and event == 'Analisar Inferencia':
        Tela_Solicitacao.Analisar_Inferencia(window, event, values, row)
        
        Tela_Solicitacao.Exportar_Dados()

    #$Eventos Viabilidade
    if window == Viabilidade and event == 'PS_Viabilidade':
        Tela_Viabilidade.PS_Viabilidade(window, event, values)
    if window == Viabilidade and event == 'Table_Viabilidade':
        values_v=values
        Tela_Viabilidade.Table_Viabilidade(window, event, values,Viabilidade_Conteudo)
        
    if window == Viabilidade_Conteudo and event == 'Table_Viabilidade2':
        Tela_Viabilidade.Table_Viabilidade2(window, event, values_v,Viabilidade_Conteudo2)
    if window == Viabilidade and event == 'Limpar Viabilidade':
        Tela_Viabilidade.Limpar_Viabilidade(window, event, values)

    #$Eventos Licenciamento
    if window == Licenciamento and event == 'Limpar Licenciamento':
        Tela_Licenciamento.Limpar_Licenciamento(window, event,  values)
    if window == Licenciamento and event == 'PS_Licenciamento':
        Tela_Licenciamento.PS_Licenciamento(window, event, values)

    if window == Licenciamento and event == 'Table_Licenciamento':
        Tela_Licenciamento.Table_Licenciamento(window, event, values,Licenciamento_Conteudo,row)

    #$Eventos Regras
    if window == Regra and event == 'PS_Regras':
        Tela_Regra.PS_Regras(window,event,values)
    if window == Regra and event == 'Adicionar_Regra':
        Tela_Regra.Adicionar_Regra(window, event, values)
        pass
    if window == Regra and event == 'excluir_Regra':
        rows=values['excluir_Regra'][0]

    if window == exRegra_tela and event =='Exclusao':

        Tela_Regra.exclusao(rows)
        exRegra_tela.hide()

    #$Eventos Mobiliario
    if window == Mobiliario and event == 'PS_Mobiliario':
        Tela_Mobiliario.PS_Mobiliario(window, event, values)

    
