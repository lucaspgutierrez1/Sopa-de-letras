import random
import csv
csvColumnas = ['Palabra','x_inicial','y_inicial','x_final','y_final']
class Programa:
    def main(self):
        datos = Obtener_Datos.obtener_datos_tablero(self)
        print(datos)
        usuario = Obtener_Datos.obtener_datos_usuario(self)
        print(usuario)
        arrayMatrizYDiccionario = Generador_Tableros.generar(self,datos[0],datos[1])
        Escritor.escribir_tablero(self,arrayMatrizYDiccionario[0],datos[2])
        nombreDiccionario = datos[2] + "Solucion"
        Escritor.escribir_solucion(self,arrayMatrizYDiccionario[1],nombreDiccionario)
        print(arrayMatrizYDiccionario[1])
class Generador_Tableros(Programa):
    def generar(self,N,listaPalabras):
        filas = N
        columnas = N
        diccionario = []
        arr = [[0 for i in range(columnas)] for j in range(filas)]
        for palabra in listaPalabras:
            posicion = random.randint(1,2) 
            print(palabra)
            if posicion == 1:
                posicionXInicial = random.randint(0,N-len(palabra)-1)
                posicionYInicial = random.randint(0,N-len(palabra)-1)
                while type(arr[posicionYInicial][posicionXInicial]) == str :
                    posicionXInicial = random.randint(0,N-len(palabra)-1)
                    posicionYInicial = random.randint(0,N-len(palabra)-1) 
                print(posicion)
                print(posicionXInicial," Posicion X")
                print(posicionYInicial," Posicion Y")
                if posicionYInicial == (N-1) :
                    diccionario.append({'Palabra':palabra,'x_inicial':posicionXInicial,'y_inicial':posicionYInicial,'x_final': posicionXInicial ,'y_final':(posicionYInicial+len(palabra)-1)}) 
                    longitudPalabra = len(palabra)
                    while (longitudPalabra > 0 ):
                        longitudPalabra = longitudPalabra - 1
                        print(palabra[longitudPalabra])
                        arr[posicionYInicial][posicionXInicial] = palabra[longitudPalabra]
                        posicionYInicial = posicionYInicial - 1
                    print("Vertical 1")
                if posicionYInicial == 0 :
                    diccionario.append({'Palabra':palabra,'x_inicial':posicionXInicial,'y_inicial':posicionYInicial,'x_final': posicionXInicial ,'y_final':(posicionYInicial+len(palabra)-1)}) 
                    longitudPalabra = 0
                    while (longitudPalabra != ( len(palabra)) ):
                        print(palabra[longitudPalabra])
                        arr[posicionYInicial][posicionXInicial] = palabra[longitudPalabra]
                        posicionYInicial = posicionYInicial + 1
                        longitudPalabra = longitudPalabra + 1
                    posicionYInicial = 0
                    print("Vertical 2")
                if (posicionYInicial < N and posicionYInicial > 0):
                    diccionario.append({'Palabra':palabra,'x_inicial':posicionXInicial,'y_inicial':posicionYInicial,'x_final': (posicionXInicial+len(palabra) -1) ,'y_final':posicionYInicial})
                    longitudPalabra = 0
                    while (longitudPalabra != ( len(palabra)) ):
                        print(palabra[longitudPalabra])
                        arr[posicionYInicial][posicionXInicial] = palabra[longitudPalabra]
                        posicionXInicial = posicionXInicial + 1
                        longitudPalabra = longitudPalabra + 1
                    print("Vertical 3")
            if posicion == 2:
                posicionXInicial = random.randint(0,N-len(palabra)-1)
                posicionYInicial = random.randint(0,N-len(palabra)-1)
                while type(arr[posicionYInicial][posicionXInicial]) == str :
                    posicionXInicial = random.randint(0,N-len(palabra)-1)
                    posicionYInicial = random.randint(0,N-len(palabra)-1) 
                print(posicion)
                print(posicionXInicial," Posicion X")
                print(posicionYInicial," Posicion Y")
                if posicionXInicial == (N-1) :
                    diccionario.append({'Palabra':palabra,'x_inicial':posicionXInicial,'y_inicial':posicionYInicial,'x_final': (posicionXInicial+len(palabra) -1) ,'y_final':posicionYInicial})
                    longitudPalabra = len(palabra)
                    while (longitudPalabra > 0 ):
                        longitudPalabra = longitudPalabra - 1
                        print(palabra[longitudPalabra])
                        arr[posicionYInicial][posicionXInicial] = palabra[longitudPalabra]
                        posicionXInicial = posicionXInicial - 1
                    print("Horizontal 1")
                if posicionXInicial == 0 :
                    diccionario.append({'Palabra':palabra,'x_inicial':posicionXInicial,'y_inicial':posicionYInicial,'x_final': (posicionXInicial+len(palabra) -1) ,'y_final':posicionYInicial})
                    longitudPalabra = 0
                    while (longitudPalabra != ( len(palabra)) ):
                        print(palabra[longitudPalabra])
                        arr[posicionYInicial][posicionXInicial] = palabra[longitudPalabra]
                        posicionXInicial = posicionXInicial + 1
                        longitudPalabra = longitudPalabra + 1
                    posicionXInicial = 0
                    print("Horizontal 2")
                if (posicionXInicial < N and posicionXInicial > 0):
                    diccionario.append({'Palabra':palabra,'x_inicial':posicionXInicial,'y_inicial':posicionYInicial,'x_final': posicionXInicial ,'y_final':(posicionYInicial+len(palabra)-1)}) 
                    longitudPalabra = 0
                    while (longitudPalabra != ( len(palabra)) ):
                        print(palabra[longitudPalabra])
                        arr[posicionYInicial][posicionXInicial] = palabra[longitudPalabra]
                        posicionYInicial = posicionYInicial + 1
                        longitudPalabra = longitudPalabra + 1
                    print("Horizontal 3")
            print(len(palabra))
        for i in range(columnas): 
            for j in range(filas):
                if arr[i][j] == 0:
                    arr[i][j] = random.choice("abcdefghijklmnopqrstuvwxyz")
        for espacio in arr:
            print(*espacio,sep =' | ')
        return arr,diccionario
class Obtener_Datos(Programa):
    def obtener_datos_usuario(self):
        print("Ingrese el nombre de usuario")
        nombreUsuario = input()
        return nombreUsuario
    def obtener_datos_tablero(self):
        print("Ingrese la cantidad de columas y filas y presione enter: ")
        error = False
        try:
            N=int(input())
        except:
            error = True
            print("Por favor ingrese un numero y presione enter")
        while error == True or N < 15:
            try:
                N=int(input())
                error = False
            except :
                print("Por favor ingrese un numero y presione enter")
        # while N < 15:
        #     print("Ingrese la cantidad de columas y filas: ")
        #     N=int(input())
        print("Ingrese una palabra de longitud menor o igual a  " + str(N/3 - 1) + ":")
        palabra=input()
        limitante = N/3
        listaPalabras= []
        while (palabra != "fin" and len(listaPalabras)<limitante):
            if (len(palabra) < limitante):
                listaPalabras.append(palabra)
            print("Ingrese una palabra de longitud menor o igual a  " + str(N/3 - 1) + ":")
            palabra=input()
        print(listaPalabras)
        print("Ingrese el nombre del archivo: ")
        nombre = input()
        verificado = False
        while verificado == False :
            if (len(nombre) < 30):
                nombreArchivo = nombre
                verificado = True
            else:
                print("Ingrese el nombre del archivo: ")
                nombre = input()
        print(nombreArchivo)
        datosTupla = (N,listaPalabras,nombreArchivo)
        print(datosTupla)
        return datosTupla
class Escritor(Programa):
    def escribir_tablero(self,matriz,nombreArchivo):
        with open(nombreArchivo,"w", newline="") as archivo:
            escritor = csv.writer(archivo,delimiter=',')
            escritor.writerows(matriz)
    def escribir_solucion(self,diccionario,nombreArchivoDiccionario):
        with open(nombreArchivoDiccionario,"w",newline="") as archivo2:
            escritor2 = csv.DictWriter(archivo2,fieldnames=csvColumnas)
            escritor2.writeheader()
            for informacion in diccionario:
                escritor2.writerow(informacion)
p = Programa()
p.main()
