# Data una parola composta da un qualsiasi numero di caratteri, determinare se sia palindroma.
# Suggerimento: utilizzare la ricorsione (funzione che chiama se stessa)

def isPolidroma(s):
    	"Funzione ricorsiva che ritorna True se la stringa e' polidroma altrimenti False"
    	if len(s) <= 1: 
		return True
    	else: 
		return s[0] == s[-1] and isPolidroma(s[1:-1])
