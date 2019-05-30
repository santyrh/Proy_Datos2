
la=[] #contiene el archivo neto
#coordenadas=[]
dicNodos={}
Rango_er=0 #
i_ini_D=0
arbol={}

def readFile(file_to_read):
    archivo = open(file_to_read, encoding = 'latin1', errors='ignore')
    for linea in archivo.readlines():
        if (linea != "\n"):
            la.append(linea.replace("\n",""))
            #print(linea.replace("\n",""))
    archivo.close()
    #print(Rango_er)
    #print(la)
    return (1+int(la.index("Costo de Caminos Cortos. Formato: ID, ID, peso"))),(float(la[0].replace("p ","")))

def ord(i):
    cont=0
    '''#guardar posiciones geograficas en un arreglo
    while(cont!=i):
        coordenadas.append(la[cont])
        cont=cont+1
    '''
    #print(coordenadas,"------------")
    cont=0 #reutilizo variable
    cont1=i
    while(cont1!=len(la)):
        aux = la[cont1].split(" ")
        #print(aux)
        if(cont1==i):
            cont=int(aux[0])
            aux.pop(0)
            dicNodos[cont]=[aux]
            #print(dicNodos[1],"diccionario")
        elif(int(aux[0])==cont):
            aux.pop(0)
            dicNodos[cont].append(aux)
            #print(dicNodos[cont],"---")
        elif(int(aux[0])>cont):
            dicNodos[cont]=sorted(dicNodos[cont], key = takeFirst, reverse=False)
            #print(dicNodos[cont],"ordenado")
            cont=int(aux[0])
            aux.pop(0)
            dicNodos[cont]=[aux]
            #print(dicNodos[cont],"------")

        if(cont1==len(la)-1):
            dicNodos[cont]=sorted(dicNodos[cont], key = takeFirst, reverse=False)
        cont1=cont1+1
    #print(dicNodos)

def DicEstadosNodos(dicNodos):
    for dato in dicNodos:
        arbol[dato] = False

def takeFirst(elem):
    return int(elem[1])


def asig_rango(arr):
    nNodos=len(arr)
    mod = round(nNodos/5) #cambiar segun si los nodos tambien se relacionan consigo mismo (nNodos-1)/5
    DicAux={}
    for i in range(5):
        for j in range(mod):
            try:
                if(j==0):
                    DicAux[i]=[arr.pop(0)]
                elif(j!=0):
                    DicAux[i].append(arr.pop(0))
            except:
                pass
        #print(DicAux)
    return DicAux


def orgVoraz(DicR):
    arr=[]
    aux=[]
    #print(len(DicR[4]),len(DicR[3]),len(DicR[2]),len(DicR[1]),len(DicR[0]),)
    estadoWhile=False
    for k in range(4,0,-1):
        cont=0
        while DicR[k]:
            print(DicR[k])
            aux=(DicR[k].pop(0))
            nodo=int(aux[0]) #se estrae el nodo para usarlo como key y buscar los nodos relacionados a esa key(nodo)
            distanciaMax=aux[1] #se estrae el tiempo maximo que puede durar el recorrido si se inicia de dicho nodo
            print(k,aux)

            nodo=int(aux[0])
            distanciaMax=aux[1]
            print(nodo ,dicNodos[nodo])
            dicNodos[nodo].pop(0)
            a=dicNodos[nodo]
            print(a)

            cont+=1
    print(arr,"arr")


def voraz(DicR,k,aux):
    nodo=int(aux[0])
    distanciaMax=aux[1]
    print(nodo ,dicNodos[nodo])
    dicNodos[nodo].pop(0)
    a=min(dicNodos[nodo], key = takeFirst)
    print(a)
    return a



#EJECUCION----------------------------------------------------------------------
i_ini_D, Rango_er = readFile("n205.txt")
ord(i_ini_D)
DicEstadosNodos(dicNodos)
DicRangos=asig_rango(dicNodos[1])
orgVoraz(DicRangos)
#voraz(DicRangos,4)
