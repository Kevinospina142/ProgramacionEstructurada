from funciones import * 

def main():
  palabra = seleccionarPalabra()
  alfabeto = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"
  jugada = ["_"]*len(palabra)

  #5 turnos
  for turno in range(5):
    print(f"\nTurno: {turno+1}")
    print("-"*20)
    #imprimir alfabeto y jugada
    imprimirActualizacion(alfabeto, jugada)
    #entrada usuario
    letra = entradaUsuario()
    #actualizar jugada y alfabeto
    jugada = actualizarJugada(palabra, letra, jugada)
    alfabeto = actualizarAlfabeto(letra, alfabeto)
    #imprimir actualizacion
    imprimirActualizacion(alfabeto, jugada)
    # Preguntar al usuario si desea adivinar o no la palabra
    check = input("Desea adivinar la palabra? (s/n): ")
    if check.lower() == "s":
      suposicion = input ("introdusca su respuesta: ").lower()
      success = verificarJugada(suposicion, palabra)
  
      if success:
        print("+"*20)
        print("ganaste webon")
        print("+"*20)
        break
      else:
        print("+"*20)
        print("la suposicion es incorrecta...")
        print("+"*20)
    if turno == 4:
      print("-"*20)
      print("se jodio")
      print(":( :( :("*20)
      
if __name__=="__main__":
  main()