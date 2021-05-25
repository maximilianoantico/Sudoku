from mapas import MAPAS
import sudoku
import random
import copy


def imprimir_sudoku(Sudoku):
    VACIO = 0
    orden_fila = 1
    valor_columnas = ("   1"+"  2"+"  3"+"  4"+"  5"+"  6"+"  7"+"  8"+"  9")
    print("""
╔╦╗╦ ╦╦╔═╗  ╦╔═╗  ╔═╗╦ ╦╔╦╗╔═╗╦╔═╦ ╦  
 ║ ╠═╣║╚═╗  ║╚═╗  ╚═╗║ ║ ║║║ ║╠╩╗║ ║  
 ╩ ╩ ╩╩╚═╝  ╩╚═╝  ╚═╝╚═╝═╩╝╚═╝╩ ╩╚═╝ """)
    print (valor_columnas)
    for fila in Sudoku:
        filas = ""
        
        for valor in fila:
            if valor == VACIO:
                filas += "|.|"
            if valor != VACIO:
                filas += ("|" + str(valor) + "|")
        print (orden_fila, filas, orden_fila)
        orden_fila +=1
    print (valor_columnas)
    
def main():
    VACIO = 0
    Sudoku = sudoku.crear_juego(juego = random.choice(MAPAS))
    imprimir_sudoku(Sudoku)
    while True:
        accion = int(input("1-Agregar Valor\n2-Borrar Valor\n3-Salir\n\nIngrese acción: "))
        
        if accion == 1:
             fila = (int(input ("Ingrese fila (Arriba a abajo) del 1 al 9 donde quiere poner su valor: ")))-1
             columna = (int(input("Ingrese columna (izquierda a derecha) del 1 al 9 donde quiere poner su valor: ")))-1
             valor = int(input ("Ingrese un valor del 1 al 9: "))
             if True == (0 <=columna<= 8 and 1 <= valor <= 9 and  0 <=fila<= 8):
                 if (True == sudoku.es_movimiento_valido(Sudoku, fila, columna, valor)) and (True == (sudoku.obtener_valor(Sudoku, fila, columna) == VACIO)):
                     imprimir_sudoku(sudoku.insertar_valor(Sudoku, fila, columna, valor))
                     Sudoku = copy.deepcopy(sudoku.insertar_valor(Sudoku, fila, columna, valor))
                 else:
                     print("""
                           Movimiento no es valido hay algun valor repetido en alguna parte
                           
                           Tambien pudo ser que se ingreso cualquier cosa jeje""")
                     imprimir_sudoku(Sudoku)  
             else:
                 print("""
                           Movimiento no es valido hay algun valor repetido en alguna parte
                           
                           Tambien pudo ser que se ingreso cualquier cosa jeje""")
                 imprimir_sudoku(Sudoku)  
        else:
            pass
        
        if accion == 2:
             fila = (int(input ("Ingrese fila (Arriba a abajo) del 1 al 9 donde borrar su valor: ")))-1
             columna = (int(input("Ingrese columna (izquierda a derecha) del 1 al 9 donde quiere borrar su valor: ")))-1
             valor = int(input ("Ingrese el valor del 1 al 9 que quiere borrar: "))
             if True == (0 <=columna<= 8 and 1 <= valor <= 9 and  0 <=fila<= 8):
                 imprimir_sudoku(sudoku.borrar_valor(Sudoku, fila, columna))
                 Sudoku = copy.deepcopy(sudoku.borrar_valor(Sudoku, fila, columna))
             else:
                 print("""
                       Movimiento no es valido hay algun valor repetido en alguna parte
                       
                       Tambien pudo ser que se ingreso cualquier cosa jeje""")
                 imprimir_sudoku(Sudoku)
                 
        else:
            pass
        
        if accion == 3:
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
             repetir = int (input("Queres seguir jugando?\n1-Pasame otro que lo completo en un PIM PAM PUM \n2-No, necesito un descansito\nOpcion Seleccionada: "))
             if repetir == 1:
                 return main()
             else:
                 break
        


main()
    
    
   
