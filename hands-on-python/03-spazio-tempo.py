'''

1) Scrivere una funzione che, acquisiti i dati relativi a dei studenti, li scriva in un file.
   Per ogni studente, in righe separate, dovranno essere indicati: nome (si assuma che ogni personaggio abbia un solo nome), mezzo (auto, bus, bici, piedi), distanza e tempo impiegato per arrivare all'università.
 
2) Scrivere una funzione in grado di restituire un'opportuna struttura dei dati contenenti le informazioni sui tempii medi  di percorrenza dei vari mezzi.
   In altri termini, creare una lista in cui ogni elemento rappresenti un dizionario con i seguenti dati: mezzo e velocità media di percorrenza.
 
3) Scrivere una funzione che esegua la seguente operazione: dato come parametro il valore del mezzo, 
   sia in grado di restituire uno studente a caso che usa il mezzo specificato.
 
4) Scrivere una funzione in grado di stampare il seguente grafico:
   per un dato mezzo, in ascisse lo spazio e in ordinate il tempo impiegato a percorre quello spazio.

'''

from random import choice
from pylab import *

def scrivi(nome_file):
	f = open(nome_file, 'w')
	while (True):
    		nome = raw_input("Nome del prossimo personaggio (Invio per terminare): ")
    		if (nome == ''):
        		break
    		cognome = raw_input("Cognome : ")
    		sesso = raw_input("Sesso (M/F): ")
    		eta = raw_input("Eta' presunta: ")
    		f.write(nome + ' ' + cognome + ' ' + sesso + ' ' + eta + '\n')
	f.close()

def leggi_file(nome_file):
	f = open(nome_file, 'r')
	personaggi = []

    	while (True):
		riga = f.readline()
		dati = riga.split(' ')
		if (riga == '' or riga == '\n'):
            		break
		personaggio = { 'nome': dati[0],
				'cognome': dati[1],
				'sesso': dati[2], 
				'eta': int(dati[3]) }

		personaggi = personaggi + [ personaggio ]

	f.close()
	return personaggi

def leggi_personaggio(personaggi, sesso):
	personaggi_selezionati = []
	for d in personaggi: 
		if d['sesso'] == sesso: 
			personaggi_selezionati = personaggi_selezionati + [d]
	return choice(personaggi_selezionati)

def stampa_torta(personaggi):
	frequenza_sesso = [0, 0] # assumo che il primo elemento della lista si riferisca ai maschi
	for d in personaggi:
		if d['sesso'] == 'M':
			frequenza_sesso[0] = frequenza_sesso[0] + 1 # assumendo che il primo elemento della lista si riferisca ai maschi
		else:
			frequenza_sesso[1] = frequenza_sesso[1] + 1
	pie(frequenza_sesso, labels = ['maschi', 'femmine'])
	show()
	
		
def main():
	nome_file = '/tmp/01-personaggi.txt'
	# scrivi(nome_file)
	personaggi = leggi_file(nome_file)
	print leggi_personaggio(personaggi, 'F')
	stampa_torta(personaggi)

main()
