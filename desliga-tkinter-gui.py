#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2014 Leonardo <leonardo_tada@hotmail.com>

import subprocess
import sys
from tkinter import *

# Compatibilidade
PY2 = sys.version_info[0] < 3
if PY2:
    input = raw_input


class GUI(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.initUI()
        
    def cancelar(self):
        subprocess.Popen(['shutdown', '-a'])
        
    def desligar(self):
        t = int(self.entry.get())
        t = str(t*60)
        if self.force.get():
            subprocess.Popen(['shutdown', '-s', '-f', '-t', t])
        else:
            subprocess.Popen(['shutdown', '-s', '-t', t])

    def initUI(self):
        self.window.title("Desligar")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)
        self.pack(fill=BOTH, expand=1)

        botao_iniciar = Button(frame, text='Desligar', width=23, command=self.desligar)
        botao_iniciar.grid(row=1, column=1, sticky=W, columnspan=2)
        botao_cancelar = Button(frame, text='Cancelar', width=23, command=self.cancelar)
        botao_cancelar.grid(row=2, column=1, sticky=W, columnspan=2)
        self.entry = Spinbox(frame, values=(0,1,5,15,30,60,90,120), width=10)
        self.force = IntVar()
        self.ckforce = Checkbutton(frame, text='Forçar', variable=self.force)
        self.entry.grid(row=3, column=1, sticky=W)
        self.ckforce.grid(row=3, column=2, sticky=W)


def main():
    root = Tk()
    root.geometry()
    GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
