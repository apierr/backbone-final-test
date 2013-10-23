# scrivere una funzione che restituisce un dizionario con l'equivalente in ore, minuti e secondi di un dato numero di secondi

def hms(num_sec):
        hh = num_sec/3600
        num_sec = num_sec % 3600
        mm = num_sec/60
        ss = num_sec % 60
        return {'ore': hh, 'minuti': mm, 'secondi': ss}
