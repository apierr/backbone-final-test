# Find the square root of a perfect square
# what is a perfect square? It’s a number who’s square root is an integer.
#  si puo' eseguire per tentativi, calcolando il quadrato dei numeri 
#  1, 2, 3, ..., fino a quando il risultato e' minore o uguale
#  al numero considerato.

n = input("insersci un numero positivo: ")
r = 1
while (r * r <= n):
	r = r + 1

print  "La parte intera della radice quadrata di", n, "e'", r - 1
