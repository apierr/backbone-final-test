# Dato un numero intero positivo in input, calcolare il numero di Fibonacci associato
# Suggerimento: utilizzare la ricorsione (funzione che chiama se stessa)

def fib(x):
	"""Funzione ricorsiva per calcolare l'n-esimo numero della successione di Fibonacci"""
	if x == 0 or x == 1: 
		return 1	
	else: 
		return fib(x-1) + fib(x-2)
