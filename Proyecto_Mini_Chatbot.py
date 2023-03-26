import time
import random
from colorama import *
WAIT_TIME = 1

Nombre_Usuario = input(
    f"{Fore.MAGENTA}Antes de comenzar el proyecto, indicame tu nombre: ")
time.sleep(0.5)
print(f"{Fore.LIGHTWHITE_EX}¡Hola {Nombre_Usuario}!")
time.sleep(0.9)
print("¡Mi nombre es Lita!")
time.sleep(1)
print("Soy una inteligencia artificial.\nMi propósito es entretenerte mediante pequeñas actividades.")
time.sleep(3)
print("Esto es un proyecto con el fin de aplicar las habilidades de mi creador.")
time.sleep(2)
print("Bien, comencemos con una apuesta, ahora te explicaré en que tratará.")
time.sleep(4)

print(
    f"""
Calcularé cualquier número que me digas y lo súmare, restaré, multiplicare, dividiré e incluso potenciaré si tu quieres.{Fore.LIGHTCYAN_EX}

·Si me equivoco en el resultado entonces ganarás tu.
·Si no es así entonces gano yo.{Fore.RESET}
""")

time.sleep(4)


def calculadora():

    try:
        N1_CALCULADORA = float(
            input(f"{Fore.CYAN}Indica los primeros digitos: "))
        N2_CALCULADORA = float(
            input(f"{Fore.CYAN}Ingresa los segundos digitos: "))
        returMessage = ":)"
        print(f"""{Fore.LIGHTWHITE_EX}

        ¿Qué quieres hacer con esos números?

        1) SUMARLOS
        2) RESTARLOS
        3) MULTIPLICARLOS
        4) DIVIDIRLOS
        5) PONTENCIARLOS
        """)

        Respuesta = int(
            input(f"{Fore.CYAN}Selecciona la opción que quieres (1-5): "))
        if Respuesta < 1:
            print(F"{Fore.RESET}Mi amor, te indiqué opciones del 1 al 5 (1-5) :)")
        elif Respuesta >= 6:
            print(f"{Fore.RESET}Cariño mio, te indiqué opciones del 1 al 5 (1-5) :)")
        elif Respuesta == 1:
            print(
                f"{Fore.RESET}La suma de {N1_CALCULADORA} + {N2_CALCULADORA} es igual a: {N1_CALCULADORA+N2_CALCULADORA:}")
        elif Respuesta == 2:
            print(
                f"{Fore.RESET}La resta {N1_CALCULADORA} - {N2_CALCULADORA} es igual a: {N1_CALCULADORA-N2_CALCULADORA}")
        elif Respuesta == 3:
            print(
                f"{Fore.RESET}La multiplicación de {N1_CALCULADORA} multiplicado por {N2_CALCULADORA} es igual a: {N1_CALCULADORA*N2_CALCULADORA}")
        elif Respuesta == 4:
            print(
                f"{Fore.RESET}La división de {N1_CALCULADORA} dividido entre {N2_CALCULADORA} es igual a: {N1_CALCULADORA/N2_CALCULADORA}")
        elif Respuesta == 5:
            print(
                f"{Fore.RESET}La potencia de {N1_CALCULADORA} elevado a {N2_CALCULADORA} es igual a: {N1_CALCULADORA**N2_CALCULADORA}")
    except ValueError:
        returMessage = ":/"
        print(
            f"{Fore.RESET}Coloca N-Ú-M-E-R-O-S. Es una calculadora. Se necesitan N-Ú-M-E-R-O-S")
        time.sleep(3)
        print("Acabas de bugear el código. Mi desarollador aún no sabe como solucionar este error. ")
        time.sleep(3)
        print("Santo dios")
        time.sleep(1)
        print("¿De verdad?\nTenías que poner letras en donde se pedía claramente")
        time.sleep(1.5)
        print(f"{Fore.GREEN}N-Ú-M-E-R-O-S")
        time.sleep(1.7)
        print(f"{Fore.RESET}Ahora te dejaré con el resto de código.")
        time.sleep(2)

    return returMessage


time.sleep(2)
print(calculadora())
try:
    time.sleep(2)
    EstoyEnLoCorrecto = input(
        "¿Estoy en lo correcto? (si/no): ").strip().lower().upper().capitalize().swapcase()
    if EstoyEnLoCorrecto == "si".strip().lower().upper().capitalize().swapcase():
        print("Jaja, lo sabía. Gane yo.")
    elif EstoyEnLoCorrecto == "no".strip().lower().upper().capitalize().swapcase():
        print("Si claro. Ya se que estoy en lo correcto :/ .")
        EstoyEnLoCorrecto = input(
            "De todas maneras ¿Deseas repetir el calculo? (si/no): ").strip().lower().upper().capitalize().swapcase()
        if EstoyEnLoCorrecto == "si".strip().lower().upper().capitalize().swapcase():
            print("Pues haremos el ejercicio de nuevo.")
            time.sleep(1)
            print(calculadora())
        elif EstoyEnLoCorrecto == "no".strip().lower().upper().capitalize().swapcase():
            print("Piola")
except ValueError:
    print("imbecil, hiciste algo mal")

print("Okay, esta fue la primera actividad.")
time.sleep(1.5)
print("Tal vez no lo notaste pero lo que acabamos de responder tenía diferentes caminos")
time.sleep(3)
print("(Puede ser que estas en esta parte porque haz bugeado el codigo pero bueno.)")
time.sleep(4)
print("A tal punto de que tengo 100 líneas de código escritas.")
time.sleep(1.5)
print("Lo peor que vamos por la primera actividad")
time.sleep(3)

print("Bien ahora seguiremos con la segunda actividad.")
time.sleep(2)
print("En esta actividad tu no tendrás que hacer nada.")
time.sleep(3)
print("Esta actividad consiste en que yo te crearé una contraseña totalmente segura y aleatoria de 12 digitos.")
time.sleep(5)
print("Comencemos.")


def Generador_de_contraseñas(longitud=12):
    Letras_Minusculas = "abcdefghijklmnñopqrstuvwxyz"
    Letras_Mayusculas = Letras_Minusculas.upper()
    simbolos = "@#€$%&="
    numeros = "1234567890"
    base = Letras_Minusculas+Letras_Mayusculas+simbolos+numeros
    muestra = random.sample(base, longitud)
    contraseña = "".join(muestra)
    return contraseña


time.sleep(5)
print(
    f"Tu contraseña generada es: {Fore.LIGHTMAGENTA_EX}{Generador_de_contraseñas()}")
time.sleep(1.5)
print(f"{Fore.RESET}Ahora haremos algo que lo va volver algo mas interesante.")
time.sleep(2)
Longitud_Contraseña = int(input(
    f"Indicame la longitud que quieres que tenga tu nueva y opcional contraseña. {Fore.RED}NUMEROS DEL 1 AL 50: "))
time.sleep(2)

if Longitud_Contraseña >= 1 and Longitud_Contraseña <= 50:
    print(
        f"{Fore.RESET}Tu contraseña generada es: {Fore.LIGHTMAGENTA_EX}{Generador_de_contraseñas(Longitud_Contraseña)}{Fore.RESET}")
elif Longitud_Contraseña <= 0:
    print(f"{Fore.RESET}Te dije que era del 1 al 50.")
    time.sleep(1)
    print(f"{Fore.RESET}Ahora te quedarás sin contraseña, idiota.")
elif Longitud_Contraseña >= 51:
    print(f"{Fore.RESET}Te acabo de mencionar que eran del 1 al 50.")
    time.sleep(1)
    print(f"{Fore.RESET}Ahora te quedarás sin contraseña. Por idiota.")


def VideoJuego():
    Vidas_Usuario = 3
    Numero_Aleatorio = random.randint(1, 10)
    while True:
        try:
            print(f"{Fore.LIGHTGREEN_EX}Continuemos con el juego: {Fore.RESET}")
            print(f"""{Fore.LIGHTBLUE_EX}Elige la opción que quieres:

                        1) INGRESAR AL JUEGO
                        2) SALIR
                        {Fore.RESET}""")
            opciones = int(input(
                f"{Fore.LIGHTGREEN_EX}Ingresa la opción que desees: {Fore.RESET} "))
        except ValueError:
            time.sleep(WAIT_TIME)
            print("Dios santo...")
            time.sleep(2)
            print(f"{Fore.RED}A la próxima coloque números.{Fore.RESET}")
            time.sleep(3)
            return

        if opciones == 1:
            try:
                for Vidas_Fallidas in range(1, Vidas_Usuario+1):
                    time.sleep(1)
                    Numero_Usuario = int(
                        input("Selecciona un número de 1 al 10: "))
                    if Numero_Usuario == Numero_Aleatorio:
                        print(
                            f"¡Felicidades, lo hiciste en {Vidas_Fallidas} intentos!")
                        time.sleep(1)
                        repeticion = input("""
                        ¿Quieres repetirlo? (si/no)
                        """).strip().lower()

                        if repeticion == "si":
                            print("¡Así será!")
                            time.sleep(WAIT_TIME)
                            VideoJuego()
                        elif repeticion == "no":
                            time.sleep(WAIT_TIME)
                            print("¡Okay!")
                            time.sleep(WAIT_TIME)
                            print("¡Adiós!")
                            return
                    elif Numero_Usuario > Numero_Aleatorio:
                        print("El número que buscas adivinar es más pequeño <3")
                    else:
                        print("El número que buscas es más grande <3")
            except ValueError:
                print(f"{Fore.RED} Coloque caracteres válidos.")

            if Numero_Usuario != Numero_Aleatorio:
                time.sleep(1)
                print("Vaya...")
                time.sleep(1)
                print("Tik..")
                time.sleep(2)
                print("¡TAK!")
                time.sleep(1)
                print(f"{Fore.RED}¡Tus vidas se acabarón! {Fore.RESET}")
                print(f"El númeor era {Numero_Aleatorio}")
                time.sleep(1.9)
                print("¿Quieres repetirlo? (si/no): ")
                opciones_siandno = (input("Selecciona si o no: ")).strip(
                ).lower().upper().capitalize().swapcase()
                if opciones_siandno == "si".strip().lower().upper().capitalize().swapcase():
                    time.sleep
                    print("Que así sea.")
                    time.sleep(1)
                    VideoJuego()
                elif opciones_siandno == "no".strip().lower().upper().capitalize().swapcase():
                    time.sleep(WAIT_TIME)
                    print("Okay")
                    time.sleep(WAIT_TIME)
                    print("¡Adiós!")
                    return

        elif opciones == 2:
            time.sleep(2)
            print("¡Okay!")
            time.sleep(1)
            print("¡Adiós!")
            time.sleep(1)
            return
        elif opciones >= 3:
            time.sleep(3)
            print("Amigo, te dije solo opciones del 1 al 2 ;/")
            time.sleep(2)
        elif opciones < 1:
            time.sleep(2)
            print("Amigo, te dije solo opciones del 1 al 2 ;/")
            time.sleep(2)


time.sleep(4)
print("Bien.\nEste fue la actividad 2.")
time.sleep(1.5)
print("Ahora pasaremos a la actividad 3.")
time.sleep(1.5)
print(f"Bien {Nombre_Usuario}.")
time.sleep(2)
print("Jugaremos a un juego. Ahora te diré en que consiste:")
time.sleep(3)
print(f"""{Fore.CYAN}
    ·Tienes 3 vidas.
    ·Tienes que adivinar un número del 1 al 10.
    ·Cada vez que fallas se te resta 1 vida
    {Fore.RESET}
    """)
time.sleep(5)
print("¿Facil verdad?")
time.sleep(0.5)
print("Estas especies de mini actividades estan hechas con el fin de pulir las habilidades de mi desarrolador.")
time.sleep(3)
VideoJuego()
time.sleep(2)
print("Espero que te haya gustado")
time.sleep(2)
print("Ahora seguiremos con la actividad 4")
time.sleep(3)
print(f"""
Consistirá en los siguiente:{Fore.LIGHTCYAN_EX}

·Pasaré kilómetros a millas
·Pasaré Grados Celcius a Grados Fahrenheit
·Solo me tienes que indicar que opción de las 2 queires y indicarme también el número de kilómetros o de grados Celcius
{Fore.RESET}
      
""")
time(5)
while True:
    print(f"""

    {Fore.LIGHTRED_EX}1)CELCIUS --> FAHRENHEIT{Fore.RESET}
    {Fore.MAGENTA}2)KILÓMETROS --> MILLAS{Fore.RESET}

    """)
    try:
        Opciones_C_K = int(
            input("Ingresa 1 o 2 dependiendo de lo que desees: "))
        if Opciones_C_K == 1:
            time.sleep(2)
            celcius = float(
                input("Ingresa los grados celcius que serán pasados a fahrenheit: "))
            fahrenheit = celcius * 1.8 + 32
            resultado_fahrenheit = (
                f"{celcius} grados celcius a grados Fahrenheit són: {fahrenheit} grados fahrenheit.")
            print(resultado_fahrenheit)
            time.sleep(4)
            message_repeat = input(
                "¿Quieres repetirlo denuevo? (Si/No): ").strip().lower()
            if message_repeat == "Si".strip().lower():
                time.sleep(2)
                print("Que así sea.")
                time.sleep(2)
            elif message_repeat == "no".strip().lower():
                time.sleep(2)
                print("¡Okay!")
                time.sleep(1)
                print("¡Adiós!")
                break
        elif Opciones_C_K == 2:
            time.sleep(2)
            km = float(
                input("Dime los kilómetros que serán pasados a millas: "))
            millas = km / 1.609
            resultado_millas = (
                f"{km} kilómetros a millas són: {millas} millas.")
            print(resultado_millas)
            time.sleep(2)
            message_repeat = input(
                "¿Quieres repetirlo denuevo? (Si/No): ").strip().lower()
            if message_repeat == "Si".strip().lower():
                time.sleep(2)
                print("Que así sea.")
                time.sleep(2)
            elif message_repeat == "no".strip().lower():
                time.sleep(2)
                print("¡Okay!")
                time.sleep(1)
                print("¡Adiós!")
                break
        elif Opciones_C_K < 1 or Opciones_C_K > 2:
            time.sleep(2)
            print("Te di a escoger entre 1 y 2, no entre otro número.")
            time.sleep(2)
    except ValueError:
        time.sleep(2)
        print(
            f"{Fore.RED}Error encontrado: Te dí a elegir entre números, no letras.{Fore.RESET}")
        time.sleep(2)

print(f"Bien {Nombre_Usuario}.")
time.sleep(WAIT_TIME)
print("")
