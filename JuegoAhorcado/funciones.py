import random
alfabeto = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"

# Funcion para escoger una palabra random
def seleccionarPalabra():
  lineas = open ("frutas_verduras.txt").readlines()
  palabra = random.choice(lineas).rstrip()
  return palabra

#Funcion entrada del teclado
def entradaUsuario():
  letra = input ("Introduzca una letra: ")
  return letra.lower()

#Funcion actualizar jugada
def actualizarJugada(palabra, letra, jugada):
  n_letras = len(palabra)

  for i in range(0, n_letras):
    if palabra[i] == letra:
      jugada [i] = letra
  return jugada

#actualizar el alfabeto
def actualizarAlfabeto(letra, alfabeto):
  alfabeto = alfabeto.replace(letra, " ")
  return alfabeto

#imprimir resultado de la jugada en pantalla
def imprimirActualizacion(alfabeto, jugada):
  print(f"Jugada: {jugada}")
  print(f"Letras disponibles: {alfabeto}")

#verficar jugada
def verificarJugada(suposicion, palabra):
  success = False
  if suposicion == palabra:
    success = True
  return success
  success = verificarJugada("tomate", palabra)
  print(success)