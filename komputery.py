dyski={}
komputery = {}
with open('komputery.txt') as plik:
    for linia in plik:
        dane=linia.strip().split()
        if dane[2] in dyski:
            dyski[dane[2]]+=1
        else:
            dyski[dane[2]]=1
        if dane[1]=='A':
            komputery[dane[0]]=[]
print(komputery)
with open('awarie.txt') as plik:
    for linia in plik:
        dane=linia.strip().split()
        if dane[1] in komputery:
            komputery[dane[1]].append(dane[0])
print(komputery)
#print(dyski)
