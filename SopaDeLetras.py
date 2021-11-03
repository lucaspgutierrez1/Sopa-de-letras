import csv


class Programa:
    listaPalabrasEncontradas = []
    listaPalabras = []
    datos=[]
    puntos = 0
    def main(self):
        arrayDatos = Obtener_Datos.obtener_datos_del_usuario(self)
        print("El nombre de usuario es: " + arrayDatos[0] + " y el nombre del archivo es: " + arrayDatos[1])
        Juego.imprimir_juego(self,arrayDatos[1])
        Juego.guardar_palabras(self,arrayDatos[1])
        while len(self.listaPalabras) > 0:
            self.datos = Juego.ingresar_palabra(self,arrayDatos[1],arrayDatos[0])
        self.puntos = str(Jugador.imprimir_puntaje(self))
        print("El jugador "+ arrayDatos[0] + " termino con " + self.puntos + " puntos")
        print("Las palabras han sido encontradas en el siguiente orden: ")
        for x in self.listaPalabrasEncontradas:
            print(x)
class Obtener_Datos(Programa):
    def obtener_datos_del_usuario(self):
        buscar = True
        error = False
        nombreUsuario = input("Ingrese el nombre de usuario,tiene que ser menor a 40 caracteres: ")
        if len(nombreUsuario) < 40:
            print("Su nombre de usuario es : " + nombreUsuario)
        while len(nombreUsuario) > 40:
            print("Ingresó un nombre de usuario que supera los 40 caracteres ")
            nombreUsuario = input("Ingrese el nombre de usuario,tiene que ser menor a 40 caracteres: ")
            if len(nombreUsuario) < 40:
                print("Su nombre de usuario es : " + nombreUsuario)
        nombreArchivo = input("Ingrese el nombre del archivo que quiere abrir: ")
        try:
            f = open (nombreArchivo)
        except IOError:
            print("No existe este archivo")
            error = True
            print("Ingresó un nombre de archivo incorrecto")
        while buscar and error == True:
            nombreArchivo = input("Ingrese el nombre del archivo que quiere abrir: ")
            try:
                f = open (nombreArchivo)
                error = False
            except IOError:
                print("No existe este archivo")
        return nombreUsuario,nombreArchivo


class Juego(Programa):
    matriz = 0
    listaPalabras = []
    listaPalabrasEncontradas = []
    palabra = 0
    def imprimir_juego(self,nombreArchivo):
        self.matriz = Tablero.imprimir(self,nombreArchivo)
    def guardar_palabras(self,nombreArchivo):
        with open(nombreArchivo+"Solucion") as archivo:
            lector1 = csv.DictReader(archivo)
            for linea3 in lector1:
                self.listaPalabras.append(linea3["Palabra"])
    def ingresar_palabra(self,nombreArchivo,nombreJugador):
        print("Estas son las palabras que quedan por encontrar:")
        for x in self.listaPalabras:
            print(x)            
        encontrePalabra = False
        palabra = input("Ingrese la palabra que encontró o ingrese la palabra fin si quiere terminar el juego: ")
        if palabra == "fin":
            print("Las palabras no encontradas son: ")
            self.listaPalabras.sort()
            for k in self.listaPalabras:
                print(k)
            self.listaPalabras = []
        DatosTablero = Tablero.encontrar_palabra(self,nombreArchivo,palabra,self.matriz)
        encontrePalabra = DatosTablero[0]
        if encontrePalabra:
            self.listaPalabras.remove(palabra)
            self.listaPalabrasEncontradas.append(palabra)
            Jugador.sumar_punto(self)
        
        return self.listaPalabras,self.listaPalabrasEncontradas
class Tablero(Juego):
    def imprimir(self,nombreArchivo):
        linea1 = []
        with open(nombreArchivo) as archivo:
            lector = csv.reader(archivo)
            for linea in lector:
                print(*linea,sep =' | ')
                linea1.append(linea)
        return linea1
    def encontrar_palabra(self,nombreArchivo,palabra,matriz):
        with open(nombreArchivo+"Solucion") as archivo:
            encontre = False
            lector1 = csv.DictReader(archivo)
            for linea2 in lector1:
                if linea2["Palabra"] == palabra:
                    print("Ha encontrado la palabra!")
                    longitudPalabra = len(palabra) - 1 
                    if linea2["x_inicial"] == linea2["x_final"]:
                        while longitudPalabra >=0: 
                            matriz[int(linea2["y_inicial"])+longitudPalabra][int(linea2["x_inicial"])] = palabra[longitudPalabra].upper()
                            longitudPalabra = longitudPalabra - 1
                    if linea2["y_inicial"] == linea2["y_final"]:
                        while longitudPalabra >=0:
                            matriz[int(linea2["y_inicial"])][int(linea2["x_inicial"])+longitudPalabra] = palabra[longitudPalabra].upper()
                            longitudPalabra = longitudPalabra - 1
                    encontre = True
            if encontre == False:
                print("Esa palabra no esta presente en el tablero")     
        for linea in matriz:
            print(*linea,sep =' | ')
        return encontre,palabra

class Jugador(Juego):
    puntos = 0
    def sumar_punto(self):
        self.puntos = self.puntos + 1
    def imprimir_puntaje(self):
        return self.puntos
programa2 = Programa()

programa2.main()