# -*- coding:utf-8 -*-
import collections 

def encontrar_estado(escolas,estado):
	e = []

	for escola in escolas:
		if escola['uf'] == estado.upper():
			e.append(escola)
	return e

def encontrar_rede(escolas,rede):
	redes = []
	
	for escola in escolas:
		if escola['rede'] == rede.capitalize():
			redes.append(escola)
	return redes

def encontrar_zona(escolas,zona):
	e = []

	for escola in escolas:
		if escola['zona'] == zona.upper():
			e.append(escola)
	return e

def ranking(escolas,n):
	return escolas[:n]

def ranking_chave(escolas,chave,nota):
	e = []
	
	for escola in escolas:
		
		if escola[chave] >= nota:
			e.append(escola)
			
	return len(e)
	
def formata(escolas):
	if not escolas:
		print ""
		print "{:^60}".format("Não há escolas para exibir")
	else:
		print "{:^10} | {:^10} | {:^15} | {:^10}".format("Ranking Regional","Ranking Nacional","Notas","Nome")
		for i in range(len(escolas)):
			print "{:^16} | {:^15} | {:^20} | {:^15}  ".format(i+1,escolas[i]['ranking'],escolas[i]['objetivas'],escolas[i]['nome'])

