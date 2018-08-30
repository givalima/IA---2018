from random import randint
import urllib

def test_config(config):
    lists = urllib.request.urlopen(
        "http://localhost:8080/antenna/simulate?phi1=" + str(config[0]) + "&theta1=" + 
        str(config[1]) + "&phi2=" + str(config[2]) + "&theta2=" + str(config[3]) + 
        "&phi3=" + str(config[4]) + "&theta3=" + str(config[5]) + "").read().decode().split('\n')
    return float(lists[0])

def mutacao(gene):
    rand = randint(1, 100)/100
    if(rand <= 0.25):
        gene[randint(0,5)] = randint(0,359)
    return gene

def fazer_selecao(population):
    selec = randint(1,100)/100
    if(selec >= 0.5):
        ind_1 = randint(1, 10)
        ind_2 = randint(1, 10)
        ind_1 = len(population)-ind_1
        ind_2 = len(population)-ind_2
        return gerar_genes(population[ind_1], population[ind_2])
    elif(selec >= 0.1 and selec < 0.5):
        ind_1 = randint(1, 50)
        ind_2 = randint(1, 50)
        return gerar_genes(population[len(population)-ind_1], population[len(population)-ind_2])
    elif(selec < 0.1):
        ind_1 = randint(1,len(populacao)-1)
        ind_2 = randint(1,len(populacao)-1)
        return gerar_genes(population[len(population)-ind_1], population[len(population)-ind_2])

def gerar_genes(individuo_1, individuo_2):
    gene = [0]*6
    teste = randint(1,2)
    if(teste == 1):
        for j in range(3):
            gene[j] = individuo_1[j]
            gene[5-j] = individuo_2[5-j]
    else:
        for j in range(3):
            gene[j] = individuo_2[j]
            gene[5-j] = individuo_1[5-j]
    gene = mutacao(gene)
    result = test_config(gene)
    gene.append(result)
    return gene
        
def formar_populacao():
    teste = []
    for i in range(6):
        teste.append(randint(0,359))
    return teste

contador = 0
populacao = []
for i in range(1000):
    populacao.append(formar_populacao())
    
for i in range(1000):
    show = test_config(populacao[i])
    populacao[i].append(show)
    
populacao.sort(key= lambda x: x[6])
melhor = populacao[len(populacao)-1][6]

while(contador < 50):
    flag = 0
    tam = len(populacao)
    for i in range(len(populacao)):
        gene = fazer_selecao(populacao)
        teste = gene[len(gene)-1] #teste = gene[6]
        populacao.append(gene)
        
        if(teste > melhor):
            melhor = teste
            flag = 1
    
    if(flag != 1):
        contador += 1
    populacao.sort(key= lambda x: x[6])
    populacao = populacao[len(populacao)-101: len(populacao)-1]

print("MELHOR RESULTADO:", melhor)
