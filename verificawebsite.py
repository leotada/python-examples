# Python 3 - Verifica disponibilidade de sites
# verifica conexao com um teste que sempre esta online e armazena log em um arquivo de texto.

from urllib.request import Request, urlopen
from urllib.error import URLError
from datetime import datetime
import time


class Url(object):
    def __init__(self, url, nome):
        self.url = url
        self.sucesso = 0
        self.erro = 0
        self.nome = nome
        self.teste = False  # se passou no teste

tempo = 120  # verificar a cada quanto tempo, segundos.
url0 = Url('http://www.google.com', 'teste')
url1 = Url('http://uol.com.br', 'Site 1')
url2 = Url('http://baixaki.com.br', 'Site 2')
urls = [url0, url1, url2]  # Quais vai testar

while True:
    for url in urls:
        try:
            response = urlopen(url.url)
            if response.info():
                url.teste = True
                url.sucesso += 1
            else:
                url.teste = False
                url.erro += 1
        except URLError:
            url.teste = False
            url.erro += 1
        #print(url.nome + ' - ' + url.teste)
        if url.nome == 'teste' and not url.teste:  # se o teste nao passar, break
            texto = '\nSem conexao local com a internet.'
            arq = open('log-status.txt', 'a')
            arq.write(texto)
            arq.close()
            print(texto)
            break
        elif url.nome != 'teste':  # se nao for o link teste, escreve
            texto = url.nome + ' - Sucessos: '+ str(url.sucesso) + \
                    ' - Erros: '+ str(url.erro) + ' - ' + str(datetime.now())+'\n'
            arq = open('log-status.txt', 'a')
            arq.write(texto)
            arq.close()
            print(texto)
            time.sleep(1)
    time.sleep(tempo)
  
