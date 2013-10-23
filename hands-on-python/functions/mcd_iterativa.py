# Massimo comune divisore di due interi (versione iterativa)

def mcd(a, b):
    """Restituisce il Massimo Comune Divisore tra a e b"""
    while b:
        # a, b = b, a % b
	c = a % b
	a = b
	b = c
    return a
