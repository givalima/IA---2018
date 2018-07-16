#MISSIONÁRIOS E CANIBAIS - GIVANILDO LIMA

def missionario(lista, cont): #(1, 0)
    if(lista[4] == 0):
        if(not(lista[0] - 1 < 0) and not(lista[0] - 1 < lista[1])):
            lista[0] = lista[0] - 1
            lista[2] = lista[2] + 1
            lista[4] = 1
            lista[6] = lista[5]
            lista[5] = cont + 1
            return lista
        return None
    else:
        if(not(lista[2] - 1 < 0) and not(lista[2] - 1 < lista [3])):
            lista[2] = lista[2] - 1
            lista[0] = lista[0] + 1
            lista[4] = 0
            lista[6] = lista[5]
            lista[5] = cont + 1
            return lista
        return None

def canibal(lista, cont): #(0, 1)
    if(lista[4] == 0):
        if(not(lista[1] - 1 < 0) and not(lista[2] < lista[3] + 1)):
            lista[1] = lista[1] - 1
            lista[3] = lista[3] + 1
            lista[4] = 1
            lista[6] = lista[5]
            lista[5] = cont + 1
            return lista
        return None
    else:
        if(not(lista[3] - 1 < 0) and not(lista[0] < lista [1] + 1)):
            lista[3] = lista[3] - 1
            lista[1] = lista[1] + 1
            lista[4] = 0
            lista[6] = lista[5]
            lista[5] = cont + 1
            return lista
        return None

def missionario_missionario(lista, cont): #(2, 0)
    if(lista[4] == 0):
        if(not(lista[0] - 2 < 0) and not(lista[0] - 2 < lista[1])):
            lista[0] = lista[0] - 2
            lista[2] = lista[2] + 2
            lista[4] = 1
            lista[6] = lista[5]
            lista[5] = cont + 1
            return lista
        return None
    else:
        if(not(lista[2] - 2 < 0) and not(lista[2] - 2 < lista [3])):
            lista[2] = lista[2] - 2
            lista[0] = lista[0] + 2
            lista[4] = 0
            lista[6] = lista[5]
            lista[5] = cont + 1
            return lista
        return None
    
def canibal_canibal(lista, cont): #(0, 2)
    if(lista[4] == 0):
        if(not(lista[1] - 2 < 0) and not(lista[2] < lista[3] + 2)):
            lista[1] = lista[1] - 2
            lista[3] = lista[3] + 2
            lista[4] = 1
            lista[6] = lista[5]
            lista[5] = cont + 1
            return lista
        return None
    else:
        if(not(lista[3] - 2 < 0) and not(lista[0] < lista [1] + 2)):
            lista[3] = lista[3] - 2
            lista[1] = lista[1] + 2
            lista[4] = 0
            lista[6] = lista[5]
            lista[5] = cont + 1
            return lista
        return None
    
def missionario_canibal(lista, cont): #(1, 1)
    if(lista[4] == 0):
        if(not(lista[0] - 1 < 0) and not(lista[1] - 1 < 0)):
            lista[0] = lista[0] - 1
            lista[1] = lista[1] - 1
            lista[2] = lista[2] + 1
            lista[3] = lista[3] + 1
            lista[4] = 1
            lista[6] = lista[5]
            lista[5] = cont + 1
            return lista
        return None
    else:
        if(not(lista[2] - 1 < 0) and not(lista[3] - 1 < 0)):
            lista[2] = lista[2] - 1
            lista[3] = lista[3] - 1
            lista[0] = lista[0] + 1
            lista[1] = lista[1] + 1
            lista[4] = 0
            lista[6] = lista[5]
            lista[5] = cont + 1
            return lista
        return None

def main():
    cont = 0
    #mis_esq, can_esq, mis_dir, can_dir, lado_barco, pos_resultado, pos_pai 
    lista = [3, 3, 0, 0, 0, 0 , -1] #Barco do lado esquerdo
    resultado = []
    resultado.append(lista)
    print(resultado, "\n")
    
    while(resultado[cont][0] != 0 and resultado[cont][1] != 0 and cont != 10):
        
        teste = missionario(resultado[cont], cont)
        if(teste != None):
            resultado.append(teste)
            cont += 1
        print(resultado, "\n")
            
        teste = canibal(resultado[cont], cont)
        if(teste != None):
            resultado.append(teste)
            cont += 1 
        print(resultado, "\n")
            
        teste = missionario_missionario(resultado[cont], cont)
        if(teste != None):
            resultado.append(teste)
            cont += 1
        print(resultado, "\n")
            
        teste = canibal_canibal(resultado[cont], cont)
        if(teste != None):
            resultado.append(teste)
            cont += 1
        print(resultado, "\n")
            
        teste = missionario_canibal(resultado[cont], cont)
        if(teste != None):
            resultado.append(teste)
            cont += 1
        print(resultado, "\n")
        
#    caminho = []
#    
#    while(resultado[cont][6] > 0):
#        caminho.append(resultado[cont])
#        cont = resultado[cont][6] #Volta pra posição do pai
#    
#    caminho.reverse()
#    print(caminho)
          
main()