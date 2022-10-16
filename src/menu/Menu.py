from operator import itemgetter

from src.mensajes.Mensajes import Mensajes

class Menu():

    def __init__(self):
        self.mensajes = Mensajes()

    def principal(self):
        self.mensajes.mensaje_inicio()
    
        respuesta = None
        while respuesta != "salir":
            respuesta = input("Ingrese una opción: listar, buscar, agregar o salir: ")
            respuesta = respuesta.lower()
            if respuesta == "listar":
                self.listar()
            elif respuesta =="buscar":
                self.buscar()
            elif respuesta == "agregar":
                self.agregar()
            elif respuesta == "salir":
                self.salir()
            else:
                print("\nPor favor ingrese una respuesta correcta.\n")
        self.mensajes.mensaje_final()

    def leer_restaurantes(self):
        archivo = open("restaurante.txt", "r")
        lista = []
        for linea in archivo:
            linea_archivo = linea.split("-")
            lista.append(linea_archivo)
        archivo.close()
        return lista

    def imprimir_tabla_restaurantes(self,lista_restaurantes):
        if lista_restaurantes:
            encabezado = '{:>12}  {:>12}  {:>12}'.format('Nombre', 'Comida', 'Precio')
            print (encabezado)
            print ( "-"*45)
            for item in lista_restaurantes:
                item_precio = "$" + item [2]
                linea = '{:>12}  {:>12}  {:>12}'.format(item[0], item[1], item_precio)
                print (linea)
        else:
            print("\nNo se encontró una lista. \n")

    def listar(self):
        print("\n<<<Listar>>>\n")
        respuesta = None
        while respuesta != "salir":
            respuesta = input("Desea ordenar por nombre, comida o precio? (o salir para volver al menu principal): ")
            respuesta = respuesta.lower()
            lista_restaurantes = self.leer_restaurantes()
    # segun la respuesta ordena la lista por un indice especifico 
            if respuesta == "nombre":
                lista_restaurantes.sort(key=itemgetter(0))
                self.imprimir_tabla_restaurantes(lista_restaurantes)
            elif respuesta =="comida":
                lista_restaurantes.sort(key=itemgetter(1))
                self.imprimir_tabla_restaurantes(lista_restaurantes)
            elif respuesta == "precio":
                lista_restaurantes.sort(key=itemgetter(2))
                self.imprimir_tabla_restaurantes(lista_restaurantes)
            elif respuesta == "salir":
                print("\nSaliendo al menu principal..\n")
            else:
                print("\nPor favor ingrese una respuesta correcta.\n")


    def buscar(self):
        print("\n<<<Buscar>>>\n")
        respuesta = None
        while respuesta != "salir":
            respuesta = input("Ingrese el nombre del restaurante o la comida que desea buscar (o salir para volver al menu principal): ")
            respuesta = respuesta.lower()
            if respuesta != "salir":
                lista_restaurantes = self.leer_restaurantes()
                encontrado = []
                for item in lista_restaurantes:
                    if respuesta in item :
                        encontrado.append(item)

                if encontrado:
                    self.imprimir_tabla_restaurantes(encontrado)
                else:
                    print ("\nNo existen resultados.\n")


    def agregar(self):
        print("\n<<<Agregar>>>\n")
        restaurante = input ("Cual es el nombre del restaurante?: ")
        comida = input ("Que comida estas buscando?: ")
        precio = input ("Cual es el precio de la comida?: ")
        nueva_linea = str(restaurante.lower() + "-" + comida.lower() + "-" + precio + "\n")
        archivo = open("restaurante.txt",'a')
        archivo.write(nueva_linea)
        archivo.close
        print("\nSe ha agregado un nuevo restaurante con los siguientes datos:\nNombre: " + restaurante + "\nPlato: " + comida + "\nPrecio: " + precio + "\n")


    def salir(self):
        print ("\nSaliendo del sistema.\n")
