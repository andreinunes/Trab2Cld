alph=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
seq=input()
x0mealy=[]
x1mealy=[]
estadosmoore=[]
estadosmealy=[]

# ////  Cria as listas contendo os estados \\\\ #
for x in range(len(seq)):
    estadosmealy.append(alph[x])

for x in range(len(seq)+1):
    estadosmoore.append(alph[x])



# ////  Cria a lista de memoria que mostra as entradas passadas na maquina de mealy \\\\ #
memoria=[]
memoria.append([])
for x in range(1,len(estadosmealy)):
    copiaseq= seq[:]
    memoria.append([])
    for i in range(x):
       memoria[x].append(int(copiaseq[i]))

# ////  Determina os proximos estados quando a entrada é igual a 1 \\\\ #
entrada= 1
for x in range(len(estadosmealy)):
    possui= False
    aux=memoria[x][:]
    aux.append(int(entrada))
    while possui == False:
        for i in range(len(estadosmealy)):
            if((possui== False) and (aux == memoria[i])):
                prox=estadosmealy[i][:]
                x1mealy.append(prox)
                possui = True
        if aux != []:
            aux.pop(0)

# ////  Determina os proximos estados quando a entrada é igual a 0 \\\\ #
entrada=0
for x in range(len(estadosmealy)):
    possui= False
    aux=memoria[x][:]
    aux.append(int(entrada))
    while possui == False:
        for i in range(len(estadosmealy)):
            if((possui== False) and (aux == memoria[i])):
                prox=estadosmealy[i][:]
                x0mealy.append(prox)
                possui = True
        if aux != []:
            aux.pop(0)


# ////  Printa a tabela de Mealy\\\\ #

print("MEALY:")
print("                |Estado Seg. |       ")
print("|   Est.Atual   | X0 |   X1  | Z0| Z1|")
for x in range(0, len(seq)):
    if(x!= len(seq)-1):
        print("|      {}        | {}  |   {}   | {} | {} |" .format(estadosmealy[x], x0mealy[x], x1mealy[x],0,0))
    if(x==len(seq)-1):
        if(seq[x]=='1'):
            print("|      {}        | {}  |   {}   | {} | {} |".format(estadosmealy[x], x0mealy[x], x1mealy[x], 0, 1))
        if (seq[x] == '0'):
            print("|      {}        | {}  |   {}   | {} | {} |".format(estadosmealy[x], x0mealy[x], x1mealy[x], 1, 0))


x0moore = []
x1moore= []

# ////  Cria a lista de memoria que mostra as entradas passadas na maquina de moore \\\\ #
memoria=[]
memoria.append([])
for x in range(1,len(estadosmoore)):
    copiaseq= seq[:]
    memoria.append([])
    for i in range(x):
       memoria[x].append(int(copiaseq[i]))



# ////  Determina os proximos estados quando a entrada é igual a 1 \\\\ #

entrada= 1
for x in range(len(estadosmoore)):
    possui= False
    aux=memoria[x][:]
    aux.append(int(entrada))
    while possui == False:
        for i in range(len(estadosmoore)):
            if((possui== False) and (aux == memoria[i])):
                prox=estadosmoore[i][:]
                x1moore.append(prox)
                possui = True
        if aux != []:
            aux.pop(0)



# ////  Determina os proximos estados quando a entrada é igual a 0 \\\\ #
entrada=0
for x in range(len(estadosmoore)):
    possui= False
    aux=memoria[x][:]
    aux.append(int(entrada))
    while possui == False:
        for i in range(len(estadosmoore)):
            if((possui== False) and (aux == memoria[i])):
                prox=estadosmoore[i][:]
                x0moore.append(prox)
                possui = True
        if aux != []:
            aux.pop(0)


# ////  Printa a tabela de Moore\\\\ #
print("\n")
print("MOORE:")
print("                |Estado Seg. |       ")
print("|   Est.Atual   | X0 |   X1  | Z0| Z1|")
for x in range(0, len(estadosmoore)):
    if(x!= len(estadosmoore)-1):
        print("|      {}        | {}  |   {}   | {} | {} |" .format(estadosmoore[x], x0moore[x], x1moore[x],0,0))
    if(x==len(estadosmoore)-1):
         print("|      {}        | {}  |   {}   | {} | {} |".format(estadosmoore[x], x0moore[x], x1moore[x], 1, 1))
