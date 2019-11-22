import random;  #LIBRERIA PARA EL NUMERO ALEATORIO
class dado:     #CLASE

####################################################
    def numero(limite):
        for x in range(1):                          #METODO DE ASIGNACION ALEATORIO DE NUMEROS
            print(random.randint(1, limite + 1))
####################################################

    print("Hola, bienvenido al dado mágico: ")      #SALUDO
    rango = int(input("Ingrese el limite del numero del dado: ")) #RANGO DEL DADO
    numero(rango)   #PRIMERA IMPRESION DEL DADO

    while True:     #CICLO PARA IMPRIMIR LAS VECES QUE QUIERA
        r = int(input("Desea otro? (1/0): "))
        if r == 1:  #CONDICION SI
            numero(rango)
        if r == 0:  #CONDICION NO
            break


