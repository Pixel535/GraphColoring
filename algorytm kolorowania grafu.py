from numpy import*

n = int(input("Podaj rozmiar tab: "))
m = int(input("Podaj rozmiar tab: "))
tab = zeros((n,m), int , order='C')
print(tab)
lw = len(tab)

def rysuj(tab):
    i = int(input("Podaj ile razy chcesz zmienic na 1: "))
    n = 1
    while n <= i:
        w = int(input("Podaj wiersz tab: "))
        k = int(input("Podaj kolumne tab: "))
        tab[w][k] = 1
        print(tab)
        n += 1

rysuj(tab)


def koloruj(tab):
    kolor = zeros((lw), int, order = 'C')
    for i in range(lw):
        stwierz1 = 0
        stwierz2 = 0
        stwierz3 = []
        maxel1 = 0
        maxel2 = 0
        maxel3 = []
        przejscia = 0
        numerkol = 1
        while przejscia < lw:
            if (len(tab[przejscia]) < lw) and (przejscia < lw-1):
                przejscia += 1
            elif (len(tab[przejscia]) < lw) and (przejscia == lw-1):
                break
            if len(tab[przejscia]) == lw:
                   stwierz1 = przejscia
                   for k in range(lw):
                       if tab[przejscia][k] != 0:
                            stwierz2 += tab[przejscia][k]
                            if (kolor[k] !=0) and (kolor[k] not in stwierz3):
                                stwierz3.append(kolor[k])
                   if len(maxel3) <= len(stwierz3):
                          if maxel2 < stwierz2:
                              maxel1 = stwierz1
                              maxel2 = stwierz2
                              maxel3 = stwierz3
                   stwierz1 = 0
                   stwierz2 = 0
                   stwierz3 = []
            przejscia += 1
        while(numerkol in maxel3):
            numerkol += 1
        kolor[maxel1] = numerkol
        tab[maxel1] = [0]
    print(kolor)

    
koloruj(tab)
