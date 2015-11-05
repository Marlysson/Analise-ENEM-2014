def encontrar_estado(escolas,estado):
	e = []

	for escola in escolas:
		if escola['uf'] == estado.upper():
			e.append(escola)
	return e

def encontrar_rede(escolas,rede):
	e = []

	for escola in escolas:
		if escolas['rede'] == rede.upper():
			e.append(escola)
	return e

def encontrar_zona(escolas,zona):
	e = []

	for escola in escolas:
		if escola['zona'] == zona.upper():
			e.append(escola)
	return e

def ranking(escolas,n):
	return escolas[:n]
	# part = []
	# for i in range(n):
	# 	part.append(escolas[i])
	# return part

def formata(escolas):
	return escolas
	# for i in range(len(escolas)):
	# 	for escola in escolas:
	# 		print "{} - {} -- {}".format(i,escolas['ranking'],escolas['nome'])


