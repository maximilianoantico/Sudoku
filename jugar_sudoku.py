from mapas import MAPAS
import sudoku
import random
import copy
VACIO = 0

def imprimir_sudoku(Sudoku):
    orden_fila = 1
    valor_columnas = ("  "+"   1"+"  2"+"  3"+"  4"+"  5"+"  6"+"  7"+"  8"+"  9")
    borde_superior = ("  "+"   _"+"  _"+"  _"+"  _"+"  _"+"  _"+"  _"+"  _"+"  _")
    borde_inferior = ("  "+"   -"+"  -"+"  -"+"  -"+"  -"+"  -"+"  -"+"  -"+"  -")
    print("""
╔╦╗╦ ╦╦╔═╗  ╦╔═╗  ╔═╗╦ ╦╔╦╗╔═╗╦╔═╦ ╦  
 ║ ╠═╣║╚═╗  ║╚═╗  ╚═╗║ ║ ║║║ ║╠╩╗║ ║  
 ╩ ╩ ╩╩╚═╝  ╩╚═╝  ╚═╝╚═╝═╩╝╚═╝╩ ╩╚═╝ 
 """)
    print (valor_columnas)
    print (borde_superior)
    for fila in Sudoku:
        filas = ""
        
        for valor in fila:
            if valor == VACIO:
                filas += "|.|"
            if valor != VACIO:
                filas += ("|" + str(valor) + "|")
        print (orden_fila, "-", filas, "-", orden_fila)
        orden_fila +=1
    print (borde_inferior)
    print (valor_columnas)
    
def main():
    Sudoku = sudoku.crear_juego(juego = random.choice(MAPAS))
    imprimir_sudoku(Sudoku)
    while True:
        accion = input("\n1-Agregar Valor\n2-Borrar Valor\n3-Salir\n\nIngrese acción: ")
        if (not accion in "123") or accion == "" :
            print("""
                  Eliga una de las 3 opciones
                  """)
            imprimir_sudoku(Sudoku)
        else:
            accion = int(accion)
        if accion == 1:
            fila = input("Ingrese fila (Arriba a abajo) del 1 al 9 donde quiere poner su valor: ")
            if (not fila in "123456789") or fila == "":
                print("""
                      El valor ingresado no es valido
                      """)
                imprimir_sudoku(Sudoku)
                continue
            else:
                fila = (int(fila)) - 1 
            columna = input ("Ingrese columna (izquierda a derecha) del 1 al 9 donde quiere poner su valor: ")
            if (not columna in "123456789") or columna == "":
                print("""
                      El valor ingresado no es valido
                      """)
                imprimir_sudoku(Sudoku)
                continue
            else:
                columna = (int(columna)) - 1
            valor = input ("Ingrese un valor del 1 al 9: ")
            if (not valor in "123456789") or valor == "":
                print("""
                      El valor ingresado no es valido
                      """)
                imprimir_sudoku(Sudoku)
                continue
            else: 
                valor = int(valor)
            if (0 <=columna<= 8) and (1 <= valor <= 9) and  (0 <=fila<= 8):
                 if (sudoku.es_movimiento_valido(Sudoku, fila, columna, valor) and (sudoku.obtener_valor(Sudoku, fila, columna) == VACIO)):
                     imprimir_sudoku(sudoku.insertar_valor(Sudoku, fila, columna, valor))
                     Sudoku = copy.deepcopy(sudoku.insertar_valor(Sudoku, fila, columna, valor))
                 else:
                     print("""
                           Movimiento no es valido hay algun valor repetido en alguna parte
                           
                           """)
                     imprimir_sudoku(Sudoku)  
            else:
                 print("""
                           Movimiento no es valido hay algun valor repetido en alguna parte
                           
                           """)
                 imprimir_sudoku(Sudoku)  

        
        elif accion == 2:
            fila = input ("Ingrese fila (Arriba a abajo) del 1 al 9 donde quiere poner su valor: ")
            if (not fila in "123456789") or fila == "":
                print("""
                      El valor ingresado no es valido
                      """)
                imprimir_sudoku(Sudoku)
                continue
            else:
                fila = (int(fila)) - 1 
            columna = input ("Ingrese columna (izquierda a derecha) del 1 al 9 donde quiere poner su valor: ")
            if (not columna in "123456789") or columna == "":
                print("""
                      El valor ingresado no es valido
                      """)
                imprimir_sudoku(Sudoku)
                continue
            else:
                columna = (int(columna)) - 1
            valor = input ("Ingrese un valor del 1 al 9: ")
            if (not valor in "123456789") or valor == "":
                print("""
                      El valor ingresado no es valido
                      """)
                imprimir_sudoku(Sudoku)
                continue
            else: 
                valor = int(valor)
            if 0 <=columna<= 8 and 1 <= valor <= 9 and  0 <=fila<= 8:
                 imprimir_sudoku(sudoku.borrar_valor(Sudoku, fila, columna))
                 Sudoku = copy.deepcopy(sudoku.borrar_valor(Sudoku, fila, columna))
            else:
                 print("""
                       Movimiento no es valido hay algun valor repetido en alguna parte
                       """)
                 imprimir_sudoku(Sudoku)
        
        elif accion == 3:
            print("Te has retirado! Sera hasta la proxima")
            return False
        
        if True == sudoku.esta_terminado(Sudoku):
            print("""
      ______     _  _        _  _                _                             _____                            _         _  _  _ 
     |  ____|   | |(_)      (_)| |              (_)                           / ____|                          | |       | || || |
     | |__  ___ | | _   ___  _ | |_  __ _   ___  _   ___   _ __    ___  ___  | |  __   __ _  _ __    __ _  ___ | |_  ___ | || || |
     |  __|/ _ \| || | / __|| || __|/ _` | / __|| | / _ \ | '_ \  / _ \/ __| | | |_ | / _` || '_ \  / _` |/ __|| __|/ _ \| || || |
     | |  |  __/| || || (__ | || |_| (_| || (__ | || (_) || | | ||  __/\__ \ | |__| || (_| || | | || (_| |\__ \| |_|  __/|_||_||_|
     |_|   \___||_||_| \___||_| \__|\__,_| \___||_| \___/ |_| |_| \___||___/  \_____| \__,_||_| |_| \__,_||___/ \__|\___|(_)(_)(_)
                                                                                                                                  
                                                                                                                                  """)
            repetir = input("Queres seguir jugando?\n1-Pasame otro que lo completo en un PIM PAM PUM \n2-No, necesito un descansito\nOpcion Seleccionada: ")
             
            if (not repetir in "12") and repetir == "":
                print("""El valor ingresado no es valido """)
                continue
            elif int(repetir) == 1:
                Sudoku = sudoku.crear_juego(juego = random.choice(MAPAS))
                continue
            elif int(repetir) == 2:
                 break
        


main()
