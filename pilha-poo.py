#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system


class Cliente(object):  # Classe cliente, vazia pois pode ser atribuido
    pass                                        # propriedades mais tarde


class Pilha(object):  # Classe Pilha

    def __init__(self):  # metodo construtor
        self.pilha = []  # declara lista vazia sendo propriedade da classe

    def incluir(self):
        "Inclui um cliente na pilha"
        cliente = Cliente()  # instancia objeto cliente
        cliente.nome = raw_input('Nome: ')  # inclui propriedade nome no objeto com valor digitado
        cliente.telefone = raw_input('Telefone: ')  # inclui propriedade nome no objeto com valor digitado
        cliente.cpf = raw_input('CPF: ')  # inclui propriedade cpf no objeto com valor digitado
        self.pilha.insert(0, cliente)  # insere sempre na primeira posicao

    def consultar(self):
        "Lista todos os items"
        for item in self.pilha:  # faz uma iteracao em todos os items da lista
            print '\nNome: ' + item.nome
            print 'Telefone: ' + item.telefone
            print 'CPF: ' + item.cpf
        raw_input()  # aguarda tecla enter

    def excluir(self):
        "Exclui o primeiro item da lista"
        if len(self.pilha) > 0:  # pega tamanho da pilha e compara
            self.pilha.pop(0)  # exclui item da posicao 0
            print 'Excluido'
        else: print 'Pilha vazia'
        raw_input()  # aguarda tecla enter


def main():

    def limpa():
        "Limpa a tela"
        system('cls')

    p = Pilha()  # instancia objeto Pilha atribuindo para p
    while True:  # loop infinito, sempre verdadeiro
        limpa()
        print("\n1. Incluir: ")
        print("\n2. Consultar: ")
        print("\n3. Excluir: ")
        print("\n4. Sair: \n")
        try:  # tenta fazer
            op = int(raw_input())  # pega a entrada do teclado e converte para int
            if op == 1:       # caso der erro na conversao cai no except abaixo
                limpa()
                p.incluir()  # chama metodo incluir do objeto p (pilha)
            elif op == 2:
                limpa()
                p.consultar()  # chama metodo consultar do objeto p (pilha)
            elif op == 3:
                limpa()
                p.excluir()  # chama metodo excluir do objeto p (pilha)
            elif op == 4:
                break  # quebra o loop e fecha o programa
            else:
                print 'Opcao invalida'
        except:  # caso tenha execao, (por exemplo digitar uma letra) sera exec
            print 'Opcao invalida, digite um numero'

main()  # chama o main, primeira funcao a ser executada
