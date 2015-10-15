#!/usr/bin/env python
# *-* coding: utf-8 *-*
#
# Leonardo Tada - leonardo_tada@hotmail.com - 2012
#
#bugs conhecidos: uma palavra 'pouco' para cafe e leite ou uma palavra 'muito' para cafe e leite
print('Seja bem-vindo!')
frase = input('Que tipo de café você gosta?\n')
cafe = frase.find('cafe')
leite = frase.find('leite')
pouco = frase.find('pouco')
muito = frase.find('muito')
metade = frase.find('metade')
#debug
#print('cafe: %s, leite: %s' % (cafe, leite))
#print('pouco: %s, muito: %s' % (pouco, muito))

if cafe >= 0:   #Se encontrar 'cafe' na frase
	#subtrai o menor do maior
	#pouco
	if cafe > pouco:
		p = cafe-pouco
	else:
		p = pouco-cafe
	#muito
	if cafe > muito:
		m = cafe-muito
	else:
		m = muito-cafe
	#define
	if p < m:
		cafe = 'pouco'
	elif m < p:
		cafe = 'muito'
	else:
		cafe = 'cafe'
else:
	cafe = -1

if leite >= 0:   #Se encontrar 'leite' na frase
	#pouco
	if leite > pouco:
		p = leite-pouco
	else:
		p = pouco-leite
	#muito
	if leite > muito:
		m = leite-muito
	else:
		m = muito-leite
	#define
	if p < m:
		leite = 'pouco'
	elif m < p:
		leite = 'muito'
	else:
		leite = 'leite'
else:
	leite = -1
		
if metade >= 0:
	cafe = 'metade'
	leite = 'metade'

#define o tipo de cafe
if (cafe == 'pouco') and (leite == 'muito'):
	print('Nós recomendamos o café "Lágrima" para você, tenha um bom dia!')
	print('(pouco café e muito leite)')
	
elif ((cafe == 'muito') and (leite == 'pouco')) or ((cafe == 'cafe') and (leite == 'pouco')):
	print('Nós recomendamos o café "Cortado" para você, tenha um bom dia!')
	print('(café c/ pouco leite)')
	
elif (cafe == 'metade') and (leite == 'metade'):
	print('Nós recomendamos o "Café com leite" para você, tenha um bom dia!')
	print('(metade café, metade leite)')

elif (cafe == 'muito') and (leite == -1):
	print('Nós recomendamos o café "Doble" para você, tenha um bom dia!')
	print('(dose dupla de café)')

elif (cafe == 'cafe') and (leite == -1):
	print('Nós recomendamos o café "Expresso" para você, tenha um bom dia!')
	print('(café preto)')
elif (cafe == -1) and (leite == 'leite'):
	print('Nós recomendamos o "Submarino" para você, tenha um bom dia!')
	print('(leite c/ uma barra de chocolate)')
else:
	print('Nada encontrado, tome água mesmo!')
