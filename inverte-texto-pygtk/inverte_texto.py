#!/usr/bin/python

# Inversor de texto com interface gráfica feita com GTK 2 usando Pygtk e a ferramenta Glade 3.8 para GTK+2.

import pygtk
pygtk.require('2.0')
import gtk
import sys

#Arquivo glade, pode ser editado com o Glade.
UI_FILE = "inverte_texto.ui"

class GUI:
    def __init__(self):
        self.builder = gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)

        window = self.builder.get_object('window')
        self.campo = self.builder.get_object('entry1')

        window.show_all()

    def botao_inverter(self, botao):
        texto = self.campo.get_text()
        self.inverte(texto)
        
    def inverte(self, texto):
        final = texto[::-1]
        self.campo.set_text(final)
                
    def sair(window, self):
        gtk.main_quit()
    
    def destroy(window, self):
        gtk.main_quit()


def main():
    app = GUI()
    gtk.main()
        
if __name__ == "__main__":
    sys.exit(main())
