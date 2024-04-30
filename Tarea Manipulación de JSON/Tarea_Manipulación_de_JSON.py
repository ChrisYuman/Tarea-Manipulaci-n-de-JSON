import os
import json

# Ruta del archivo
ruta = r"C:\Users\Chris\Downloads\Json pruebas\tarea.json"

# Datos estructurados
datos = [
    {
       "id": "1",
       "nombre": "Gorra roja",
       "precio": 100,
       "cantidad": 5,
       "categoria": "Ropa"
    },
    {
       "id": "2",
       "nombre": "Camisa",
       "precio": 100,
       "cantidad": 10,
       "categoria": "Ropa"
    },
    {
       "id": "3",
       "nombre": "Jordan 1",
       "precio": 1650,
       "cantidad": 2,
       "categoria": "Zapatos"
    },
    {
       "id": "4",
       "nombre": "Control",
       "precio": 840,
       "cantidad": 1,
       "categoria": "Electrodomesticos"
    },
    {
       "id": "5",
       "nombre": "Audifonos",
       "precio": 1840,
       "cantidad": 1,
       "categoria": "Electrodomesticos"
    },
    {
       "id": "6",
       "nombre": "Teclado",
       "precio": 1963,
       "cantidad": 4,
       "categoria": "Electrodomesticos"
    },
    {
       "id": "7",
       "nombre": "Pantalon",
       "precio": 240,
       "cantidad": 1,
       "categoria": "Ropa"
    },
    {
       "id": "8",
       "nombre": "Jordan 4",
       "precio": 1840,
       "cantidad": 1,
       "categoria": "Zapatos"
    },
    {
       "id": "9",
       "nombre": "Sueter",
       "precio": 1040,
       "cantidad": 1,
       "categoria": "Ropa"
    },
    {
       "id": "10",
       "nombre": "Gorra",
       "precio": 340,
       "cantidad": 1,
       "categoria": "Ropa"
    },
    {
       "id": "11",
       "nombre": "Nintendo Switch",
       "precio": 4840,
       "cantidad": 1,
       "categoria": "Electrodomesticos"
    },
    {
       "id": "12",
       "nombre": "Play 5",
       "precio": 6840,
       "cantidad": 1,
       "categoria": "Electrodomesticos"
    },
    {
       "id": "13",
       "nombre": "New balans",
       "precio": 2840,
       "cantidad": 1,
       "categoria": "Zapatos"
    },
    {
       "id": "14",
       "nombre": "Control play 4",
       "precio": 840,
       "cantidad": 1,
       "categoria": "Electrodomesticos"
    },
    {
       "id": "15",
       "nombre": "Control play 5",
       "precio": 1840,
       "cantidad": 1,
       "categoria": "Electrodomesticos"
    },
    {
       "id": "16",
       "nombre": "3DS",
       "precio": 5725,
       "cantidad": 1,
       "categoria": "Electrodomesticos"
    },
    {
       "id": "17",
       "nombre": "Sueter X EMINEM",
       "precio": 840,
       "cantidad": 1,
       "categoria": "Ropa"
    },
    {
       "id": "18",
       "nombre": "MADKAT Sueter",
       "precio": 1840,
       "cantidad": 1,
       "categoria": "Ropa"
    },
    {
       "id": "19",
       "nombre": "Control Xbox 360",
       "precio": 545,
       "cantidad": 1,
       "categoria": "Electrodomesticos"
    },
    {
       "id": "20",
       "nombre": "Monitor",
       "precio": 4840,
       "cantidad": 1,
       "categoria": "Electrodomesticos"
    },
]

# Crear el archivo JSON
with open(ruta, "w") as archivoJson:
    json.dump(datos, archivoJson, indent=2)

# Leer el archivo JSON
def cargarArchivos(archivoJson):
    if os.path.exists(archivoJson):
        with open(archivoJson, "r") as archivo:
            datos = json.load(archivo)
    else:
        datos = []
    return datos

## FUNCIONES

# Función para filtrar productos
def filtrarProductos(datos, categoria=None, stock_min=0, precio_max=float('inf')):
    productos_filtrados = []
    for producto in datos:
        if (not categoria or producto['categoria'] == categoria) and \
           producto['cantidad'] > stock_min and \
           producto['precio'] < precio_max:
            productos_filtrados.append(producto)
    return productos_filtrados

# Función para ordenar productos
def ordenarProductos(datos, clave='precio', ascendente=True):
    return sorted(datos, key=lambda x: x[clave], reverse=not ascendente)

# Imprimir los datos
def imprimirProductos(productos):
    for producto in productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}, Categoria: {producto['categoria']}")
    print()

# Cargar los datos del archivo
datosProductos = cargarArchivos(ruta)

# Filtrar y mostrar únicamente los productos que pertenezcan a una categoría específica, que los productos tengan un stock mayor a 0 o que tengan un precio menor a cierto valor
productos_filtrados = filtrarProductos(datosProductos, categoria='Ropa', stock_min=0, precio_max=1000)
print("Productos filtrados por categoria 'Ropa', stock mayor a 0 y precio menor a 1000:")
imprimirProductos(productos_filtrados)

# Ordenar y mostrar los productos de acuerdo al precio ascendente
productos_ordenados = ordenarProductos(datosProductos, clave='precio', ascendente=True)
print("Productos ordenados por precio ascendente:")
imprimirProductos(productos_ordenados)