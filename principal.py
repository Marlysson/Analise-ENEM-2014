# -*- encoding:utf-8 -*-
'''
Arquivo com o menu e as chamadas para as classes auxiliares
'''

from normaliza import *
from metodos import *

arquivo = open('enem2014.csv')
escolas = to_json(arquivo)


def menu():

	funcionalidades = [
			'Por estado',
			'Por rede',
			'Rede por estado',
			'Sair'
	]

	print "########## Análise ENEM 2014 #########"
	for valor,item in enumerate(funcionalidades):
		print "{} - {}".format(valor+1,item)


menu()

opcao = int(raw_input('Escolha uma opção: '))

while opcao != 4:
	if opcao == 1:
		estado = raw_input('Sigla: ')
		quant = int(raw_input('Quantidade: '))

		escola_estado = encontrar_estado(escolas,estado)
		lista = ranking(escola_estado,quant)
		# print lista
		formata(lista)
		opcao = None





