from sys import stdin, stderr
from sets import Set

def beste_sti(nm, sans):
    tattlol = [0]
    tempsans = 0
    while True:
        newnode = 0
        for i in range(0, nm.__len__()):
            if i in tattlol:
                for x in range(0, len(nm[i])):
                    if nm[i][x] != 0 and sans[x] >= tempsans and x not in tattlol:
                        tempsans = sans[x]
                        newnode = x
        tattlol.append(newnode)
        tempsans = 0

        tilgjenglige_noder = Set()
        for tatt in tattlol:
            i = 0
            for nabo in nm[tatt]:
                if nabo == 1:
                    tilgjenglige_noder.add(i)
                i += 1
        if(tilgjenglige_noder.__len__() >= nm.__len__()):
            return tattlol
            break
        # SKRIV DIN KODE HER

n = int(stdin.readline())
sansynligheter = [float(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [0] * n
    naboer = [int(nabo) for nabo in linje.split()]
    for nabo in naboer:
        naborad[nabo] = 1
    nabomatrise.append(naborad)
print beste_sti(nabomatrise, sansynligheter)
# TODO: SPORRE STUDASS HVORFOR DET IKKE ER RIKTIG