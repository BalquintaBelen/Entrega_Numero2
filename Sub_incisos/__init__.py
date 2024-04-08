#2. Conocer el nombre y la cantidad de goles del goleador o goleadora.

def Goles(datosJugadores): #datosJugadores es la lista de tuplas
    diccionario = {"Nombre": "", "Goles" : 0}
    for lista in datosJugadores:
        if(lista[1] > diccionario["Goles"]):
            diccionario["Nombre"] = lista[0]
            diccionario["Goles"] = lista[1]
    return diccionario

# Conocer el nombre del jugador o jugadora más influyente
def Influyente(dic,datosJugadores):
    # diccionario -->"GolesAFavor": 1.5, "GolesEvitados": 1.25, "Asistencias": 1
    dic2 = {"nombre": "", "suma_de_todo": 0}
    for lista in datosJugadores:
        golea_a_favor = lista[1] * dic["GolesAFavor"]
        goles_evitados = lista[2] * dic["GolesEvitados"]
        asistencias = lista[3]*dic["Asistencias"]
        sumaTodo = golea_a_favor + goles_evitados + asistencias
        if (sumaTodo > dic2["suma_de_todo"]):
            dic2["suma_de_todo"] = sumaTodo
            dic2["nombre"] = lista[0]
    return dic2


 #4. Conocer el promedio de goles por partido. Dato: Se jugaron 25 partidos en la temporada.   
def promedio (datosJugadores, total_partidos):
    # Esto haria la suma de los goles de todos los jugadores
    golesTotales = sum(map(lambda x: x[1],datosJugadores))  
    prom = golesTotales/ total_partidos
    return prom

#5. Conocer el promedio de goles por partido del goleador o goleadora. Dato: Se jugaron 25 partidos en la temporada.
def PromGolesJugador(ganador,total_partidos):
    # Recibe el nombre del jugador y su cantidad de goles
    prom = ganador["Goles"] / total_partidos    
    return prom