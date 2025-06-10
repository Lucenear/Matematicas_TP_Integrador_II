# funciones de logica relacionadas con el procesamiento de DNIs.

# Ingresamos DNIs
def ingresar_dn_is():
# diccionario vacio para guardar los DNIs
    dnis = {}

# etiquetas de las personas
    etiquetas = ["A", "B", "C", "D", "E"]

#reccorro cada etiqueta:
    for etiqueta in etiquetas:
        while True:
            # validamos que sean solo 8 digitos?
            entrada = input(f"Ingrese el DNI de la persona {etiqueta} (solo números): ")

            # Verificamos que sea un numero. Se comenta filtro de cant de digitos
            if entrada.isdigit(): #and len(entrada) == 8:
                #guardo el dni
                dnis[etiqueta] = int(entrada)
                break
            else:
                print("DNI invalida. Deben ser solo digitos numericos")

    #retorno el diccionario con los dnis
    return dnis


# creacion de conjuntos
def crear_conjuntos(dnis):
# creo diccionario vacio para guardar los conjuntos
    conjuntos = {}

    #reccorro cada persona y dni
    for persona, dni in dnis.items():
        # Convertimos los digitos en numeros y se guarda en el diccionario
        # tomado del codigo de thiago. validar si elimina duplicados
        conjuntos[persona] = set(int(d) for d in str(dni))

    #retorno los resultados del conjunto
    return conjuntos


# operaciones con los conjuntos
def calcular_operaciones(conjuntos):
    #asignamos variables a cada conjunto
    A = conjuntos["A"]
    B = conjuntos["B"]
    C = conjuntos["C"]
    D = conjuntos["D"]
    E = conjuntos["E"]

    # Union: todos los digitos que aparecen en alguno de los conjuntos
    union_total = A | B | C | D | E

    # Interseccion: digitos comunes en los conjuntos
    interseccion_total = A & B & C & D & E

    # Diferencia: elementos que estan en A pero no en E
    #Generamos los siguientes conjuntos?
    diferencia_AE = A - E

    # Diferencia simetrica: elementos que estan en A o E
    simetrica_AE = A ^ E

    # Devuelvo los resultados de las opraciones
    return {
        'union': union_total,
        'interseccion': interseccion_total,
        'diferencia_AE': diferencia_AE,
        'simetrica_AE': simetrica_AE
    }


#Calculo de la frecuencia de cada digito...revisar logica
def calcular_estadisticas(dnis):
    #guardo en diccionario la suma de los digitos
    sumas_digitos = {}

    #diccionario para guardar la frecuencia de cada digito
    frecuencias = {}

    #recorrro las pernosas y sus dnis
    for persona, dni in dnis.items():

        #convertimos los digitos en string
        digitos = list(str(dni))

        #sumo los digitos
        suma = sum(int(digito) for digito in digitos)

        # guardamos la suma para esta persona
        sumas_digitos[persona] = suma

        # creamos un diccionario para contar las veces aparece cada digito
        freq = {}
        for digito in digitos:
            # Si ya existe aumenta el contador
            if digito in freq:
                freq[digito] += 1
            else:
                freq[digito] = 1

        # se guardan las frecuencias
        frecuencias[persona] = freq

    #devuelvo la suma y frecuencia
    return sumas_digitos, frecuencias


#Condiciones logicas
def evaluar_condiciones(conjuntos):
    #listo nombres de conjuntos => 6 digitos
    alta_diversidad = [nombre for nombre, conjunto in conjuntos.items() if len(conjunto) >= 6]

    #lo tomo de Thiago. Condicion amplia:
    #A tiene más digitos que B
    # Alguno de los digitos de C es impar
    condicion_amplia = len(conjuntos["A"]) > len(conjuntos["B"]) and any(x % 2 != 0 for x in conjuntos["C"])

    # compruebo si existe digito comun a todos los conjuntos
    representativo = len(conjuntos["A"] & conjuntos["B"] & conjuntos["C"] & conjuntos["D"] & conjuntos["E"]) == 1

    # devuelvo resultados de las condiciones...faltan?
    return {
        'alta_diversidad': alta_diversidad,
        'condicion_amplia': condicion_amplia,
        'representativo': representativo
    }