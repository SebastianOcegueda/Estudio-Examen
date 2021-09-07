def main():
    #escribe tu código abajo de esta línea
    
    n=int(input('Dame un numero: '))
    suma=0

    while (n != 0):
        suma=suma+n
        n=int(input('Dame un numero: '))

    print(suma)




if __name__=='__main__':
    main()
