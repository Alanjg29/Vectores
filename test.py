num4array = 0;

num4array = int(input("Cual es la longitud de tu vector? "))

#Esto sirve para borrar la pantalla y visualizar mis listas
def clear(a, b, fitA, fitB):
    import os
    os.system('cls')
    print("1) vector %r y su fit %d" %(a, fitA))
    print("2) vector %r y su fit %d" %(b, fitB))
    #print("")
    return

#Este lo uso para generar mis primeras listas
def firstRandom():
    num = num4array;
    aList = list()
    for num in range(num4array):
        from random import randint
        x = randint(0,1)
        aList.append(x)
    return aList

#Aqui hago el crossover de mis dos listas y elijo con cual me quedo
def compare(a, b, fitA, fitB):
    #clear(a, b, fitA, fitB)
    print("Este es A antes", a)
    print("Este es B antes", b)
    print("********************")
    y = len(a)
    z = round(y/2)
    y1 = len(a)/2
    z1 = round(y/2)
    swap4A = a
    swap4B = b
    if fitA == z:
        if fitB == z:
            a = swap4A[:z1] + swap4B[:z1]
            print(a)
            b = swap4B[z1:] + swap4A[z1:]
            print("Nuevo vector del primeradfadadfo ", a)
            fitSwapA = int(input("Cuantos aciertos para este vector? "))
            print("Nuevo vector del segundo" , b)
            fitSwapB = int(input("Cuantos aciertos para este vector?"))
            if fitSwapA == 0:
                fitA = fitSwapA
                compareFit(a, b, fitA, fitB)
            if fitSwapB == 0:
                fitB == fitSwapB
                compareFit(a, b, fitA, fitB)
            if fitSwapA > fitA:
                if fitSwapA >= fitB:
                    if fitSwapB >= fitB:
                        fitA = fitSwapA
                        fitB = fitSwapB
                        compareFit(a, b, fitA, fitB)
                else:
                    fitB = fitSwapA
                    compareFit(a, b, fitA, fitB)
                    return
            if fitSwapA <= fitA:
                if fitSwapB >= fitA:
                    if fitA == fitB:
                        if fitSwapA == fitSwapB:
                            secondRandom(a, b, fitA, fitB)
                    else:
                        b = swap4B
                        fitB = fitSwapB
                        compareFit(a, b, fitA, fitB)
                elif fitSwapA >= fitB:
                    if fitSwapB > fitB:
                        fitB = fitSwapB
                        compareFit(a, b, fitA, fitB)
                    else:
                        b = swap4B
                        fitB = fitSwapA
                        compareFit(a, b, fitA, fitB)
                elif fitSwapB > fitB:
                    fitB = fitSwapB
                    compareFit(a, b, fitA, fitB)
                elif fitSwapB <= fitA:
                    a = swap4A
                    b = swap4B
                    secondRandom(a, b, fitA, fitB)
                return
    a = swap4A[:z] + swap4B[z:]
    print(a)
    print(swap4A)
    b = swap4B[:z] + swap4A[z:]
    print("Nuevo vector del primero ", a)
    fitSwapA = int(input("***Cuantos aciertos para este vector? "))
    print("Nuevo vector del segundo" , b)
    fitSwapB = int(input("Cuantos aciertos para este vector? "))
    if fitSwapA == 0:
        fitA = fitSwapA
        compareFit(a, b, fitA, fitB)
    if fitSwapB == 0:
        fitA == fitSwapB
    if fitSwapA > fitA:
        if fitSwapA >= fitB:
            if fitSwapB >= fitB:
                fitA = fitSwapA
                fitB = fitSwapB
                compareFit(a, b, fitA, fitB)
        if fitSwapB < fitB:
            fitB = fitSwapA
            compareFit(a, b, fitA, fitB)
            return
    if fitSwapA <= fitA:
        if fitSwapB >= fitA:
            if fitA == fitB:
                if fitSwapA == fitSwapB:
                    secondRandom(a, b, fitA, fitB)
            else:
                fitB = fitSwapB
                compareFit(a, b, fitA, fitB)
        elif fitSwapA >= fitB:
            if fitSwapB > fitB:
                fitB = fitSwapB
                compareFit(a, b, fitA, fitB)
            else:
                b = swap4B
                fitB = fitSwapA
                compareFit(a, b, fitA, fitB)
        elif fitSwapB > fitB:
            fitB = fitSwapB
            compareFit(a, b, fitA, fitB)
        elif fitSwapB <= fitA:
            a = swap4A
            b = swap4B
            secondRandom(a, b, fitA, fitB)
    return

#Aqui si del "compare" no me sale un fit mejor generamos un 3er random y comparamos
def secondRandom(a, b, fitA, fitB):
    #clear(a, b, fitA, fitB)
    c = list(firstRandom())
    print(a)
    print(b)
    print("********************")
    print(c)
    fitC = int(input("second random "))
    if fitC > fitA:
        a = c
        fitA = fitC
        compareFit(a, b, fitA, fitB)
    elif fitC > fitB:
        b = c
        fitB = fitC
        compareFit(a, b, fitA, fitB)
    else:
        secondRandom(a, b, fitA, fitB)
    return

#Aqui solo comparamos el fit para ver si le atinamos o no, si no lo mandamos al compare para hacer un crossover
def compareFit(a, b, fitA, fitB):
    #clear(a, b, fitA, fitB)
    if fitA == num4array:
        print("Le atinamos woohoo! ")
        print("Este es tu vector: ", a)
        return exit
    if fitB == num4array:
        print("Le atinamos woohoo!")
        print("Este es tu vector: ", b)
        return exit
    #if fitA == 0:
    #    flip(a, b, fitA, fitB)
    #if fitB == 0:
    #    flip(a, b, fitA, fitB)
    #elif fitA == fitB:
    #    compare(a, b, fitA, fitB)
    #else:
        if fitB > fitA:
            fitC = fitA
            fitA = fitB
            fitB = fitC
            c = a
            a = b
            b = c
            compare(a, b, fitA, fitB)
            pass
    compare(a, b, fitA, fitB)
    return

#El flip me sirve para si en el fit recibe un 0 me hace un flip de todo, lo cual al momento de invertir deberia de dar el resultado
def flip(a, b, fitA, fitB):
    #clear(a, b, fitA, fitB)
    if fitA == 0:
        for i in range(len(a)):
            if a[i] == 1:
                a[i] = 0
            else:
                a[i] = 1
        print(a)
        fitA = int(input("Este fue el flip de A, cuantos? "))
        compareFit(a, b, fitA, fitB)
    if fitB == 0:
        for i in range(len(a)):
            if b[i] == 1:
                b[i] = 0
            else:
                b[i] = 1
        print(b)
        fitB = int(input("Este fue el flip de B, cuantos? "))
        compareFit(a, b, fitA, fitB)
    return

#La función main, aquí es donde empieza a correr el programa.
def main ():
    a = list(firstRandom())
    b = list(firstRandom())
    print(a)
    fitA = int(input("Cuantos aciertos para el primer vector? "))
    print(b)
    fitB = int(input("Cuantos aciertos para el segundo vector? "))
    if fitA > num4array:
        print("ERROR! Acertijo es mas grande que el vector!")
        print(a)
        fitA = int(input("Cuantos aciertos para el primer vector? "))
    elif fitB > num4array:
        print("ERROR! Acertijo es mas grande que el vector!")
        print(b)
        fitB = int(input("Cuantos aciertos para el segundo vector? "))
    if fitA == 0:
        flip(a, b, fitA, fitB)
    if fitB == 0:
        flip(a, b, fitA, fitB)
    if fitA != fitB:
        compareFit(a, b, fitA, fitB)
    if fitA == fitB:
        compareFit(a, b, fitA, fitB)
    return

main();
