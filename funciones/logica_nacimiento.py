# Importo libreria para tener fecha actual
from datetime import datetime as fecha_actual

# Se ingresan los nombre y a;o de nacimiento de los 5
def ingresar_fechas():
    # Creo diccionaria para guradar los datos
    fechas = {}

    #Reccoro y pido los los datos 
    for _ in range(5):
        nombre = input("Ingressa el nombre del integrante: ")

        while True:
            año = input(f"Indique el año de nacimiento de {nombre}: ")

            #valido digitos y rango de 1950 a actualidad
            if año.isdigit() and 1950 <= int(año) <= fecha_actual.now().year:
                # guardo el año
                fechas[nombre] = int(año)
                break
            else:
                print("Año inválido. Debe ser un número entre 1900 y el año actual.")

    #Devuelvo resultados
    return fechas


#identificar grupo Z
def grupo_z(fechas):
    #Creo diccionario para el grupo Z
    grupo_Z = {}

    #recorremos persona y fecha
    for nombre, año in fechas.items():
        #si nacion despues del 2000, lo agrego
        if año > 2000:
            grupo_Z[nombre] = año

    #retorno valores
    return grupo_Z


#año bisiesto
def es_bisiesto(año):
    #calculo: divisible por 4y no por 100 O divisible por 400
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)


#busco nacidos en año bisiesto
def grupo_bisiesto(fechas):
    #creo diccionario
    grupo_especial = {}

    #recorremos personas y años
    for nombre, año in fechas.items():
        if es_bisiesto(año):
            grupo_especial[nombre] = año

    #retorno resultados
    return grupo_especial


#personas en año par
def grupo_pares(fechas):
    #creamos diccionario
    grupo_par = {}

    #Recorremos personas y años de nacimiento
    for nombre, año in fechas.items():
        #si el año es par lo agregamos al grupo
        if año % 2 == 0:
            grupo_par[nombre] = año

    #retorno valores
    return grupo_par


# personas en año impar
def grupo_impares(fechas):
    #Creamos diccionario
    grupo_impar = {}

    #recorremos personas y año de nacimiento
    for nombre, año in fechas.items():
        #Si el año es impar lo agrego al grupo
        if año % 2 != 0:
            grupo_impar[nombre] = año

    # Retorno valores
    return grupo_impar


#calculo edades...me sirve para el producto cartesiano
def grupo_edades(fechas):
    #obtenemos fecha actual
    año_actual = fecha_actual.now().year

    #Creamos diccionario
    edades = {}

    # Reccorremos personas y fecha de nacimento
    for nombre, año in fechas.items():
        #Calculamos edades
        edades[nombre] = año_actual - año

    # retorno valores
    return edades


#Generamos producto cartesiano
def producto_cartesiano(fechas, edades):
    # Extraemos solo los valores para crear los conjuntos de (años y edades)
    lista_fechas = set(fechas.values())  # {1977, 2000, 2001, 2003}
    lista_edades = set(edades.values())  # {22, 24, 25, 48}
    resultado = []
    # Producto cartesiano entre años y edades
    for fecha in lista_fechas:
        for edad in lista_edades:
            resultado.append((fecha, edad))
    return resultado
