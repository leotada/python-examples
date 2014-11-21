# -*- coding: utf-8 -*-
# Python 3
# Copia arquivo se a data de modificacao for mais nova ou não existir outro arquivo no lugar.

import os
import sys
import shutil


class File(object):
    def __init__(self, path):
        self.path = os.path.join(*os.path.splitdrive(path))
        self.mtime = os.stat(path).st_mtime

try:
    fileNew = File('//SERVIDOR/ftp/Leonardo/Arquivo.xml')
    dest = File('C:/Users/leonardo/Desktop')
except:  # Nao tem arquivo novo para copiar
    sys.exit(0)

try:  # Compara data dos arquivos
    fileOld = File('C:/Users/leonardo/Desktop/Arquivo.xml')
    if fileNew.mtime > fileOld.mtime:
        shutil.copy2(fileNew.path, dest.path)
except:  # Nao tem arquivo antigo para comparar data, copia direto
    shutil.copy2(fileNew.path, dest.path)
