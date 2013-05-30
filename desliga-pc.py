#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Agenda o desligamento do computador em quantos minutos desejados, para Windows.  


import os

def main():
    x = raw_input('1. Desligar\n2. Cancelar Desligamento\n3. Fechar\n')
    if x == '1':
        desligar()
    elif x == '2':
        cancelar()
    elif x == '3':
        exit()
    else:
        print('Opção inválida!')
        
def cancelar():
    comando('shutdown -a')
    
def desligar():
    t = int(raw_input('Quantos minutos para desligar:\n'))
    t = str(t*60)
    cmd = 'shutdown -s -f -t ' + (t)
    comando(cmd)
    
def comando(cmd):
    os.system(cmd)

    
if __name__ == '__main__':
    main()
