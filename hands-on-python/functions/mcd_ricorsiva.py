# Massimo comune divisore di due interi (versione ricorsiva)

def mcd(a, b):
    	"""Restituisce il Massimo Comune Divisore tra a e b"""
    	if a == b:  
		return a
    	elif a > b: 
		return mcd(a-b, b)
    	else:
		return mcd(b-a, a)
