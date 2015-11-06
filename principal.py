# -*- coding:utf-8 -*-
'''
Arquivo com o menu e as chamadas para as classes auxiliares
'''

from normaliza import *
from metodos import *

arquivo = open('enem2014.csv')
escolas = to_json(arquivo)

redes = {'E':'Estadual','M':'Municipal','F':'Federal','P':'Privada'}

opcoes_funcionalidades = [
		'Por estado',
		'Por rede',
		'Rede por estado',
		'Quantidade de escolas acima de um valor',
		'Sair'
]


def menu(opcoes):
	for valor,item in enumerate(opcoes):
		print "{} - {}".format(valor+1,item)


print ""
print "########## Análise ENEM 2014 #########"
menu(opcoes_funcionalidades)

opcao = int(raw_input('Escolha uma opção: '))

while opcao != 5:
	if opcao == 1:
		
		estado = raw_input('Sigla: ')
		while estado.isdigit() or not estado:
			estado = raw_input('Sigla: ')
			
		quant = int(raw_input('Quantidade: '))
		while not quant:
			quant = int(raw_input('Quantidade: '))
		
		escola_estado = encontrar_estado(escolas,estado)
		lista = ranking(escola_estado,quant)
		
		formata(lista)
		
		menu(opcoes_funcionalidades)
	if opcao == 2:
		op = raw_input("Digite a rede desejada: M - F - E - P - [S]air: ").upper()
		
		if op == 'S':
			break
		else:
			
			r = encontrar_rede(escolas,redes[op])
			
			quant = int(raw_input('Quantidade: '))
			while not quant:
				quant = int(raw_input('Quantidade: '))
				
			primeiras = ranking(r,quant)
			
			formata(primeiras)
			
	if opcao == 3:
		op = raw_input("Digite a rede desejada: M - F - E - P - [S]air: ").upper()
		
		if op == 'S':
			break
		else:
			
			sigla = raw_input('Sigla: ')	
			
			r = encontrar_rede(escolas,redes[op])
			escola_rede = encontrar_estado(r,sigla)
			
			quant = int(raw_input('Quantidade: '))
			while not quant:
				quant = int(raw_input('Quantidade: '))
					
			primeiras = ranking(escola_rede,quant)
				
			formata(primeiras)
			
	if opcao == 4:
		
		materias = ['Objetivas','Matematica','Linguagens','Humanas','Natureza','Redacao','Sair']
		
		print ""
		print "########## Análise ENEM 2014 #########"
		menu(materias)
		
		materia = materias[int(raw_input('\nMatéria: ')) - 1].lower()
		
		if materia == 'sair':
			break
		
		elif materia != 'sair':
			nota = float(raw_input('Nota: '))
			
			num_escolas = ranking_chave(escolas,materia,nota)
			
			print "\nHá {} escolas iguais acima de {} em {}".format(num_escolas,nota,materia)
			
			
			op = raw_input('Consultar novamente? [s/n]').lower()
			
			if op == 's':
				menu(materias)
			else:
				break

	if opcao == 5:
		break
	




