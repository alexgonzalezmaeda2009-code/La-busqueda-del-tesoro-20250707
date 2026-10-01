# ============================================================
# LA BÚSQUEDA DEL TESORO PERDIDO
# Juego desarrollado en Python
# ============================================================

# ---------------- VARIABLES GLOBALES ----------------
vidas = 3
puntaje = 0
inventario = []
nivel_actual = 1


# ---------------- FUNCIONES DEL JUEGO ----------------

def instrucciones():
    print("\n========================================")
    print("           INSTRUCCIONES")
    print("========================================")
    print("Eres un aventurero en busca de un tesoro perdido.")
    print("Debes explorar diferentes lugares para encontrar")
    print("llaves, pistas y herramientas.")

    print("\nDurante el juego debes:")
    print("- Explorar las zonas.")
    print("- Buscar objetos.")
    print("- Resolver acertijos.")
    print("- Luchar contra enemigos.")
    print("- Utilizar tu inventario.")
    print("- Encontrar el tesoro.")

    print("\nTienes 3 vidas.")
    print("Si pierdes todas tus vidas, pierdes el juego.")
    print("¡Buena suerte, aventurero!")


def mostrar_estado():
    print("\n----------------------------------------")
    print("VIDAS:", vidas)
    print("PUNTAJE:", puntaje)
    print("INVENTARIO:", inventario)
    print("----------------------------------------")


def explorar():
    global puntaje

    print("\n========================================")
    print("              EXPLORAR")
    print("========================================")
    print("Exploras cuidadosamente el lugar...")
    print("Encuentras algunas huellas y objetos antiguos.")

    puntaje += 10

    print("Has ganado 10 puntos.")
    mostrar_estado()


def buscar_objetos():
    global puntaje

    print("\n========================================")
    print("           BUSCAR OBJETOS")
    print("========================================")
    print("Buscas entre las piedras y los árboles.")
    print("Encontraste una poción.")

    inventario.append("Poción")
    puntaje += 15

    print("La Poción fue agregada al inventario.")
    print("Has ganado 15 puntos.")
    mostrar_estado()


def usar_inventario():
    global vidas

    print("\n========================================")
    print("           USAR INVENTARIO")
    print("========================================")

    if len(inventario) == 0:
        print("Tu inventario está vacío.")
        return

    print("Objetos disponibles:")

    for objeto in inventario:
        print("-", objeto)

    if "Poción" in inventario:
        print("\nPuedes utilizar una Poción para recuperar una vida.")

        respuesta = input("¿Quieres usar la Poción? (si/no): ")

        if respuesta.lower() == "si":
            vidas += 1
            inventario.remove("Poción")

            print("Has utilizado la Poción.")
            print("Recuperaste una vida.")

        else:
            print("No utilizaste ningún objeto.")

    else:
        print("No tienes una Poción para usar.")

    mostrar_estado()


def luchar_enemigo():
    global vidas
    global puntaje

    print("\n========================================")
    print("       LUCHAR CONTRA ENEMIGOS")
    print("========================================")
    print("¡Un enemigo apareció!")
    print("Debes elegir una estrategia.")

    print("\n1. Atacar")
    print("2. Defenderte")
    print("3. Huir")

    try:
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            print("\nAtacas al enemigo con valentía.")
            print("¡Derrotaste al enemigo!")

            puntaje += 30

            print("Ganaste 30 puntos.")

        elif opcion == 2:
            print("\nTe defiendes del ataque.")
            print("El enemigo te hizo daño.")

            vidas -= 1

            print("Perdiste una vida.")

        elif opcion == 3:
            print("\nLograste escapar del enemigo.")
            print("No ganaste puntos.")

        else:
            print("\nOpción no válida.")

    except ValueError:
        print("\nDebes ingresar un número.")

    mostrar_estado()


# ---------------- NIVEL 1 ----------------

def nivel_uno():
    global puntaje

    print("\n")
    print("########################################")
    print("#       NIVEL 1: BOSQUE MISTERIOSO    #")
    print("########################################")

    print("\nObjetivo: encontrar la primera llave.")
    print("Te encuentras en un bosque oscuro y misterioso.")
    print("Hay varios caminos para explorar.")

    llave_encontrada = False

    while not llave_encontrada and vidas > 0:

        print("\n¿Qué deseas hacer?")
        print("1. Explorar")
        print("2. Buscar objetos")
        print("3. Revisar inventario")
        print("4. Continuar")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                explorar()

            elif opcion == 2:
                buscar_objetos()

            elif opcion == 3:
                usar_inventario()

            elif opcion == 4:
                print("\nEncuentras unas huellas que conducen")
                print("hasta un árbol antiguo.")
                print("Detrás del árbol encuentras una llave.")

                inventario.append("Primera llave")
                puntaje += 50

                print("\n¡Encontraste la primera llave!")
                print("Has ganado 50 puntos.")

                llave_encontrada = True

            else:
                print("Opción no válida.")

        except ValueError:
            print("Debes ingresar un número.")

    if vidas <= 0:
        print("\nHas perdido todas tus vidas.")
        return False

    return True


# ---------------- NIVEL 2 ----------------

def nivel_dos():
    global puntaje
    global vidas

    print("\n")
    print("########################################")
    print("#         NIVEL 2: CUEVA OSCURA       #")
    print("########################################")

    print("\nObjetivo: resolver acertijos y evitar trampas.")
    print("Entras a una cueva oscura y peligrosa.")
    print("Para avanzar debes resolver un acertijo.")

    acertijo_resuelto = False

    while not acertijo_resuelto and vidas > 0:

        print("\n¿Qué deseas hacer?")
        print("1. Explorar la cueva")
        print("2. Resolver acertijo")
        print("3. Usar inventario")
        print("4. Luchar contra enemigo")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                print("\nExploras la cueva.")
                print("Encuentras una pequeña antorcha.")

                if "Antorcha" not in inventario:
                    inventario.append("Antorcha")
                    puntaje += 10
                    print("Has ganado 10 puntos.")
                else:
                    print("Ya tienes una antorcha.")

            elif opcion == 2:
                print("\n----------------------------------------")
                print("              ACERTIJO")
                print("----------------------------------------")
                print("Tengo hojas y no soy un árbol.")
                print("Tengo páginas y no soy un cuaderno.")
                print("¿Qué soy?")

                respuesta = input("Tu respuesta: ")

                if respuesta.lower().strip() == "libro":
                    print("\n¡Respuesta correcta!")
                    print("Has encontrado la salida de la cueva.")

                    puntaje += 50
                    acertijo_resuelto = True

                    inventario.append("Pista de la cueva")

                    print("Has ganado 50 puntos.")

                else:
                    print("\nRespuesta incorrecta.")
                    print("¡Caíste en una trampa!")

                    vidas -= 1

                    print("Perdiste una vida.")

            elif opcion == 3:
                usar_inventario()

            elif opcion == 4:
                luchar_enemigo()

            else:
                print("Opción no válida.")

        except ValueError:
            print("Debes ingresar un número.")

    if vidas <= 0:
        print("\nHas perdido todas tus vidas.")
        return False

    return True


# ---------------- NIVEL 3 ----------------

def nivel_tres():
    global puntaje

    print("\n")
    print("########################################")
    print("#         NIVEL 3: TEMPLO ANTIGUO     #")
    print("########################################")

    print("\nObjetivo: abrir la puerta secreta")
    print("y encontrar el tesoro.")

    puerta_abierta = False

    while not puerta_abierta and vidas > 0:

        print("\nLlegas frente a una enorme puerta antigua.")
        print("La puerta tiene una cerradura.")

        print("\n¿Qué deseas hacer?")
        print("1. Buscar una pista")
        print("2. Usar la primera llave")
        print("3. Explorar el templo")
        print("4. Luchar contra el enemigo")
        print("5. Revisar inventario")

        try:
            opcion = int(input("Elige una opción: "))

            if opcion == 1:
                print("\nEncuentras una inscripción en la pared.")
                print("La inscripción dice:")
                print('"La llave abre el camino hacia el tesoro."')

                if "Pista del templo" not in inventario:
                    inventario.append("Pista del templo")
                    puntaje += 10
                    print("Has ganado 10 puntos.")
                else:
                    print("Ya habías encontrado esta pista.")

            elif opcion == 2:

                if "Primera llave" in inventario:
                    print("\nUtilizas la Primera llave...")
                    print("La puerta comienza a abrirse.")
                    print("¡La puerta secreta está abierta!")

                    puerta_abierta = True
                    puntaje += 50

                else:
                    print("\nNo tienes la llave necesaria.")

            elif opcion == 3:
                explorar()

            elif opcion == 4:
                luchar_enemigo()

            elif opcion == 5:
                usar_inventario()

            else:
                print("Opción no válida.")

        except ValueError:
            print("Debes ingresar un número.")

    if vidas <= 0:
        print("\nHas perdido todas tus vidas.")
        return False

    return True


# ---------------- FINAL DEL JUEGO ----------------

def final_juego():

    print("\n")
    print("========================================")
    print("          ¡TESORO ENCONTRADO!")
    print("========================================")

    print("\nEntras a la habitación secreta...")
    print("Frente a ti aparece un enorme cofre.")
    print("Te acercas lentamente y lo abres.")

    print("\n¡ENCONTRASTE EL TESORO PERDIDO!")

    print("\nTu aventura ha terminado.")

    print("----------------------------------------")
    print("PUNTAJE FINAL:", puntaje)
    print("VIDAS RESTANTES:", vidas)
    print("OBJETOS:", inventario)
    print("----------------------------------------")

    print("\n★★★★★★★★★★★★★★★★★★★★")
    print("        ¡FELICIDADES!")
    print("★★★★★★★★★★★★★★★★★★★★")


# ---------------- JUEGO PRINCIPAL ----------------

def jugar():
    global vidas
    global puntaje
    global inventario

    vidas = 3
    puntaje = 0
    inventario = []

    print("\n")
    print("****************************************")
    print("*                                      *")
    print("*    LA BÚSQUEDA DEL TESORO PERDIDO    *")
    print("*                                      *")
    print("****************************************")

    print("\nEres un aventurero que explora")
    print("un laberinto en busca de un tesoro.")
    print("Debes sobrevivir hasta encontrarlo.")

    continuar = nivel_uno()

    if continuar:
        continuar = nivel_dos()

    if continuar:
        continuar = nivel_tres()

    if continuar:
        final_juego()

    else:
        print("\n========================================")
        print("                PERDISTE")
        print("========================================")
        print("La aventura terminó.")
        print("Puntaje obtenido:", puntaje)


# ---------------- MENÚ PRINCIPAL ----------------

opcion_menu = 0

while opcion_menu != 4:

    print("\n")
    print("========================================")
    print("           MENÚ PRINCIPAL")
    print("========================================")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Salir")
    print("4. Salir del programa")
    print("========================================")

    try:
        opcion_menu = int(input("Selecciona una opción: "))

        if opcion_menu == 1:
            jugar()

        elif opcion_menu == 2:
            instrucciones()

        elif opcion_menu == 3:
            print("\nGracias por jugar.")
            print("¡Hasta pronto!")
            opcion_menu = 4

        elif opcion_menu == 4:
            print("\nSaliendo del juego...")

        else:
            print("\nOpción no válida.")

    except ValueError:
        print("\nERROR: Debes ingresar un número.")