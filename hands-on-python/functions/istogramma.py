# Scrivere una funzione che sia in grado di contare il numero di occorrenze di ciascuna lettera presente in una data parola.

def histogramma(s):
    	d = {} # inizializza un dizionario vuoto
    	for c in s:
        	if c not in d:
            		d[c] = 1
        	else:
            		d[c] += 1
    	return d 
