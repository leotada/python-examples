# -*- coding: utf-8 -*-
#
# Minha versão em Python da música da Xuxa, Cinco Patinhos, retirado deste blog de um amigo feito em C#
# http://techblog.desenvolvedores.net/2012/03/03/xuxa-para-programadores/


def quack():
    "Repete qua! 4 vezes"
    print 'quá! ' * 4

patos = 5
while patos > 0:
    print str(patos) + (' patinhos foram passear' if patos != 1 else ' patinho foi passear')
    print 'além das montanhas para brincar'
    print 'A mamãe gritou'
    patos -= 1
    quack()
    if patos >= 1:
        print 'Mas só ' + str(patos) + (' patinhos voltaram de lá.\n' if patos != 1 else ' patinho voltou de lá.\n')
    else:
        print 'Mas nenhum patinho voltou de lá.\n'

print '\nA mamãe patinha foi procurar'
print 'Além das motanhas'
print 'Na beira do mar'
print 'A mamãe gritou'
quack()
print 'E os 5 patinhos voltaram de lá.'
input()  # Apenas para deixar na tela ao acabar
