# -*- coding: utf-8 -*-

def limpa_linha(linha):
	linha = linha.strip("\r\n") 
	linha = linha.strip(";")
	return linha

def format_notas(d):
	if d.isdigit():
		return int(d) #Retorna o próprio número
	elif ',' in d:
		d = d.replace(',','.')
		return float(d) #Retorna a string transformada em float
	else:
		# d = d.encode('cp1252').decode('utf-8')
		return d #Retorna a própria string

def get_campos(linha,separador=';'):
	linha = limpa_linha(linha)
	linha = linha.lower()
	linha = linha.split(separador)
	return linha

def to_json(arquivo):

	dados = []
	data = {}

	campos = get_campos(arquivo.readline())
	escolas = arquivo.readlines()

	for escola in escolas:
		escola = limpa_linha(escola)
		escola = escola.split(';')

		for campo,dado in zip(campos,escola):
			data[campo] = format_notas(dado)
		dados.append(data.copy())

	return dados
