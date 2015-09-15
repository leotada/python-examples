#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2015 Leonardo <leonardo_tada@hotmail.com>
#  Programa para agendamento de desligamento do computador
#  Roda em Python 2, 3, Windows e Linux

import subprocess
import sys
import os

# Compatibilidade
plataforma = os.name
PY2 = sys.version_info[0] < 3
if PY2:
    from Tkinter import *
    input = raw_input
else:
    from tkinter import *


class GUI(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.initUI()
        
    def cancelar(self):
        if plataforma == 'nt':
            subprocess.Popen(['shutdown', '-a'])
        else:
            subprocess.Popen(['shutdown', '-c'])
        
    def desligar(self):
        t = int(self.entry.get())
        if plataforma == 'nt':
            t = str(t*60)
            if self.force.get():
                subprocess.Popen(['shutdown', '-s', '-f', '-t', t])
            else:
                subprocess.Popen(['shutdown', '-s', '-t', t])
        else:
            t = str(t)
            if self.force.get():
                subprocess.Popen(['shutdown', '-h', '-f', t])
            else:
                subprocess.Popen(['shutdown', '-h', t])


    def initUI(self):
        self.window.title("Desligar")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)
        self.pack(fill=BOTH, expand=1)

        botao_iniciar = Button(frame, text='Desligar', width=23, command=self.desligar)
        botao_iniciar.grid(row=1, column=1, sticky=W, columnspan=2)
        botao_cancelar = Button(frame, text='Cancelar', width=23, command=self.cancelar)
        botao_cancelar.grid(row=2, column=1, sticky=W, columnspan=2)
        self.entry = Spinbox(frame, values=(1,5,15,30,60,90,120), width=10)
        self.force = IntVar()
        self.ckforce = Checkbutton(frame, text='Forçar', variable=self.force)
        self.entry.grid(row=3, column=1, sticky=W)
        self.ckforce.grid(row=3, column=2, sticky=W)


def main():
    root = Tk()
    root.geometry()  # "1000x600+300+300"
    GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
