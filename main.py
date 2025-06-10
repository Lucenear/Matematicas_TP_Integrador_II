# Importamos las funciones de los archivos
import funciones.logica_dnis as log_dni
import funciones.logica_nacimiento as log_nacim

#Menu
def mostrar_menu():
    print("\n===== Menu Principal =====")
    print("1. Realizar operaciones con DNIs")
    print("2. Realizar operaciones con Años de Nacimiento")
    print("3. Salir")

    opcion = input("Selecciona una opcion (1, 2, 3): ")

    return opcion


#ejecutamos opcion seleccionada
def ejecutar_opcion(opcion):
    if opcion == "1":
        print("\n=== OPERACIONES CON DNIs ===")
        #ingresar DNI
        dnis = log_dni.ingresar_dn_is()

        #conjuntos de digitos unicos
        conjuntos = log_dni.crear_conjuntos(dnis)

        #operaciones entre conjuntos
        resultados_op = log_dni.calcular_operaciones(conjuntos)

        #suma de digitos y frecuencia
        sumas_digitos, frecuencias = log_dni.calcular_estadisticas(dnis)

        #Condiciones logicas
        condiciones = log_dni.evaluar_condiciones(conjuntos)
###
        #mostramos conjuntos generados
        print("\nConjuntos de digitos:")
        for persona, conjunto in conjuntos.items():
            print(f"{persona} = {conjunto}")

        #Mostramos las operaciones
        print("\nOperaciones entre conjuntos:")
        print("Union total:", resultados_op['union'])
        print("Interseccion total:", resultados_op['interseccion'])
        print("Diferencia A - E:", resultados_op['diferencia_AE'])
        print("Diferencia simetrica A △ E:", resultados_op['simetrica_AE'])

        #se comprueba digitos compartidos
        if condiciones['representativo']:
            digito_compartido = list(resultados_op['interseccion'])[0]
            print(f"Digito compartido: {digito_compartido}")
        else:
            print("No hay un digito compartido entre todos.")

        #Mostramos alta diversidad numerica
        print("Conjuntos con alta diversidad:", condiciones['alta_diversidad'])

        # Mostramos condición amplia
        print("Existe condicion de combinacion amplia?:", "Si" if condiciones['condicion_amplia'] else "No")

        #Mostramos la suma de los digitos
        print("\nSuma de los digitos por DNI:")
        for persona, suma in sumas_digitos.items():
            print(f"{persona}: {suma}")

        #mostramos cuantas veces aparece cada digito
        print("\nFrecuencia de cada digito por DNI:")
        for persona, freq in frecuencias.items():
            print(f"{persona}: {freq}")




    elif opcion == "2":
        print("\n=== OPERACIONES CON AÑOS DE NACIMIENTO ===")

        #Ingresamos nombres y años de nacimiento
        fechas = log_nacim.ingresar_fechas()

        #Calculo edades
        edades = log_nacim.grupo_edades(fechas)

        #Identificamos personas del grupo Z
        grupoZ = log_nacim.grupo_z(fechas)

        #Identifico personas de año bisiesto
        bisiestos = log_nacim.grupo_bisiesto(fechas)

        #Identificamos personas de año par
        pares = log_nacim.grupo_pares(fechas)

        # identificamos personas de año impar
        impares = log_nacim.grupo_impares(fechas)

        #mostramos producto cartesiano de la tupla
        cartesiano = log_nacim.producto_cartesiano(fechas, edades)

####

        #mostramos datos ingresados
        print("\nAños de nacimiento:", fechas)

        #mostramos edades
        print("Edades actuales:", edades)

        #mostramos grupo Z
        print("Integrantes en Grupo Z:", grupoZ)

        #Mostramos los de año bisiesto
        print("Integrantes nacidos en año bisiesto:", bisiestos)

        # Mostramos año par
        print("Personas nacidas en año par:", pares)

        #mostramos año impar
        print("Personas nacidas en año impar:", impares)

        #Mostramos producto cartesiano
        print("Producto cartesiano (año, edad):", cartesiano)


        # comprobamos si TODOS son del grupo Z
        if len(grupoZ) == 5:
            print("Grupo Z")
        else:
            print("No es un Grupo Z completo")

        # Comprobamos si hay algun año bisiesto
        if len(bisiestos) > 0:
            print("Tenemos un año especial")
        else:
            print("Ningun año bisiesto")

    # Sale del programa
    elif opcion == "3":
        print("Vuelva prontos!")
        exit()

    else:
        print("Intenta de nuevo por favor...1, 2 o 3")


#bucle recurrente de Menu
while True:
    opcion = mostrar_menu()
    ejecutar_opcion(opcion)