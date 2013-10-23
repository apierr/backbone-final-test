# Data una lista di 5 numeri, calcolare la somma, la media e la varianza

def somma(lista):
    	s = 0.0
    	for num in lista:
        	s += num
    	return s

def media(lista):
	lunghezza_lista = 5
    	return somma(lista) / 5

def varianza(lista):
	lunghezza_lista = 5
	med = media(lista)
	varianza = 0.0
	i = 0
	while (i < lunghezza_lista):
		scarto = (lista[i] - med)
		varianza = varianza + scarto * scarto 
		i = i + 1
	return varianza / lunghezza_lista
