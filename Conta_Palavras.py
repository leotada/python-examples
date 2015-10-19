#!/usr/bin/env python3
import os
from sys import argv
import re
from collections import Counter

def contar(entrada):
    texto=re.findall('\w(?:[-\w]*\w)?', entrada.lower())
    contaPalavras=Counter(texto).most_common()
    return contaPalavras

def ProcessaTxt(arquivos):
    for arquivo in arquivos:
        if os.path.isfile(arquivo):
            texto=open(arquivo, 'r').read()
            resultado=open('RESULTADO - '+arquivo, 'w+')
            for palavra, quantidade in contar(texto):
                resultado.write('%s -- %s\n' % (palavra, quantidade))
            print('O arquivo com os resultados do arquivo %s ja foi salvo!' % arquivo)
        else:
            print('Ou não existe ou não é um arquivo.')


def main():
    if len(argv) > 1:
        ProcessaTxt(argv[1:])
    else:
        print('Uso: Conta_Palavras arquivo1.txt arquivo2.txt ...')

if __name__ == '__main__':
    main()
