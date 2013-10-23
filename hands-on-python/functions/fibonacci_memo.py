# Calcolate il numero di Fibonacci.
# Se provate a usare la funzione di Fibonacci (fibonacci.py), potreste aver notato che piu' grande e' il numero che si fornisce, e piu' tempo si impiega a calcolare il numero.
# Utilizzando i dizionari, cercate di implementare una soluzione piu' efficiente.

memo = {0:0, 1:1}

def fibonacci(n):
    	if n in memo:
        	return memo[n]

    	res = fibonacci(n-1) + fibonacci(n-2)
    	memo[n] = res
    	return res
