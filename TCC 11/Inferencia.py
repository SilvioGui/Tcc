from auth import getConnection,getConnection2
from collections import defaultdict
from collections import Counter
import PySimpleGUI as sg2
import buttons
import pymysql
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
class Inferencia():

    def __init__(self):
        print('--CONECÇÃO--')
        self.Banco_de_Dados = getConnection()
        self.Banco_de_Dados2 = getConnection2()
        self.cursor = self.Banco_de_Dados.cursor()
        self.cursor2 = self.Banco_de_Dados2.cursor()
        self.ordemExecutada=1
        self.id=0
        self.repeticao=False
        self.Inferencia_Melhor = Inferencia_Melhor()

    def layout(self,variavel):
        sg2.theme('Reddit')
        layout = [
        [sg2.Text(f"Campo {variavel} vazio, favor informar qual o valor:")],
        [sg2.InputText(key="valor_dado") ],
        [sg2.Button("Enviar", key= "Envio_Valor")],     
        ]
        return sg2.Window('Inferencia', layout, finalize=True)

    def Iniciar_Inferencias(self,id):
        if  id!=0:
            self.id=id
            return self.Condicoes()
        else:
            print('ID não Encontrado')
###################################################################################################################################
    def Condicoes(self):
        print('--BUSCA CONDICÃO--')
        if self.Inferencia_Melhor.verificacao():
            resultadoCondicoes=self.Inferencia_Melhor.melhor_escolha()
            self.Regras_ME(resultadoCondicoes)
        else:
            self.cursor.execute(' SELECT * FROM condicoes ')
            self.resultadoCondicoes = self.cursor.fetchall()
            print("--INICIO ANALISE--")
            self.regras(ordemRegra = 1, num_regra = 1)
            if self.repeticao:
                self.repeticao=False
                self.regras(1, 1)
###################################################################################################################################
    def regras(self, ordemRegra, num_regra):
        print(f"Numero da Regra: {num_regra}  Ordem: {ordemRegra}")
        for condicao in self.resultadoCondicoes:
            
            if condicao['numeroRegra'] == num_regra and condicao['ordem'] == ordemRegra:

                if self.cursor.execute(f"select * from executadas where regra_numero = {num_regra} and id_solicitacao = '{self.id}'"):
                    print('Regra ja Executada')
                    return self.regras(num_regra = num_regra + 1, ordemRegra = ordemRegra)
                else:
                    self.cursor.execute(f" SELECT MB_{condicao['variavelA']} from solicitacao where IdSolicitacao = {self.id}")
                    condicao['result']=next((a for a in self.cursor.fetchone().values()))

                    self.cursor.execute(f"SELECT conclusao FROM condicoes where ordem = {ordemRegra} and numeroRegra = {num_regra} ")    
                    condicao['conclusao_atual']=next((a for a in self.cursor.fetchone().values()))
                    print(condicao)
                    #-------------BUG--------------------#
                    if condicao['result'] ==None or condicao['result'] == '':
                        pergunta=self.layout(condicao['variavelA'])
                        Inferencia =None
                        envio =0
                        while True:
                            if envio == 1:
                                break
                            window,event,values = sg2.read_all_windows()
                            if event == 'Envio_Valor':
                                self.cursor.execute(f"update solicitacao set MB_{condicao['variavelA']}='{values['valor_dado']}' where IdSolicitacao = '{self.id}'")
                                sg2.popup('Dado salvo')
                                self.Banco_de_Dados.commit()
                                envio = 1
                                pergunta.hide()
                                break
                            
                    #-------------BUG--------------------#

                    self.Inferencia(ordemRegra, num_regra, condicao)
        



###################################################################################################################################
    def Inferencia(self, ordemRegra, num_regra,condicao):
        print('--INICIO INFERENCIA--')
        try:
            
            if condicao['condicao'] == '==':
                print('-Condição executada: ==')
                if condicao['result'] == condicao['variavelB']:
                    print('True')
                    return self.validacao_regras1(ordemRegra, num_regra, condicao)
                else:
                    print('False')
                    return self.validacao_regras2(ordemRegra, num_regra, condicao)
    ##################################################
            if condicao['condicao'] == '!=':
                print('-Condição executada: !=')
                if condicao['result'] != condicao['variavelB']:
                    print('True')
                    return self.validacao_regras1(ordemRegra, num_regra, condicao)
                else:
                    print('False')
                    return self.validacao_regras2(ordemRegra, num_regra, condicao)
    ##################################################
            if condicao['condicao'] == '>':
                print('-Condição executada: >')
                if condicao['result'] > condicao['variavelB']:
                    print('True')
                    return self.validacao_regras1(ordemRegra, num_regra, condicao)
                else:
                    print('False')
                    return self.validacao_regras2(ordemRegra, num_regra, condicao)
    ##################################################
            if condicao['condicao'] == '<':
                print('-Condição executada: <')
                if condicao['result'] < condicao['variavelB']:
                    print('True')
                    return self.validacao_regras1(ordemRegra, num_regra, condicao)
                else:
                    print('False')
                    return self.validacao_regras2(ordemRegra, num_regra, condicao)
        except:
            self.regras(ordemRegra = 1, num_regra = 1)
###################################################################################################################################
    def validacao_regras1(self, ordemRegra, num_regra,condicao):
        print('--VALIDACÃO TRUE--')
        if condicao['conclusao_atual'] == '&':
            print('-Conclusão: &')
            return self.regras( num_regra = num_regra, ordemRegra = ordemRegra + 1)

        elif condicao['conclusao'] == '||':
            print(bcolors.OK +  '-Conclusão: finalizada' + bcolors.RESET)
            self.cursor.execute('insert into executadas values (0 ,{}, {}, {})'.format(self.id, num_regra, self.ordemExecutada))

            self.cursor.execute(f"select * from condicoes where numeroRegra ={condicao['numeroRegra']} order by ordem desc")
            condicao_final= self.cursor.fetchone()

            self.cursor.execute(f"update solicitacao set MB_{condicao_final['conclusao']} where IdSolicitacao = '{self.id}'")
            self.ordemExecutada = self.ordemExecutada + 1
            self.Banco_de_Dados.commit()
            self.repeticao=True
        else:
            print(bcolors.OK +  '-Conclusão: finalizada' + bcolors.RESET)
            self.cursor.execute('insert into executadas values (0 ,{}, {}, {})'.format(self.id, num_regra, self.ordemExecutada))
            


            self.cursor.execute(f"update solicitacao set MB_{condicao['conclusao_atual']} where IdSolicitacao = '{self.id}'")
            self.ordemExecutada = self.ordemExecutada + 1
            self.Banco_de_Dados.commit()
            self.repeticao=True
            
            return self.regras(num_regra = num_regra + 1, ordemRegra = 1) 
###################################################################################################################################
    def validacao_regras2(self, ordemRegra, num_regra,condicao):
            print('--VALIDACÃO FALSE--')
            if condicao['conclusao_atual'] == '&':
                print('-Conclusão: &')
                return self.regras(num_regra = num_regra + 1, ordemRegra = ordemRegra) 

            elif condicao['conclusao_atual'] == '||':
                print('-Conclusão: ||')
                return self.regras( num_regra = num_regra, ordemRegra = ordemRegra + 1)

            else:
                print('-Conclusão: finalizada')
                return self.regras(num_regra = num_regra + 1, ordemRegra = 1) 
###################################################################################################################################







    def Regras_ME(self,resultadoCondicoes):
        for Ordem,Valores in resultadoCondicoes.items():
            print(bcolors.FAIL +"\nORDEM: " + bcolors.RESET, Ordem)
            Valor_Executed=0
            for Valor in Valores:
                if Valor['numeroRegra'] != Valor_Executed:
                    print('Regra: ',Valor['numeroRegra'])
                    if self.Verificacao_ME(resultadoCondicoes,Valor['numeroRegra']):


                        self.cursor.execute(f" SELECT MB_{Valor['variavelA']} from solicitacao where IdSolicitacao = {self.id}")
                        Valor['result']=next((a for a in self.cursor.fetchone().values()))

                        #self.cursor.execute(f"SELECT conclusao FROM condicoes where ordem = {Ordem} and numeroRegra = {Valor['numeroRegra']} ")    
                        #condicao['conclusao_atual']=next((a for a in self.cursor.fetchone().values()))


                        #-------------BUG--------------------#
                        if Valor['result'] ==None or Valor['result'] == '':
                            pergunta=self.layout(Valor['variavelA'])
                            Inferencia =None
                            while True:
                                window,event,values = sg2.read_all_windows()
                                if event == 'Envio_Valor':
                                    self.cursor.execute(f"update solicitacao set MB_{Valor['variavelA']}='{values['valor_dado']}' where IdSolicitacao = '{self.id}'")
                                    sg2.popup('Dado salvo')
                                    self.Banco_de_Dados.commit()
                                    pergunta.hide()
                                    break
                        #-------------BUG--------------------#
                        print(Valor)
                        self.Inferencia_ME(Valor,Valor['numeroRegra'])
                    else:
                        Valor_Executed=Valor['numeroRegra']
        
    def Inferencia_ME(self,Valor,num_regra):

        print(bcolors.OK + '--INICIO INFERENCIA--'+ bcolors.RESET)
        if Valor['condicao'] == '==':
            print('-Condição executada: ==')
            if Valor['result'] == Valor['variavelB']:
                print('True')
                return self.validacao_regras1_ME(num_regra, Valor)
            else:
                print('False')
                return self.validacao_regras2_ME(num_regra, Valor)
##################################################
        if Valor['condicao'] == '!=':
            print('-Condição executada: !=')
            if Valor['result'] != Valor['variavelB']:
                print('True')
                return self.validacao_regras1_ME(num_regra, Valor)
            else:
                print('False')
                return self.validacao_regras2_ME(num_regra, Valor)
##################################################
        if Valor['condicao'] == '>':
            print('-Condição executada: >')
            if Valor['result'] > Valor['variavelB']:
                print('True')
                return self.validacao_regras1_ME(num_regra, Valor)
            else:
                print('False')
                return self.validacao_regras2_ME(num_regra, Valor)
##################################################
        if Valor['condicao'] == '<':
            print('-Condição executada: <')
            if Valor['result'] < Valor['variavelB']:
                print('True')
                return self.validacao_regras1_ME(num_regra, Valor)
            else:
                print('False')
                return self.validacao_regras2_ME(num_regra, Valor)



    def validacao_regras1_ME(self,num_regra, Valor):
        print(bcolors.OK +  '--VALIDACÃO TRUE--'+ bcolors.RESET)
        if Valor['conclusao'] == '&':
            print('-Conclusão: &')
            
        elif Valor['conclusao'] == '||':
            print(bcolors.OK +  '-Conclusão: finalizada' + bcolors.RESET)
            self.cursor.execute('insert into executadas values (0 ,{}, {}, {})'.format(self.id, num_regra, self.ordemExecutada))

            self.cursor.execute(f"select * from condicoes where numeroRegra ={Valor['numeroRegra']} order by ordem desc")
            condicao_final= self.cursor.fetchone()

            self.cursor.execute(f"update solicitacao set MB_{condicao_final['conclusao']} where IdSolicitacao = '{self.id}'")
            self.ordemExecutada = self.ordemExecutada + 1
            self.Banco_de_Dados.commit()
        else:
            print(bcolors.OK +  '-Conclusão: finalizada' + bcolors.RESET)
            self.cursor.execute('insert into executadas values (0 ,{}, {}, {})'.format(self.id, num_regra, self.ordemExecutada))
            self.cursor.execute(f"update solicitacao set MB_{Valor['conclusao']} where IdSolicitacao = '{self.id}'")
            self.ordemExecutada = self.ordemExecutada + 1
            self.Banco_de_Dados.commit()

        
    def validacao_regras2_ME(self,num_regra, Valor):
        print(bcolors.OK +  '--VALIDACÃO FALSE--'+ bcolors.RESET)
        
        if Valor['conclusao'] == '&':
            print('-Conclusão: finalizada')
            Valor_Executed=num_regra
            
        elif Valor['conclusao'] == '||':
             print('-Conclusão: ||')
        else:
            print('-Conclusão: finalizada')

    def Verificacao_ME(self,resultadoCondicoes,num_regra):
        if self.cursor.execute(f"select * from executadas where regra_numero = {num_regra} and id_solicitacao = '{self.id}'"):
                print(bcolors.WARNING + 'Regra ja Executada\n'+ bcolors.RESET)

                return False
        else:
                return True        


























###################################################################################################################################        

class   Inferencia_Melhor ():
    def __init__ (self):
        self.Banco_de_Dados = getConnection()
        self.Banco_de_Dados2 = getConnection2()
        self.cursor = self.Banco_de_Dados.cursor()
        self.cursor2 = self.Banco_de_Dados2.cursor()

    def verificacao (self):
        total_elemento_executados=0
        total_elemento_condicoes=0
        self.cursor.execute("select * from executadas")
        execuadas = self.cursor.fetchall()
        
        self.cursor.execute("select * from condicoes")
        condicoes = self.cursor.fetchall()



        #parametro de decisão deve ser de ao menos  75% das regras no executadas
        try:
            b=Counter(a['regra_numero'] for a in execuadas )
            for _ in b:
                total_elemento_executados+=1

            b=Counter(a['numeroRegra'] for a in condicoes )
            for _ in b:
                total_elemento_condicoes+=1

            print(total_elemento_executados/total_elemento_condicoes)

            if total_elemento_executados/total_elemento_condicoes< 0.75:
                return False

                return True
        except:
            return False 

    def melhor_escolha(self):
        self.cursor.execute(f"TRUNCATE `tcc`.`melhor_escolha`")
        self.Banco_de_Dados.commit()
        contar_regra = defaultdict(int)

        contar_ordem_regra = defaultdict(dict)
        self.cursor.execute("select * from executadas")
        execuadas = self.cursor.fetchall()

        for ex in execuadas:
            contar_ordem_regra[ex['ordemExecutada']] = {}
        
        for  count in contar_ordem_regra:
            contar_regra = defaultdict(int)
            for ex in execuadas:
                contar_regra[ex['regra_numero']] = 0

            contar_ordem_regra[count] =contar_regra
        a=0
        for cor in contar_ordem_regra:

            for cr in contar_ordem_regra[cor]:
                cr2=contar_ordem_regra[cor]
                for ex in execuadas:
                    if ex['regra_numero'] == cr and ex['ordemExecutada'] == cor: cr2[cr] += 1
                

        
        for cor in contar_ordem_regra:
            maior=0
            for cr in contar_ordem_regra[cor]:
                cr2=contar_ordem_regra[cor]
                self.cursor.execute(f"INSERT INTO `tcc`.`melhor_escolha` VALUES (0,{cor},{cr},{cr2[cr]});")
        self.Banco_de_Dados.commit()

        melhor_escolha = defaultdict(list)
        for cor in contar_ordem_regra: 
            self.cursor.execute(f"select Ordem,Regra,Valor from `tcc`.`melhor_escolha` where Ordem ={cor} order by Valor desc;")
            Ordem_Regras = self.cursor.fetchall()
            for OR in Ordem_Regras:
                self.cursor.execute(f"SELECT * FROM condicoes where numeroRegra ={OR['Regra']}")
                regras = self.cursor.fetchall()

                melhor_escolha[cor]+=regras
        
        for me in melhor_escolha:
            print('Ordem: ',me)
            for me_r in melhor_escolha[me]:
                print('Values: ', me_r)
        
        return melhor_escolha
        #print(Counter(a for a in next(exec_dict for exec_dict in execuadas).items()))
       #print(Counter(a for a in (exec_dict for exec_dict in execuadas).items() if a != 'total'))




