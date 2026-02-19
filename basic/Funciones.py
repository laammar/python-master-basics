# Modulo con las funciones utlizadas en mi codigo del juego El Solitario. Carlos Lara Marín 77767539P
#Ademas importamos las librerias necesarias. Este programa utiliza la libreria externa "pandas" para el manejo de ficheros Excel. Aunque en clase se usara openpyxl he preferido usar pandas por comodidad y porque vi que se utilizaba en la tarea de python avanzado.
#Aunque en jupiter ya venga instalada, si no estuviera instalada se podria instalar con: pip install pandas. EL resto no requieren instalación.

import pandas as pd
import os
import random
PartidasGanadaSolitarioFacil=0
PartidasGanadaSolitarioMedio=0
PartidasGanadaSolitarioDificil=0
PartidasGanadaDuoFacil=0
PartidasGanadaDuoMedio=0
PartidasGanadaDuoDificil=0
Puntuacion=0
PartidasJugadas=0
PartidasJugadasSolitario=0
PartidasJugadasDuo=0





# PRIMERA FUNCION: MENU
def Menu():
  print("\n" *2)
  print("=======================================")
  print("                  MENU PRINCIPAL")
  print("=======================================")
  print("1. Juego Solitario")
  print("2. Juego Dos Jugadores")
  print("3. Estadisticas")
  print("4. Salir")
  print("=======================================")

# SEGUNDA FUNCION: SUBMENU
def submenu():
  print("\n")
  print("---------------------------------------")
  print("                  DIFICULTAD")
  print("---------------------------------------")
  print("1. Facil (20 intentos)")
  print("2. Medio (12 intentos)")
  print("3. Dificil (5 intentos)")
  print("4. Salir")
  print("---------------------------------------")

# TERCERA FUNCION: MODO SOLITARIO
def Solitario():
  global PartidasGanadaSolitarioFacil
  global PartidasGanadaSolitarioMedio
  global PartidasGanadaSolitarioDificil
  global PartidasJugadas
  global PartidasJugadasSolitario
  global Puntuacion

  NumeroAleatorio=random.randint(1,1000)
  submenu()
  opcion=Valida(1,4)
  if opcion == 1:
    PartidasJugadas=PartidasJugadas+1
    PartidasJugadasSolitario=PartidasJugadasSolitario+1
    intentos=20
    resultado = "PERDIDA"
    puntos_partida = 0
    while intentos>0:
      numero=int(input("Escriba un numero: "))
      if numero==NumeroAleatorio:
        PartidasGanadaSolitarioFacil=PartidasGanadaSolitarioFacil+1
        Puntuacion=Puntuacion+100
        puntos_partida = 100
        resultado = "GANADA"
        print("\n==================================")
        print("                    !!HAS GANADO!!")
        print("==================================")
        print("El numero era...... ",NumeroAleatorio)
        nombre = input("Introduce tu nombre: ")
        GuardarPartida(nombre, "Duo", "Dificil", resultado, puntos_partida, intentos)
        break
      elif numero>NumeroAleatorio:
        print("\nEl numero a adivinar es menor ↓")
      elif numero<NumeroAleatorio:
        print("\nEl numero a adivinar es mayor ↑")


      intentos= intentos -1
      print("Te quedan", intentos, "intentos")

    if resultado == "PERDIDA":
      print("HAS PERDIDO")
      nombre = input("Introduce tu nombre: ")
      GuardarPartida(nombre, "Solitario", "Facil", resultado, puntos_partida, intentos)



  if opcion == 2:
    PartidasJugadas=PartidasJugadas+1
    PartidasJugadasSolitario=PartidasJugadasSolitario+1
    intentos=12
    resultado = "PERDIDA"
    puntos_partida = 0
    while intentos>0:
      numero=int(input("Escriba un numero: "))
      if numero==NumeroAleatorio:
        PartidasGanadaSolitarioMedio=PartidasGanadaSolitarioMedio+1
        Puntuacion=Puntuacion+170
        puntos_partida = 170
        resultado = "GANADA"
        print("\n==================================")
        print("                    !!HAS GANADO!!")
        print("==================================")
        print("El numero era...... ",NumeroAleatorio)

        nombre = input("Introduce tu nombre: ")
        GuardarPartida(nombre, "Duo", "Dificil", resultado, puntos_partida, intentos)
        break
      elif numero>NumeroAleatorio:
        print("\nEl numero a adivinar es menor ↓")
      elif numero<NumeroAleatorio:
        print("\nEl numero a adivinar es mayor ↑")


      intentos= intentos -1
      print("Te quedan", intentos, "intentos")

    if resultado == "PERDIDA":
      print("HAS PERDIDO")
      nombre = input("Introduce tu nombre: ")
      GuardarPartida(nombre, "Solitario", "Medio", resultado, puntos_partida, intentos)


  if opcion == 3:
    PartidasJugadas=PartidasJugadas+1
    PartidasJugadasSolitario=PartidasJugadasSolitario+1
    intentos=5
    resultado = "PERDIDA"
    puntos_partida = 0
    while intentos>0:
      numero=int(input("Escriba un numero: "))
      if numero==NumeroAleatorio:
        PartidasGanadaSolitarioDificil=PartidasGanadaSolitarioDificil+1
        Puntuacion=Puntuacion+400
        puntos_partida = 400
        resultado = "GANADA"
        print("\n==================================")
        print("                    !!HAS GANADO!!")
        print("==================================")
        print("El numero era...... ",NumeroAleatorio)
        nombre = input("Introduce tu nombre: ")
        GuardarPartida(nombre, "Duo", "Dificil", resultado, puntos_partida, intentos)
        break
      elif numero>NumeroAleatorio:
        print("\nEl numero a adivinar es menor ↓")
      elif numero<NumeroAleatorio:
        print("\nEl numero a adivinar es mayor ↑")


      intentos= intentos -1
      print("Te quedan", intentos, "intentos")

    if resultado == "PERDIDA":
      print("HAS PERDIDO")
      nombre = input("Introduce tu nombre: ")
      GuardarPartida(nombre, "Solitario", "Dificil", resultado, puntos_partida, intentos)


  if opcion == 4:
    return

# CUARTA FUNCION: MODO DOS JUGADORES
def DosJugadores():
  global PartidasGanadaDuoFacil
  global PartidasGanadaDuoMedio
  global PartidasGanadaDuoDificil
  global PartidasJugadas
  global PartidasJugadasDuo
  global Puntuacion

  import getpass
  submenu()
  opcion = Valida(1,4)
  if opcion == 1:
    PartidasJugadas=PartidasJugadas+1
    PartidasJugadasDuo=PartidasJugadasDuo+1
    numeroAdivinado=int(getpass.getpass("Tienes que introducir un numero entre 1 y 1000"))
    while numeroAdivinado < 1 or numeroAdivinado > 1000:
      print("El numero no esta entre 1 y 1000")
      numeroAdivinado=int(getpass.getpass("Tienes que introducir un numero entre 1 y 1000"))
    intentos=20
    resultado = "PERDIDA"
    puntos_partida = 0
    while intentos>0:
        numero=int(input("Escriba un numero: "))
        if numero==numeroAdivinado:
          PartidasGanadaDuoFacil=PartidasGanadaDuoFacil+1
          Puntuacion=Puntuacion+100
          puntos_partida=100
          resultado = "GANADA"
          print("\n==================================")
          print("                    !!HAS GANADO!!")
          print("==================================")
          print("El numero era...... ",numeroAdivinado)
          nombre = input("Introduce tu nombre: ")
          GuardarPartida(nombre, "Duo", "Dificil", resultado, puntos_partida, intentos)
          break
        elif numero>numeroAdivinado:
          print("\nEl numero a adivinar es menor ↓")
        elif numero<numeroAdivinado:
          print("\nEl numero a adivinar es mayor ↑")
        intentos= intentos -1
        print("Te quedan", intentos, "intentos")

    if resultado == "PERDIDA":
      print("HAS PERDIDO")
      nombre = input("Introduce tu nombre: ")
      GuardarPartida(nombre, "Duo", "Facil", resultado, puntos_partida, intentos)


  if opcion == 2:
    PartidasJugadas=PartidasJugadas+1
    PartidasJugadasDuo=PartidasJugadasDuo+1
    numeroAdivinado=int(getpass.getpass("Tienes que introducir un numero entre 1 y 1000"))
    while numeroAdivinado < 1 or numeroAdivinado > 1000:
      print("El numero no esta entre 1 y 1000")
      numeroAdivinado=int(getpass.getpass("Tienes que introducir un numero entre 1 y 1000"))
    intentos=12
    resultado = "PERDIDA"
    puntos_partida = 0
    while intentos>0:
        numero=int(input("Escriba un numero: "))
        if numero==numeroAdivinado:
          PartidasGanadaDuoMedio=PartidasGanadaDuoMedio+1
          Puntuacion=Puntuacion+170
          puntos_partida=170
          resultado = "GANADA"
          print("\n==================================")
          print("                    !!HAS GANADO!!")
          print("==================================")
          print("El numero era...... ",numeroAdivinado)
          nombre = input("Introduce tu nombre: ")
          GuardarPartida(nombre, "Duo", "Dificil", resultado, puntos_partida, intentos)
          break
        elif numero>numeroAdivinado:
          print("\nEl numero a adivinar es menor ↓")
        elif numero<numeroAdivinado:
          print("\nEl numero a adivinar es mayor ↑")
        intentos= intentos -1
        print("Te quedan", intentos, "intentos")
    if resultado == "PERDIDA":
      print("HAS PERDIDO")
      nombre = input("Introduce tu nombre: ")
      GuardarPartida(nombre, "Duo", "Medio", resultado, puntos_partida, intentos)


  if opcion == 3:
    PartidasJugadas=PartidasJugadas+1
    PartidasJugadasDuo=PartidasJugadasDuo+1
    numeroAdivinado=int(getpass.getpass("Tienes que introducir un numero entre 1 y 1000"))
    while numeroAdivinado < 1 or numeroAdivinado > 1000:
      print("El numero no esta entre 1 y 1000")
      numeroAdivinado=int(getpass.getpass("Tienes que introducir un numero entre 1 y 1000"))
    intentos=5
    resultado = "PERDIDA"
    puntos_partida = 0
    while intentos>0:
        numero=int(input("Escriba un numero: "))
        if numero==numeroAdivinado:
          PartidasGanadaDuoDificil=PartidasGanadaDuoDificil+1
          Puntuacion=Puntuacion+400
          puntos_partida=400
          resultado = "GANADA"
          print("\n==================================")
          print("                    !!HAS GANADO!!")
          print("==================================")
          print("El numero era...... ",numeroAdivinado)
          nombre = input("Introduce tu nombre: ")
          GuardarPartida(nombre, "Duo", "Dificil", resultado, puntos_partida, intentos)
          break
        elif numero>numeroAdivinado:
          print("\nEl numero a adivinar es menor ↓")
        elif numero<numeroAdivinado:
          print("\nEl numero a adivinar es mayor ↑")
        intentos= intentos -1
        print("Te quedan", intentos, "intentos")
    if resultado == "PERDIDA":
      print("HAS PERDIDO")
      nombre = input("Introduce tu nombre: ")
      GuardarPartida(nombre, "Duo", "Dificil", resultado, puntos_partida, intentos)

  if opcion == 4:
    return

#QUINTA FUNCION: VALIDA Para no permitir insertar opciones mayores que 4 o menores que 1 en los menus
def Valida(minimo, maximo):
  opcion=int(input("Escriba una opción: "))
  while opcion<minimo or opcion>maximo:
    opcion=int(input("Escriba una opción entre 1 y 4: "))
  return opcion

#SEXTA FUNCION: ESTADISTICA Incluye el print del excel que se genera en la siguiente función
def Estadistica():

  Rojo = "\033[31m"
  Verde = "\033[32m"
  RESET = "\033[0m"

  print("\n===== DATOS GUARDADOS EN EXCEL =====")
  archivo = r"c:\EjerciciosPython\partidas.xlsx"
  if os.path.exists(archivo):
    df = pd.read_excel(archivo)
    print(df)
  else:
    print("Todavía no hay partidas guardadas en el fichero Excel")

  print("\n===== ESTADÍSTICAS =====")
  print(f"{'ESTADISTICA':30} |  VALOR")
  print("-"*50)

  print(f"Ganadas {Rojo}solitario{RESET} (fácil)      | {Verde}{PartidasGanadaSolitarioFacil}{RESET}")
  print(f"Ganadas {Rojo}solitario{RESET} (medio)      | {Verde}{PartidasGanadaSolitarioMedio}{RESET}")
  print(f"Ganadas {Rojo}solitario{RESET} (difícil)    | {Verde}{PartidasGanadaSolitarioDificil}{RESET}")

  print(f"Ganadas {Rojo}2 jugadores{RESET} (fácil)    | {Verde}{PartidasGanadaDuoFacil}{RESET}")
  print(f"Ganadas {Rojo}2 jugadores{RESET} (medio)    | {Verde}{PartidasGanadaDuoMedio}{RESET}")
  print(f"Ganadas {Rojo}2 jugadores{RESET} (difícil)  | {Verde}{PartidasGanadaDuoDificil}{RESET}")

  print(f"Partidas jugadas {Rojo}solitario{RESET}     | {Verde}{PartidasJugadasSolitario}{RESET}")
  print(f"Partidas jugadas {Rojo}duo{RESET}           | {Verde}{PartidasJugadasDuo}{RESET}")

  print(f"{'Partidas totales':30} | {Verde}{PartidasJugadas}{RESET}")
  print(f"{'Puntuación total':30} | {Verde}{Puntuacion}{RESET}")

  print("="*50)

#SEPTIMA FUNCION: GUARDAR PARTIDA
def GuardarPartida(nombre, modo, dificultad,resultado, puntos_partida, intentos_restantes):
  archivo = r"c:\EjerciciosPython\partidas.xlsx"
  if os.path.exists(archivo):
    df = pd.read_excel(archivo)
  else:
    df = pd.DataFrame(columns=["Nombre", "Modo", "Dificultad", "Resultado", "Puntos", "Intentos restantes"])

  nueva_fila = {
      "Nombre": nombre,
      "Modo": modo,
      "Dificultad": dificultad,
      "Resultado": resultado,
      "Puntos": puntos_partida,
      "Intentos restantes": intentos_restantes
  }
  df.loc[len(df)] = nueva_fila
  df.to_excel(archivo, index=False)
 


