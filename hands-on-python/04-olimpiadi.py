# -*- coding: utf-8 -*-
'''
Scrivere un programma in python che analizzi i risultati delle olimpiadi:

1)
Aggiunta medaglie atleti:
questa funzionalita' prende come input il nome dell'atleta, la nazionalita' e il numero di medaglie vinte e li scrive in un file.
Per esempio, supponnedo che Michael Phelps abbia vinto 4 medaglie d'oro, due d'argento e nessuna di bronzo, la riga relativa a Michael Phelps conterra' i seguenti dati:
Michael Phelps/Stati Uniti/4 2 0

2)
Elenco atleti:
questa funzionalità genera una lista in cui ad ogni elemento corrisponde un dizionario contenente tre chiavi (nome, nazionalita', medaglie)
La chiave medaglia ha come valore un dizionario con tre chiavi oro, argento e bronzo corrispondente al numero di medaglie vinte, rispettivamente oro, argento e bronzo.

3) 
Atleta con piu' medaglie 
questa funzionalità prende come input un'opzione tra le seguenti tre: oro, argento o bronzo
e stampa l'atleta che ha vinto piu' medaglie di un certo tipo

4)
Medagliere per nazioni:
questa funzionalita' scrive in un file il medagliere per nazioni.
Il file dovra' contenere cinque colonne, rispettivamente: nazione, numero ori, argenti, bronzo e totale delle medaglie vinte.

'''

atleti_file = '/tmp/04-atleti.txt'
file_medagliere = '/tmp/medagliere_nazioni.txt'

def scrivi_atleti():
    f = open(atleti_file, 'a')
    vuoi_continuare = 'si'
    while (vuoi_continuare == 'si'):
        atleta = raw_input('Insersci atleta: ' )
        nazione = raw_input('Insersci nazione: ' )
        medaglie = raw_input('Insersci medaglie (ori, argenti, bronzi): ' )
        f.write(atleta + '/' + nazione + '/' + medaglie + '\n')
        vuoi_continuare = raw_input('Voui continuare (si/no)? ')
    f.close()

def leggi_elenco_atleti(): 
    lista = []
    f = open(atleti_file, 'r')
    righe = f.readlines()
    f.close()
    for riga in righe:
	dati = riga.split('/')
        medaglie = dati[2].split(' ')
        atleta = { 'nome': dati[0], 'nazione': dati[1], 
                   'medaglie': { 'oro': int(medaglie[0]), 'argento': int(medaglie[1]), 'bronzo': int(medaglie[2]) } 
                 }
	lista = lista + [atleta]
    return lista

def atleta_piu_medaglie():
    tipo_medaglia = raw_input('Scegli il tipo di medaglia tra (oro, argento, bronzo)')
    elenco_atleti = leggi_elenco_atleti()
    numero_medaglie = 0
    for d in elenco_atleti:
        if (d['medaglie'][tipo_medaglia] > numero_medaglie):
 	   numero_medaglie = d['medaglie'][tipo_medaglia]
           atleta = d
    print 'l\'atleta con piu\' medgli di ' + tipo_medaglia + ' e\': ' + atleta['nome']

def medagliere_nazioni():
    elenco_atleti = leggi_elenco_atleti()
    medagliere_nazioni = {}
    for d in elenco_atleti:
       if d['nazione'] in medagliere_nazioni:
          for tipo_medaglia in ['oro', 'argento', 'bronzo']:
             medagliere_nazioni[d['nazione']][tipo_medaglia] = medagliere_nazioni[d['nazione']][tipo_medaglia] + d['medaglie'][tipo_medaglia]
       else:
          medagliere_nazioni[d['nazione']] = d['medaglie']
    print medagliere_nazioni
    f = open(file_medagliere, 'w')
    for nazione in medagliere_nazioni:
        ori = str(medagliere_nazioni[nazione]['oro'])
        argenti = str(medagliere_nazioni[nazione]['argento'])
        bronzi = str(medagliere_nazioni[nazione]['bronzo'])
        f.write(nazione + ' ' + ori + ' ' + argenti  + ' ' + bronzi + '\n')
    f.close()
	

#scrivi_atleti()
#print leggi_elenco_atleti()
#atleta_piu_medaglie()
medagliere_nazioni()
