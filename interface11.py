from ast import Break
from calendar import c
from cgitb import text
from cmath import e
from ctypes import sizeof
from dataclasses import field
from glob import escape
from tkinter import Y
from typing import Literal
import PySimpleGUI as sg
import sqlite3
from sqlite3 import Error
import smtplib
from email.message import EmailMessage
import os
from twilio.rest import Client
caminho = "C:\\sistemaachadoseperdidos\\agenda.db"
# TELA DE MENUPRINCIPAL =======================================================================================================================================================================================
class Telamenuprincipal():
    def __init__(self):
        global janela
        #layout
        layout = [
            [sg.Image(filename="menu.png",size=(450,87))],
            [sg.Button("CADASTRAR VÍTIMAS",size=(50,2),pad=((20,10),(10,0)))],
            [sg.Button("CADASTRAR OBJETOS",size=(50,2),pad=((20,10),(2,0)))],
            [sg.Button("ATUALIZAR DADOS DA VÍTIMA",size=(50,2),pad=((20,10),(2,0)))],
            [sg.Button("ATUALIZAR DADOS DO OBJETO",size=(50,2),pad=((20,10),(2,0)))],
            [sg.Button("EXCLUIR VÍTIMAS",size=(50,2),pad=((20,10),(2,0)))],
            [sg.Button("OBJETOS ACHADOS",size=(50,2),pad=((20,10),(2,0)))],
            [sg.Button("EXCLIR OBJETOS ACHADOS",size=(50,2),pad=((20,10),(2,0)))],
            [sg.Button("CONSULTAR VÍTIMAS",size=(50,2),pad=((20,10),(2,0)))],
            [sg.Button("CONSULTAR OBJETOS DA VÍTIMA",size=(50,2),pad=((20,10),(2,0)))]
        ]
        #janela
        janela = sg.Window("TELA DE MENU",size=(470,510)).layout(layout)
        self.button,self.values = janela.read()
    def iniciar(self):
        global escolha
        if self.button == "CADASTRAR VÍTIMAS":
            escolha = '1'
            janela.hide()
        elif self.button == "CADASTRAR OBJETOS":
            escolha = '2'
            janela.hide()
        elif self.button == "ATUALIZAR DADOS DA VÍTIMA":
            escolha = '3'
            janela.hide()
        elif self.button == "ATUALIZAR DADOS DO OBJETO":
            escolha = '4'
            janela.hide()
        elif self.button == "EXCLUIR VÍTIMAS":
            escolha = '5'
            janela.hide()
        elif self.button == "OBJETOS ACHADOS":
            escolha = '6'
            janela.hide()
        elif self.button == "EXCLIR OBJETOS ACHADOS":
            escolha = '7'
            janela.hide()
        elif self.button == "CONSULTAR VÍTIMAS":
            escolha = '8'
            janela.hide()
        elif self.button == "CONSULTAR OBJETOS DA VÍTIMA":
            escolha = '9'
            janela.hide()
        return escolha
        
# TELA DE CADASTRO DE USUSARIO ================================================================================================================================================================================
class telacadastrousuario():
    def __init__(self):
        global janela 
        layout = [
            [sg.Image(filename="teste2.png",size=(450,87))],
            [sg.Text('NOME',size=(20,0)),sg.Text('                           NASCIMENTO')],
            [sg.Input(size=(30,0),key='nome'),sg.Text("DIA"),sg.Combo(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'],key='dia'),sg.Text("MES"),sg.Combo(["JAN","FEV","MAR","ABR","MAI","JUN","JUL","AGO","SET","OUT","NOV","DEZ"],key='mes'),sg.Text('ANO'),sg.Combo(['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],key='ano')],
            [sg.Text('TELEFONE',size=(8,0)),sg.Text("EX:(+55 98 9XXXX XXXX)")],
            [sg.Input(size=(30,0),key='tel')],
            [sg.Text('CPF',size=(20,0))],
            [sg.Input(size=(30,0),key='cpf')],
            [sg.Text('EMAIL',size=(5,0))],
            [sg.Input(size=(30,0),key='email')],
            [sg.Text("SEXO:")],
            [sg.Checkbox("Masculino",key='mas'),sg.Checkbox("Feminino",key='fem'),sg.Checkbox("Outros",key='outr')],
            [sg.Button('ENVIAR DADOS'),sg.Button("VOLTAR PARA O MENU")]
            
        ]
        janela = sg.Window("CADASTRO DOS DADOS",size=(530,410)).layout(layout)
        self.button,self.values = janela.read()
       
    def inserirnobanco(self):
        proximo = False
        if self.button == 'VOLTAR PARA O MENU':
            proximo = True
            janela.hide()
        while proximo!=True:
            try:
                nome = self.values['nome']
                telefone = self.values['tel']
                cpf = self.values['cpf']
                email = self.values['email']
                if self.values['mas']:
                    sexo = 'Masculino'
                elif self.values["fem"]:
                    sexo =  "Feminino"
                else:
                    sexo = "Outros"
                dia = self.values['dia']
                mes = self.values['mes']
                ano = self.values['ano']
                vsql0 = "INSERT INTO sistema ( N_CPFVITIMA,T_NOMEVITIMA,T_TELEFONEVITIMA,T_EMAILVITIMA,T_SEXOVITIMA,N_DIANASCIMENTO,T_MESNASCIMENTO,N_ANONASCIMENTO)VALUES('"+cpf+"','"+nome+"','"+telefone+"','"+email+"','"+sexo+"','"+dia+"','"+mes+"','"+ano+"')"
                con = sqlite3.connect(caminho)
                c= con.cursor()
                c.execute(vsql0)
                con.commit()
                con.close()
                if self.button == 'ENVIAR DADOS':
                    sg.popup('USUARIO CADASTRADO COM SUCESSO!')
                    proximo = True
                    janela.hide()  
            except:
                sg.popup('CPF JÁ CADASTRADO SISTEMA!!\nDescrição:\nEsse cpf Já está em uso, por favor verifique os dados e cadastre novamente!!')
                proximo = False
                self.button,self.values = janela.read()
                if self.button == "VOLTAR PARA O MENU":
                    proximo = True
                    janela.hide()
        
#TELA DE ATUALZIZAR TELEFONE ==================================================================================================================================================================================

class atuaalizatelefone():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    def __init__(self):
        global janela
        tela = [
            [sg.Image(filename="2.png",size=(450,87))],
            [sg.Text('CPF:')],
            [sg.Input(size=(20,0),key="cpfvit")],
            [sg.Text('NOVO NÚMERO:')],
            [sg.Input(size=(30,0),key="novnum")],
            [sg.Button('ENVIAR'),sg.Button("VOLTAR")],
            [sg.Image(filename="atualizacao2.png",size=(450,87))]
        ]
        janela = sg.Window('ATUALIZAR TELEFONE',size=(400,350)).layout(tela)
        self.button,self.values = janela.read()
    def inserirnobanco1(self):
        proximo = False
        if self.button == 'VOLTAR':
            proximo = True
            janela.hide()
        while proximo!=True:
            try:
                condicao = False
                cpf_vitima = self.values["cpfvit"]
                novo_tel = self.values["novnum"]
                vsqlteste = "SELECT * from sistema"
                con = sqlite3.connect(caminho)
                c = con.cursor()
                c.execute(vsqlteste)
                resultado = c.fetchall()
                con.close()
                for c in resultado:
                    if  c[0] == int(cpf_vitima):
                        condicao = True
                if condicao:
                    vsql5 = "UPDATE sistema SET T_TELEFONEVITIMA = '"+novo_tel+"' WHERE N_CPFVITIMA == "+cpf_vitima+""
                    con = sqlite3.connect(caminho)
                    c = con.cursor()
                    c.execute(vsql5)
                    con.commit()
                    con.close()
                    if self.button =='ENVIAR':
                        sg.popup('TELEFONE ATUALIZADO COM SUCESSO!!')
                        proximo = True
                        janela.hide()
                else:
                    sg.popup('ESSE CPF NÃO ESTÁ CADASTRADO NO SISTEMA\nPOR FAVOR VERIFIQUE OS DADOS E TENTE NOVAMENTE!!!')
                    proximo =False
                    self.button,self.values = janela.read()
                    if self.button == "VOLTAR":
                        proximo =True                       
                        janela.hide()

            except:
                sg.popup('DADOS NÃO CORRESPONDEM!')
                proximo =False
                self.button,self.values = janela.read()
                if self.button == "VOLTAR":
                    proximo = True
                    janela.hide()
# ATUALIZA EMAIL ==============================================================================================================================================================================================
class atuaalizaemail():
    def __init__(self):
        global janela
        tela = [
            [sg.Image(filename="3.png",size=(450,87))],
            [sg.Text('CPF:')],
            [sg.Input(size=(20,0),key='cpf')],
            [sg.Text('NOVO EMAIL:')],
            [sg.Input(size=(30,0),key='email')],
            [sg.Text()],
            [sg.Button('ENVIAR'),sg.Button('VOLTAR')],
            [sg.Image(filename="atualizacao2.png",size=(450,87))]
        ]
        janela = sg.Window('ATUALIZAR EMAIL',size=(400,350)).layout(tela)
        self.button,self.values = janela.read()
    def inserirnobanco1(self):
        proximo = False
        if self.button =="VOLTAR":
            proximo = True
            janela.hide()
        while proximo != True:
            try:
                condicao = False
                cpf_vitima = self.values['cpf']
                novo_email = self.values['email']
                vsqlteste = "SELECT * from sistema"
                con = sqlite3.connect(caminho)
                c = con.cursor()
                c.execute(vsqlteste)
                resultado = c.fetchall()
                con.close()
                for c in resultado:
                    if  c[0] == int(cpf_vitima):
                        condicao = True
                if condicao:
                    vsql5 = "UPDATE sistema SET T_EMAILVITIMA = '"+novo_email+"' WHERE N_CPFVITIMA == "+cpf_vitima+""
                    con = sqlite3.connect(caminho)
                    c = con.cursor()
                    c.execute(vsql5)
                    con.commit()
                    con.close()
                    if self.button == 'ENVIAR':
                        sg.popup('EMAIL ATUALIZADO COM SUCESSO!!!')
                        proximo = True
                        janela.hide()
                else:
                    sg.popup('ESSE CPF NÃO ESTÁ CADASTRADO NO SISTEMA\nPOR FAVOR VERIFIQUE OS DADOS E TENTE NOVAMENTE!!')
                    proximo = False
                    self.button,self.values = janela.read()
                    if self.button == 'VOLTAR':
                        proximo = True
                        janela.hide()
            except:
                sg.popup('OS DADOS NÃO CORRESPONDEM!')
                proximo = False
                self.button,self.values = janela.read()
                if self.button == 'VOLTAR':
                    proximo = True
                    janela.hide()
# ATUALIZA TIPO ===============================================================================================================================================================================================
class atualizatipo():
    def __init__(self):
        global janela
        tela = [
            [sg.Image(filename="atualizacao1.png",size=(450,87))],
            [sg.Text('CPF PROPRIETARIO:')],
            [sg.Input(size=(20,0),key='cpf')],
            [sg.Text("COR:")],
            [sg.Combo(["AMARELO","AZUL","BRANCO","VERDE","ROXO","CIANO","PRETO","ROSA","VERMELHO","LARANJA","MARROM","LILÁS","LIMA","DOURADO","CARMESIM","CASTANHO","CINZA","BEGE"],key="cor",size=(29,1))],
            [sg.Text("MODELO:")],
            [sg.Combo(["SEM MODELO"],key="modelo",size=(29,1))],
            [sg.Text('NOVO TIPO:')],
            [sg.Combo(["CELULAR","RELOGIO","COMPUTADOR","NOOTBOOK","TABLET","FONE DE OUVIDO","BICICLETA","IMPRESSORA","TELEVISÃO","CAIXA DE SOM","RÁDIO","CÂMERA"],key="tipo",size=(29,1))],
            [sg.Button('ENVIAR'),sg.Button('VOLTAR')],
            [sg.Image(filename="atualizacao2.png",size=(450,87))]
        ]
        janela = sg.Window('ATUALIZAR TIPO',size=(400,350)).layout(tela)
        self.button,self.values = janela.read()
    def inserirnobanco2(self):
        proximo = False
        if self.button == 'VOLTAR':
            proximo = True
            janela.hide()
        while(proximo!= True):
            try:
                condicao = False
                cpf_pro = self.values['cpf']
                modelo = self.values['modelo']
                cor = self.values['cor']
                novo_tipo = self.values['tipo']
                vsqlteste = "SELECT * from sistema"
                con = sqlite3.connect(caminho)
                c = con.cursor()
                c.execute(vsqlteste)
                resultado = c.fetchall()
                con.close()
                for c in resultado:
                    if  c[0] == int(cpf_pro):
                        condicao = True
                if condicao:
                    vsql5 = "UPDATE pertences SET T_TIPODISPOSIVO = '"+novo_tipo+"' WHERE N_CPFPROPRIETARIO == '"+cpf_pro+"' AND T_MODELODISPOSITIVO ='"+modelo+"' AND T_CORDISPOSITIVO = '"+cor+"'"
                    con = sqlite3.connect(caminho)
                    c = con.cursor()
                    c.execute(vsql5)
                    con.commit()
                    if self.button == 'ENVIAR':
                        sg.popup('TIPO ATUALIZADO COM SUCESSO!!!')
                        proximo = True
                        janela.hide()
                else:
                    sg.popup('CPF NÃO ESTÁ CADASTRADO SISTEMA\nPOR FAVOR VERIFIQUE OS DADOS E TENTE NOVAMENTE!!')
                    proximo = False
                    self.button,self.values = janela.read()
                    if self.button == 'VOLTAR':
                        proximo = True
                        janela.hide()
            except:
                sg.popup("OS DADOS INFORMADOS NÃO CORRESPONDEM\n TENTE NOVAMENTE MAIS TARDE!!")
                proximo = False
                self.button,self.values = janela.read()
                if self.button == 'VOLTAR':
                    proximo = True
                    janela.hide()
# ATUALIZA MODELO =============================================================================================================================================================================================
class atualizamodelo():
    def __init__(self):
        global janela
        tela = [
            [sg.Image(filename="atualizacao1.png",size=(450,87))],
            [sg.Text('CPF PROPRIETARIO:')],
            [sg.Input(size=(20,0),key='cpf')],
            [sg.Text("TIPO:")],
            [sg.Combo(["CELULAR","RELOGIO","COMPUTADOR","NOOTBOOK","TABLET","FONE DE OUVIDO","BICICLETA","IMPRESSORA","TELEVISÃO","CAIXA DE SOM","RÁDIO","CÂMERA"],key="tipo",size=(29,1))],
            [sg.Text("COR:")],
            [sg.Combo(["AMARELO","AZUL","BRANCO","VERDE","ROXO","CIANO","PRETO","ROSA","VERMELHO","LARANJA","MARROM","LILÁS","LIMA","DOURADO","CARMESIM","CASTANHO","CINZA","BEGE"],key="cor",size=(29,1))],
            [sg.Text('NOVO MODELO:')],
            [sg.Combo(["SEM MODELO"],key="modelo",size=(29,1))],
            [sg.Button('ENVIAR'),sg.Button('VOLTAR')],
            [sg.Image(filename="atualizacao2.png",size=(450,87))]
        ]
        janela = sg.Window('ATUALIZAR MODELO',size=(400,350)).layout(tela)
        self.button,self.values = janela.read()
    def inserirnobanco2(self):
        proximo = False
        if self.button == 'VOLTAR':
            proximo = True
            janela.hide()
        while proximo!=True:
            try: 
                condicao = False
                cpf_pro = self.values['cpf']
                novo_modelo = self.values['modelo']
                cor = self.values["cor"]
                tipo = self.values["tipo"]
                vsqlteste = "SELECT * from sistema"
                con = sqlite3.connect(caminho)
                c = con.cursor()
                c.execute(vsqlteste)
                resultado = c.fetchall()
                con.close()
                for c in resultado:
                    if  c[0] == int(cpf_pro):
                        condicao = True
                if condicao:
                    vsql5 = "UPDATE pertences SET T_MODELODISPOSITIVO = '"+novo_modelo+"' WHERE N_CPFPROPRIETARIO == '"+cpf_pro+"' and T_CORDISPOSITIVO = '"+cor+"' and T_TIPODISPOSIVO = '"+tipo+"'"
                    con = sqlite3.connect(caminho)
                    c = con.cursor()
                    c.execute(vsql5)
                    con.commit()
                    if self.button == 'ENVIAR':
                        sg.popup('MODELO ATUALIZADO COM SUCESSO!!!')
                        proximo = True
                        janela.hide()
                else:
                    sg.popup('CPF NÃO ESTÁ CADASTRADO NO SISTEMA\nPOR FAVOR VERIFIQUE OS DADOS E TENTE NOVAMENTE!!!')
                    proximo = False
                    self.button,self.values = janela.read()
                    if self.button == 'VOLTAR':
                        proximo = True
                        janela.hide()
            except:
                sg.popup('OS DADOS INFORMADOS NÃO CORRESPONDEM\nTENTE NOVAMENTE MAIS TARDE!')
                proximo = False
                self.button,self.values = janela.read()
                if self.button == 'VOLTAR':
                    proximo = True
                    janela.hide()

# ATUALIZA COR ================================================================================================================================================================================================
class atualizacor():
    def __init__(self):
        global janela
        tela = [
            [sg.Image(filename="atualizacao1.png",size=(450,87))],
            [sg.Text('CPF PROPRIETARIO:')],
            [sg.Input(size=(20,0),key='cpf')],
            [sg.Text("TIPO:")],
            [sg.Combo(["CELULAR","RELOGIO","COMPUTADOR","NOOTBOOK","TABLET","FONE DE OUVIDO","BICICLETA","IMPRESSORA","TELEVISÃO","CAIXA DE SOM","RÁDIO","CÂMERA"],key="tipo",size=(29,1))],
            [sg.Text("MODELO:")],
            [sg.Combo(["SEM MODELO"],key="modelo",size=(29,1))],
            [sg.Text('NOVA COR:')],
            [sg.Combo(["AMARELO","AZUL","BRANCO","VERDE","ROXO","CIANO","PRETO","ROSA","VERMELHO","LARANJA","MARROM","LILÁS","LIMA","DOURADO","CARMESIM","CASTANHO","CINZA","BEGE"],key="cor",size=(29,1))],
            [sg.Button('ENVIAR'),sg.Button('VOLTAR')],
            [sg.Image(filename="atualizacao2.png",size=(450,87))]
        ]
        janela = sg.Window('ATUALIZAR COR',size=(400,350)).layout(tela)
        self.button,self.values = janela.read()
    def inserirnobanco2(self):
        proximo = False
        if self.button == 'VOLTAR':
            proximo = True
            janela.hide()
        while proximo != True:
            try:
                condicao = False
                cpf_pro = self.values['cpf']
                nova_cor = self.values['cor']
                modelo = self.values["modelo"]
                tipo = self.values['tipo']
                vsqlteste = "SELECT * from sistema"
                con = sqlite3.connect(caminho)
                c = con.cursor()
                c.execute(vsqlteste)
                resultado = c.fetchall()
                con.close()
                for c in resultado:
                    if  c[0] == int(cpf_pro):
                        condicao = True
                if condicao:
                    vsql5 = "UPDATE pertences SET T_CORDISPOSITIVO = '"+nova_cor+"' WHERE N_CPFPROPRIETARIO == '"+cpf_pro+"' and T_TIPODISPOSIVO = '"+tipo+"'and T_MODELODISPOSITIVO = '"+modelo+"'"
                    con = sqlite3.connect(caminho)
                    c = con.cursor()
                    c.execute(vsql5)
                    con.commit()
                    if self.button == 'ENVIAR':
                        sg.popup('COR ATUALIZADA COM SUCESSO!!!')
                        proximo = True
                        janela.hide()
                else:
                    sg.popup("CPF NÃO ESTÁ CADASTRADO NO SISTEMA\nPOR FAVOR VERIFIQUE OS DADOS E TENTE NOVAMENTE!!")
                    proximo = False
                    self.button,self.values = janela.read()
                    if self.button == 'VOLTAR':
                        proximo = True
                        janela.hide()
            except:
                sg.popup('OS DADOS INFORMADOS NÃO CORRESPONDEM\nTENTE NOVAMENTE MAIS TARDE!!')
                proximo = False
                self.button,self.values = janela.read()
                if self.button == 'VOLTAR':
                    proximo = True
                    janela.hide()
# CADASTRO DE PERTENCES =======================================================================================================================================================================================
class telacadastrodepertence():
    def __init__(self):
        global janela
        layout = [
            [sg.Image(filename="teste1.png",size=(450,87))],
            [sg.Text('CPF DO PROPRIETÁRIO',size=(50,0))],
            [sg.Input(size=(30,0),key='cpfpro')],
            [sg.Text('TIPO',size=(50,0))],
            [sg.Combo(["CELULAR","RELOGIO","COMPUTADOR","NOOTBOOK","TABLET","FONE DE OUVIDO","BICICLETA","IMPRESSORA","TELEVISÃO","CAIXA DE SOM","RÁDIO","CÂMERA"],key="tipo",size=(29,1))],
            [sg.Text('MODELO',size=(10,0))],
            [sg.Combo(["SEM MODELO"],key="modelo",size=(29,1))],
            [sg.Text('COR',size=(50,0))],
            [sg.Combo(["AMARELO","AZUL","BRANCO","VERDE","ROXO","CIANO","PRETO","ROSA","VERMELHO","LARANJA","MARROM","LILÁS","LIMA","DOURADO","CARMESIM","CASTANHO","CINZA","BEGE"],key="cor",size=(29,1))],
            [sg.Button('CADASTRAR DADOS'),sg.Button("VOLTAR PARA O MENU")],
            [sg.Image(filename="teste3.png",size=(450,87))]
        ]
        janela = sg.Window("CADASTRO DOS PERTENCES",size=(400,390)).layout(layout)
        self.button,self.values = janela.read()
        
    def inserirnobanco(self):
        proximo = False
        if self.button == "VOLTAR PARA O MENU":
            proximo = True
            janela.hide()
        while (proximo!=True):
            try:
                condicao = False
                cpf_proprietario = self.values['cpfpro']
                tipo = self.values['tipo']
                modelo = self.values['modelo']
                cor = self.values["cor"]
                vsqlteste = "SELECT * from sistema"
                con = sqlite3.connect(caminho)
                c = con.cursor()
                c.execute(vsqlteste)
                resultado = c.fetchall()
                con.close()
                for c in resultado:
                    if  c[0] == int(cpf_proprietario):
                        condicao = True
                        
                if condicao:
                    vsql1 = "INSERT INTO pertences (N_CPFPROPRIETARIO,T_TIPODISPOSIVO,T_MODELODISPOSITIVO,T_CORDISPOSITIVO)VALUES('"+cpf_proprietario+"','"+tipo+"','"+modelo+"','"+cor+"')"
                    con = sqlite3.connect(caminho)
                    c = con.cursor()
                    c.execute(vsql1)
                    con.commit()
                    con.close()
                    if self.button == 'CADASTRAR DADOS':
                        sg.popup_ok('PERTENCE CADASTRADO COM SUCESSO!!')
                        janela.hide()
                        proximo = True
                else:
                    sg.popup('CPF NÃO ESTÁ CADASTRADO NO SISTEMA\nPARA ALOCAR UM OBJETO NESSE CPF PRIMEIRO É PRECISO CADASTRÁ-LO')
                    proximo = False
                    self.button,self.values = janela.read()
                    if self.button == "VOLTAR PARA O MENU":
                        janela.hide()
                        proximo = True
                        
            except:
                sg.popup('OS DADOS INFORMADOS NÃO CORRESPODEM!!')
                proximo = False
                self.button,self.values = janela.read()
                if self.button == "VOLTAR PARA O MENU":
                    janela.hide()
                    proximo = True
        
# TELA ATUALIZAR DADOS DAS VITIMAS=============================================================================================================================================================================
class telaatualizardadosdavitima():
    def __init__(self):
        global janela
        layout = [
            [sg.Image(filename="teste2.png",size=(450,87))],
            [sg.Text()],
            [sg.Button("ATUALIZAR TELEFONE",size=(50,2),pad=((10,10),(3,0)))],
            [sg.Button("ATUALIZAR EMAIL",size=(50,2),pad=((10,10),(20,30)))],
            
        ]
        janela = sg.Window("ATUALIZAÇÃO DE DADOS",size=(400,350)).layout(layout)
        self.button,self.values = janela.read()

    def inserirnobanco(self):
            if self.button == "ATUALIZAR TELEFONE":
                janela.hide()
                atualiza_telefone = atuaalizatelefone()
                atualiza_telefone.inserirnobanco1()

            elif self.button == "ATUALIZAR EMAIL":
                janela.hide()
                atualiza_email = atuaalizaemail()
                atualiza_email.inserirnobanco1()
#TELA ATUALIZAR DADOS DO OBJETO================================================================================================================================================================================
class telaatualizardadosdoobjeto():
    def __init__(self):
        global janela
        layout = [
            [sg.Image(filename="atualizacao1.png",size=(450,78))],
            [sg.Button("ATUALIZAR TIPO",size=(50,2),pad=((10,10),(3,0)))],
            [sg.Button("ATUALIZAR MODELO",size=(50,2),pad=((10,10),(10,0)))],
            [sg.Button("ATUALIZAR COR",size=(50,2),pad=((10,10),(10,0)))],
            [sg.Image(filename="atualizacao2.png",size=(450,87))]
        ]
        janela = sg.Window("ATUALIZAÇÃO DE DADOS",size=(400,350)).layout(layout)
        self.button,self.values = janela.read()
    def inserirnobanco(self):
        if self.button == "ATUALIZAR TIPO":
            janela.hide()
            atualiza_tipo = atualizatipo()
            atualiza_tipo.inserirnobanco2()
        elif self.button == "ATUALIZAR MODELO":
            janela.hide()
            atualiza_modelo = atualizamodelo()
            atualiza_modelo.inserirnobanco2()
        elif self.button == "ATUALIZAR COR":
            janela.hide()
            atualiza_cor = atualizacor()
            atualiza_cor.inserirnobanco2()
# TELA OBJETOS ACHADOS ========================================================================================================================================================================================
class telaobjetosachados:
    def __init__(self):
        global janela
        layout = [
            [sg.Text('TIPO',size=(10,0))],
            [sg.Combo(["CELULAR","RELOGIO","COMPUTADOR","NOOTBOOK","TABLET","FONE DE OUVIDO","BICICLETA","IMPRESSORA","TELEVISÃO","CAIXA DE SOM","RÁDIO","CÂMERA"],key="tipo",size=(29,1))],
            [sg.Text('MODELO',size=(10,0))],
            [sg.Combo(["SEM MODELO"],key="modelo",size=(29,1))],
            [sg.Text('COR')],
            [sg.Combo(["AMARELO","AZUL","BRANCO","VERDE","ROXO","CIANO","PRETO","ROSA","VERMELHO","LARANJA","MARROM","LILÁS","LIMA","DOURADO","CARMESIM","CASTANHO","CINZA","BEGE"],key="cor",size=(29,1))],
            [sg.Button('CONSISTIR'),sg.Button('VOLTAR PARA MENU')],
            [sg.Image(filename="teste3.png",size=(450,87))]    
        ]
        janela = sg.Window('OBJETO ACHADOS',size=(400,300)).layout(layout)
        self.button,self.values = janela.read()
    def enviaremail(self):
        proximo = False
        if self.button == 'VOLTAR PARA MENU':
            proximo = True
            janela.hide()
        while proximo!=True:
            try:
                tipo = self.values['tipo']
                modelo = self.values['modelo']
                cor = self.values['cor']
                vsql6 = "SELECT * FROM pertences WHERE T_TIPODISPOSIVO ='"+tipo+"'AND T_MODELODISPOSITIVO = '"+modelo+"' AND T_CORDISPOSITIVO = '"+cor+"'"
                con = sqlite3.connect(caminho)
                c = con.cursor()
                c.execute(vsql6)
                resultado = c.fetchall()
                for r in resultado:
                    res = list(r)
                    cpf1 = res[0]
                    con.close()
                    vsql7 ="SELECT * FROM sistema WHERE N_CPFVITIMA == '"+str(cpf1)+"'"
                    con = sqlite3.connect(caminho)
                    c = con.cursor()
                    c.execute(vsql7)
                    result = c.fetchall()
                    for i in result:
                        f = list(i)
                        c = f[2]
                    sg.popup_auto_close('AGUARDE ENQUANTO PROCURAMOS POR VÍTIMAS NO BANCO..................')
                    #configurar conta e senha========================================================================================
                    account_sid = "ACc5e104a1f83bc4ad8a039af6e986d1b6"
                    auth_token = "cecdb350f8df52037882b674793da28a"
                    # criar um sms==================================================================================================
                    client = Client(account_sid, auth_token)
                    #enviar um sms===================================================================================================
                    client.messages.create(from_="+13133970035", body="Óla compareça à deleagacia na qual você fez o boletim de ocorrência\nEncontramos um objeto com características semelhantes às suas! ", to= c)
                    con.close()
                if self.button == 'CONSISTIR':
                    if tipo == '' or modelo == '' or cor == '':
                        sg.popup("CAMPOS FALTANDO!")
                        proximo = False
                        self.button,self.values = janela.read()
                    else:
                        sg.popup('AS VÍTIMAS SERÃO INFORMADAS POR SMS!')
                        proximo = True
                        janela.hide()
                elif self.button == 'VOLTAR PARA MENU':
                    proximo = True
                    janela.hide()

            except:
                sg.popup('DADOS NÃO CORRESPODEM!!')
                proximo = False
                self.button,self.values = janela.read()
                if self.button == "VOLTAR PARA MENU":
                    proximo = True
                    janela.hide()
class deletar():
    def __init__(self):
        global janela
        layout = [
            [sg.Text('CPF DA VÍTIMA')],
            [sg.Input(size=30,key='cpf')],
            [sg.Button('EXCLUIR'),sg.Button('VOLTAR PARA MENU')],
            [sg.Image(filename='4.png')]
        ]
        janela = sg.Window("EXCLUIR USUÁRIOS",size=(450,200)).layout(layout)
        self.button,self.values = janela.read()           
    def excluirdobanco(self):
        proximo = False
        if self.button == 'VOLTAR PARA MENU':
            proximo = True
            janela.hide()
        while proximo!=True:
            try:
                condicao = False
                cpf = self.values['cpf']
                vsqlteste = "SELECT * from sistema"
                con = sqlite3.connect(caminho)
                c = con.cursor()
                c.execute(vsqlteste)
                resultado = c.fetchall()
                con.close()
                for c in resultado:
                    if  c[0] == int(cpf):
                        condicao = True
                if condicao:
                    vsql00 = "DELETE FROM sistema where N_CPFVITIMA =='"+cpf+"'"
                    vsql01 = "DELETE FROM pertences where N_CPFPROPRIETARIO =='"+cpf+"'"
                    con = sqlite3.connect(caminho)
                    c = con.cursor()
                    c.execute(vsql00)
                    con.commit()
                    con.close()
                    con = sqlite3.connect(caminho)
                    c = con.cursor()
                    c.execute(vsql01)
                    con.commit()
                    con.close()
                    if self.button == 'EXCLUIR':
                        sg.popup('OS DADOS DA VÍTIMA FORAM EXCLUIDOS COM SUCESSO!!')
                        proximo = True
                        janela.hide()
                else:
                    sg.popup('O CPF INFORMADO NÃO SE ENCONTRA NO BANCO DE DADOS!')
                    proximo = False
                    self.button,self.values = janela.read()
                    if self.button == "VOLTAR PARA MENU":
                        proximo = True
                        janela.hide() 

            except:
                sg.popup('OS DADOS INFORMADOS NÃO CORRESPONDEM\nTENTE NOVAMENTE!')
                proximo = False
                self.button,self.values = janela.read()
                if self.button == "VOLTAR PARA MENU":
                    proximo = True 
class deletarobjeto:
    def __init__(self):
        global janela
        layout = [
            [sg.Text('CPF DA VÍTIMA')],
            [sg.Input(size=30,key='cpf')],
            [sg.Text('TIPO DE DISPOSITIVO: ')],
            [sg.Combo(["CELULAR","RELOGIO","COMPUTADOR","NOOTBOOK","TABLET","FONE DE OUVIDO","BICICLETA","IMPRESSORA","TELEVISÃO","CAIXA DE SOM","RÁDIO","CÂMERA"],key="tipo",size=(29,1))],
            [sg.Text('MODELO DO DISPOSITIVO:')],
            [sg.Combo(["SEM MODELO"],key="modelo",size=(29,1))],
            [sg.Text('COR DO DISPOSITIVO:')],
            [sg.Combo(["AMARELO","AZUL","BRANCO","VERDE","ROXO","CIANO","PRETO","ROSA","VERMELHO","LARANJA","MARROM","LILÁS","LIMA","DOURADO","CARMESIM","CASTANHO","CINZA","BEGE"],key="cor",size=(29,1))],
            [sg.Button('EXCLUIR'),sg.Button('VOLTAR PARA MENU')] 
        ]
        janela = sg.Window("EXCLUIR OBJETOS",size=(450,260)).layout(layout)
        self.button,self.values = janela.read()           
    def excluirdobanco(self):
        proximo = False
        if self.button == 'VOLTAR PARA MENU':
            proximo = True
            janela.hide()
        while proximo!=True:
            try:
                condicao = False
                cpf = self.values['cpf']
                tipo = self.values['tipo']
                modelo = self.values['modelo']
                cor = self.values['cor']
                vsqlteste = "SELECT * from sistema"
                con = sqlite3.connect(caminho)
                c = con.cursor()
                c.execute(vsqlteste)
                resultado = c.fetchall()
                con.close()
                for c in resultado:
                    if  c[0] == int(cpf):
                        condicao = True
                if condicao:
                    vsql00 = "DELETE FROM pertences where N_CPFPROPRIETARIO =='"+cpf+"'AND T_TIPODISPOSIVO == '"+tipo+"' AND T_MODELODISPOSITIVO ='"+modelo+"' AND T_CORDISPOSITIVO = '"+cor+"'"
                    con = sqlite3.connect(caminho)
                    c = con.cursor()
                    c.execute(vsql00)
                    con.commit()
                    con.close()
                    if self.button == 'EXCLUIR':
                        sg.popup('OS OBJETOS FORAM EXCLUIDOS COM SUCESSO!!')
                        proximo = True
                        janela.hide()
                else:
                    sg.popup('O CPF INFORMADO NÃO SE ENCONTRA NO BANCO DE DADOS!')
                    proximo = False
                    self.button,self.values = janela.read()
                    if self.button == "VOLTAR PARA MENU":
                        proximo = True
                        janela.hide()

            except:
                sg.popup('OS DADOS INFORMADOS NÃO CORRESPONDEM\nTENTE NOVAMENTE!')
                proximo = False
                self.button,self.values = janela.read()
                if self.button == "VOLTAR PARA MENU":
                    proximo = True
                    janela.hide()
class informacaovitima:
    def __init__(self):
        sg.theme('BrownBlue')
        layout = [
            [sg.Text('CPF')],
            [sg.Input(size=(20,0),key='cpf'),sg.Button('BUSCAR'),sg.Button('MENU')],
            [sg.Output(size=(60,50))]
        ]
        self.janela = sg.Window("CONSULTA DE VITIMAS",size=(400,350)).layout(layout)
    def buscar(self):
        proximo = False
        while proximo!=True:
            self.Button,self.values = self.janela.read()
            if self.Button == 'MENU':
                self.janela.hide()
                break
            try:    
                cpf = self.values['cpf']
                vsqlteste = "SELECT * from sistema"
                con = sqlite3.connect(caminho)
                c = con.cursor()
                c.execute(vsqlteste)
                resultado = c.fetchall()
                con.close()
                for c in resultado:
                    if  c[0] == int(cpf):
                        condicao = True
                if condicao:
                    vsql1 = "SELECT * FROM sistema where N_CPFVITIMA == "+cpf+""
                    con = sqlite3.connect(caminho)
                    c= con.cursor()
                    c.execute(vsql1)
                    usuario = c.fetchall()
                    con.close()
                    res = list(usuario[0])
                    print('                               DADOS DA VÍTIMA')
                    print()
                    print("CPF.......: "+ str(res[0]).upper())
                    print("-"*80)
                    print("NOME......: "+ str(res[1]).upper())
                    print("-"*80)
                    print("TELEFONE..: "+ str(res[2]).upper())
                    print("-"*80)
                    print("EMAIL.....: "+ str(res[3]).upper())
                    print("-"*80)
                    print("SEXO......: "+ str(res[4]).upper())
                    print("-"*80)
                    print("NASCIMENTO: "+ str(res[5])+"\ "+res[6]+"\ "+str(res[7]))
                    proximo = False
            except:
                sg.popup('OS DADOS INFORMADOS NÃO ESTÃO NO NOSSO BANCO DE DADOS\nVERIFIQUE E TENTE NOVAMENTE!')
                proximo = False
class objetosdavitima:
    def __init__(self):
        sg.theme('BrownBlue')
        layout = [
            [sg.Text('CPF')],
            [sg.Input(size=(20,0),key='cpf'),sg.Button('BUSCAR'),sg.Button('MENU')],
            [sg.Output(size=(60,50))]
        ]
        self.janela = sg.Window("CONSULTA DE OBJETOS",size=(400,350)).layout(layout)
    def buscar(self):
        proximo =False
        while proximo!=True:
            self.Button,self.values = self.janela.read()
            if self.Button == 'MENU':
                self.janela.hide()
                break
            try:
                cpf = self.values['cpf']
                vsqlteste = "SELECT * from sistema"
                con = sqlite3.connect(caminho)
                c = con.cursor()
                c.execute(vsqlteste)
                resultado = c.fetchall()
                con.close()
                for c in resultado:
                    if  c[0] == int(cpf):
                        condicao = True
                if condicao:
                    vsql2 = "SELECT * FROM pertences where N_CPFPROPRIETARIO == "+cpf+""
                    con = sqlite3.connect(caminho)
                    c= con.cursor()
                    c.execute(vsql2)
                    usuario = c.fetchall()
                    con.close()
                    res = list(usuario)
                    
                    print('                               OBJETOS DA VÍTIMA')
                    cont =0
                    for c in res:
                        print("="*43)
                        x = list(c)
                        print("##OBJETO "+str((cont+1)))
                        print()
                        print("TIPO......: "+ (x[1]))
                        print("-"*85)
                        print("MODELO..: "+ (x[2]))
                        print("-"*85)
                        print("COR.....: "+ (x[3]))
                        cont+=1
                proximo = False
            except:
                sg.popup('OS DADOS INFORMADOS NÃO ESTÃO NO NOSSO BANCO DE DADOS\n VERIFIQUE E TENTE NOVAMENTE!!')
                proximo = False

# TELA DE LOGIN

def iniciar_sesion(user,nip):
    global res
    if(user =='' or nip ==''):
        res =''
        sg.popup_error("CAMPOS FALTANDO")
    else:
        if(user == 'caio.matos' and nip == 'infor@mpl'):
            res = "liberado"
        else:
            res = ''
            sg.popup_error('USUARIO E SENHA INCORRETOS!')
        return res

layout = [
    [sg.Image(filename='images.png', pad=((40, 40), (3, 10)))],
    [sg.Text('Usuario:', size=(100,1), justification='center')],
    [sg.InputText('', pad=((0,0), (0,10)),key='user')],
    [sg.Text('Senha', size=(100,1),justification='center')],
    [sg.InputText('', password_char='*', key='nip')],
    [sg.Button('login in', key='login'),sg.Button('Sair',key='close')]
]
window = sg.Window('Login',layout, size=(350,350))
res = 0
while (res !='liberado'):
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'close':
        break
    elif (event == 'login'):
        iniciar_sesion(values['user'],values['nip'])

if res == 'liberado':
    window.hide()

#LOOP PRINCIPAL DO PROGRAMA ===================================================================================================================================================================================
resultado ='0'
while resultado != '10':
    tela = Telamenuprincipal()
    if tela.button == sg.WINDOW_CLOSED:
        break
    resultado = tela.iniciar()
    if resultado == '1':
        usuario = telacadastrousuario()
        if usuario.button == sg.WINDOW_CLOSED:
            break
        usuario.inserirnobanco()
    elif resultado == '2':
        pertence = telacadastrodepertence()
        if pertence.button == sg.WINDOW_CLOSED:
            break
        pertence.inserirnobanco()
    elif resultado == '3':
        atualiza = telaatualizardadosdavitima()
        if atualiza.button == sg.WINDOW_CLOSED:
            break
        atualiza.inserirnobanco()
    elif resultado == '4':
        atualiza2 = telaatualizardadosdoobjeto()
        if atualiza2.button == sg.WIN_CLOSED:
           break
        atualiza2.inserirnobanco() 
    elif resultado == '6':
        objeto = telaobjetosachados()
        if objeto.button == sg.WIN_CLOSED:
            break
        objeto.enviaremail()
    elif resultado == '5':
        exclui = deletar()
        if exclui.button == sg.WIN_CLOSED:
            break
        exclui.excluirdobanco()
    elif resultado == '7':
        del_object = deletarobjeto()
        if del_object.button == sg.WIN_CLOSED:
            break
        del_object.excluirdobanco()
    elif resultado == '8':
        infor = informacaovitima()
        infor.buscar()
        if infor.Button == sg.WIN_CLOSED:
            break
    elif resultado == '9':
        inforobject = objetosdavitima()
        inforobject.buscar()
        if inforobject.Button == sg.WIN_CLOSED:
            break
        
