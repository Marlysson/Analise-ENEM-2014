# -*- coding: utf-8 -*-
import json

class Escola(object):
	
	def __init__(self,arquivo):
		self.arquivo = arquivo
		self.escolas = self.to_json(self.arquivo)
		
	def formata(self,d):
		if ',' in d:
			d = d.replace(',','.')
			return float(d)
		elif d.isdigit():
			return int(d)
		else:
			return d
			
	def get_campos(self,linha,separador=';'):
		linha = linha.lower()
		linha = linha.strip('\n\r')
		linha = linha.split(separador)
		return linha

	def to_json(self,arquivo):

			dados = []
			data = {}
			campos = self.get_campos(arquivo.readline())

			escolas = arquivo.readlines()

			for escola in escolas:
				escola = escola.strip('\r\n').split(';')
			
			   for campo,dado in zip(campos,escola):
					data[campo] = self.formata(dado)
				dados.append(data)

			return dados

		
	def compara_escolas(self,escola1,escola2):
		pass

	def ranking(self,tipo):
		pass

arquivo = open('enem2014.csv')
escola = Escola(arquivo)
print escola.escolas

