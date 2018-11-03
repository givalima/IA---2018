import urllib
from random import randint
#import pandas as pd

#base = pd.read_csv("C://Users//givae//Downloads//iris.csv")
base = urllib.request.urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").read().decode().split('\n')
base = base[0:150]

def distancia(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 + (a[3]-b[3])**2)**(1/2)

for i in range(150):
    elemento = base [i]  # Separei o elemento da lista.
    elemento = elemento.split(',') #Separei o emaranhado de strings numa lista de strings
    elemento[0] = float(elemento[0])
    elemento[1] = float(elemento[1])
    elemento[2] = float(elemento[2])
    elemento[3] = float(elemento[3])
    base[i] = elemento  #devolvi pra lista
    #print(elemento)
    
cont = 0
visitados = []
teste = []
while(cont<50):
    aux = randint(0, 149)
    for j in range(len(visitados)):
        if(visitados[j] == aux):
            continue
    visitados.append(aux)
    teste.append(base[aux])
    cont += 1

train = []
for i in range(150):
    flag = 0
    for j in range(50):
        if(i == visitados[j]):
            flag = 1
            break
    if(flag != 1):
        train.append(base[i])
        
acertos = 0
for i in range(len(teste)):
    setosa = 0
    virginica = 0
    versicolor = 0
    for j in range(len(train)):
        train[j].append(distancia(teste[i], train[j]))
    #print(len(train))
    #print("TRAIN:", train)
    train.sort(key = lambda x: x[5])
    for j in range(5):
        if(train[len(train)-j-1][4] == "SETOSA"):
            setosa += 1
        elif(train[len(train)-j-1][4] == "VIRGINICA"):
            virginica += 1
        elif(train[len(train)-j-1][4] == "VERSICOLOR"):
            versicolor += 1
    if(setosa == max(setosa, virginica, versicolor) and teste[i][4] == "SETOSA"):
        acertos+=1
    if(virginica == max(setosa, virginica, versicolor) and teste[i][4] == "VIRGINICA"):
        acertos+=1
    if(versicolor == max(setosa, virginica, versicolor) and teste[i][4] == "VERSICOLOR"):
        acertos+=1

print("ACERTOS:", acertos, "ACURÁCIA:", acertos/50)