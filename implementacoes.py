# -*- coding: utf8 -*-

import sqlite3

arquivo = open('enem_2014_csv.csv')

class Banco(object):

	def create_db(self,name):
		arquivos = os.listdir('./')
		db = name+'.db'

		if not db in arquivos:
			con = sqlite3.connect(db)
			return con
		else:
			return "Already exists database '{}'".format(name)


	def verify_table(self,con,name):
		tables = con.execute("SELECT * FROM sqlite_master WHERE type='table'")
		print tables
		if name in tables:
			return True
		return False

	def create_table(self,con=None,table=None,campos=None):
		con.execute("CREATE table {} {}".format(table,campos))
		
	def get_fields(self,arquivo,separador=None):
		tabela = arquivo.readline() #pegar primeira linha
		tabela = tabela.lower().split(separador) #transforma em minúsculo e separa no delimitador

		for  in tabela:
			if 'm\xe9dia da escola'
		return tabela


class Escola(object):
	def compara_escolas(self,escola1,escola2):
		pass

	def ranking(self,tipo):
		pass


campos = [
			'ranking','nome','municipio','UF','tipo',
			'permanencia','socioeconomico','prova_objetiva',
			'linguagens','matematica','natureza','humanas','redacao'
		]


con = sqlite3.connect('enem.db')

b = Banco()
campos = b.get_fields(arquivo,separador=";")

print campos