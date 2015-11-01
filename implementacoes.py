# -*- coding: utf-8 -*-
import json

class Escola(object):
	
	def subs(self,p):
	    s = 'Sem informacao'
	    if p == 'Sem informação':
	        p = p.replace(p,s)
	        return p

	def get_campos(self,linha,separador=';'):
		linha = linha.lower()
		linha = linha.strip('\n\r')
		linha = linha.split(separador)
	
		return linha

	def to_json(self,arquivo):

		with open(arquivo) as arquivo:

			dados = []
			data = {}

			campos = self.get_campos(arquivo.readline())

			escolas = arquivo.readlines()

			for escola in escolas:
				escola = escola.strip('\r\n').split(';')
			
				for campo,dado in zip(campos,escola):
					data[campo] = dado	
				dados.append(data)

			return dados

		

	def compara_escolas(self,escola1,escola2):
		pass

	def ranking(self,tipo):
		pass


# campos = [
# 			'ranking','nome','municipio','UF','tipo',
# 			'permanencia','socioeconomico','prova_objetiva',
# 			'linguagens','matematica','natureza','humanas','redacao'
# 		]

escola = Escola()
print escola.to_json('enem_2014.csv')

