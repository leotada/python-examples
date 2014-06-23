#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 2 - Criado por Leonardo Tada - 12/04/2012
import sys, os
from datetime import datetime

pasta = 'c:'
#print(os.path.isfile('caixa.txt'))

def main():
    dinheiro(preco())
    
def preco():
    while 1:
        preco = raw_input('Preço: ')
        try:
            preco = preco.replace(',','.')
            preco = eval(preco)
            print(preco)
            preco = float(preco)
            return(preco)
            break
        except:
            if (preco=='c') or (preco=='cancelar'):
                continue
            elif (preco=='f') or (preco=='fechar'):
                fechar_caixa()
            elif (preco=='s') or (preco=='sair'):
                sair()
            else: continue
        
def dinheiro(preco):
    arq = open(pasta+'entrada.txt', 'a')
    texto = []
    while 1:
        dinheiro = raw_input('Dinheiro: ')
        try:
            dinheiro = float(dinheiro)
            if (dinheiro < preco):
                print('%.2f, falta dinheiro.' % (dinheiro-preco))
                continue
            break
        except:
            if (dinheiro=='c') or (dinheiro=='cancelar'):
                main()
            elif (preco=='f') or (preco=='fechar'):
                fechar_caixa()
            elif (dinheiro=='s') or (dinheiro=='sair'):
                sair()
            else: continue
    troco = dinheiro - preco
    print('Troco: %.2f\n' % troco)
    texto.append('%s\n' % preco)
    arq.writelines(texto)
    arq.close()
    main()
    
def sair():
    sys.exit(0)
    
def fechar_caixa():
    d = raw_input('Deseja fechar o caixa: s/n? ')
    if (d == 's'):
        lido = []
        soma = 0
        arq = open(pasta+'entrada.txt', 'r')
        arq2 = open(pasta+'fechamento.txt', 'a')
        lido = arq.readlines()
        for linha in lido:
            print(linha)
            soma = soma+float(linha)
        total = 'Total: R$'+str(soma) 
        print(total)
        #data e hora
        today = datetime.now()
        data = today.strftime("%d/%m/%y")
        hora = today.strftime("%I:%M%p")
        data = '\n'+data+'--'+hora
        print(data)
        #salva
        arq2.writelines(data+' - '+total)
        arq2.close()
        arq.close()
        #limpa arquivo
        arq = open(pasta+'entrada.txt', 'w')
        arq.close()
    else: main()
    
if __name__ == "__main__":
    main()
