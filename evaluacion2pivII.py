#Yohnbel Rodriguez
# C.I. 27.474.805

''' 
ELABORAR UNA TIENDA DE PRODUCTOS

1.	La tienda tiene un alrededor de 5 productos, los cuales se identifican por código, nombre y cantidad. +
2.	Cada producto se registra, en el caso que este exista se le adiciona al monto anterior. 
3.	Aunado a lo anterior, existe el proceso de venta del artículo, el cual consiste pedir el código del producto y la cantidad a 
comprar (esta no puede exceder el total en el stock), al finalizar deberá mostrar el producto que se compró y el precio total.
4.	Notificar si el producto está o no vacío. +
5.	Esto debe funcionar para n cantidad de clientes.
6.	Importante: debe validar todo lo que sea necesario

'''

class Tienda():
    #ATRIBUTOS

    codigo=''
    nombre=''
    cantidad=''

    #crear un diccionario para los articulo
    art={}

    #CONSTRUCTOR
    def _init_(self):
        print('¡BIENVENIDO!')

    #PEDIR LOS DATOS
    def RegistrodeProductos(self):
        repetir = True #PERMITIR QUE SE REPITA SI INGRESA UNA DATO VACIO
        while repetir == True:
            self.codigo=input('Ingrese el código del producto: ')
            self.nombre=input('Ingrese el nombre del producto: ')
            self.cantidad=int(input('Ingrese la cantidad de productos: ')) 

            if self.codigo == '' and self.cantidad == '':
                print('Los campos no pueden estar vacios, intente nuevamente.')
                repetir=True
            else:
                repetir=False

        self.art=dict(codigo=self.codigo, nombre=self.nombre)
        return self.art

Tienda.RegistrodeProductos()


#     def AgregarProducto(self):
#         for codigo in self.art():
#             if codigo == codigo:
#                 self.art.append(codigo) 
