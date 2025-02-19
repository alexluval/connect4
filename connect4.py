# Alejandro Luna
# Class Competition 2019: Bachelor's in Mathematics, University of Alicante
# Everything was written in Spanish

from sys import stderr
from time import sleep

def rellena_matriz_int(n, m, valor):
    M = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(valor)
        M.append(row)
    return M


def imprime_matriz(tablero):
    print("\n".join([" ".join(['🔵' if c == AZUL else '🔴' if c == ROJA else '⚪' for c in fila]) for fila in tablero]))
    print(" 1  2  3  4  5  6  7 ")


def ganador(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] != VACIO:
                for ficha in [ROJA, AZUL]:
                    if cuenta_fichas(tablero, i, j, 1, -1, ficha) == 4:
                        return ficha
                    if cuenta_fichas(tablero, i, j, 1, 0, ficha) == 4:
                        return ficha
                    if cuenta_fichas(tablero, i, j, 1, 1, ficha) == 4:
                        return ficha
                    if cuenta_fichas(tablero, i, j, 0, 1, ficha) == 4:
                        return ficha
    return None


def cuenta_fichas(tablero, y, x, incy, incx, ficha):
    contar = 0
    while y >= 0 and y < len(tablero) and x >= 0 and x < len(tablero[0]) and tablero[y][x] == ficha:
        contar += 1
        x += incx
        y += incy
    return contar


def tablero_lleno(tablero):
    return 0 not in tablero[0]


def coloca_ficha(tablero, col, ficha):
    if tablero[0][col] != VACIO:
        print('Movimiento no permitido: Columna llena')
    else:
        for i in range(1, len(tablero)):
            if tablero[i][col] != VACIO:
                tablero[i - 1][col] = ficha
                return tablero
        tablero[5][col] = ficha
        return tablero


def imprime_cabecera():
    for i in range(1, 8):
        print(i, end=' ')
    print()


def imprime_tablero(tablero):
    imprime_cabecera()
    imprime_matriz(tablero)


def error(msg):
    print(msg, file=stderr)
    sleep(1)


def columna_maspuntuada(puntoscolumnas):
    columna = 1
    maxima = max(puntoscolumnas)
    for i in puntoscolumnas:
        if i != maxima:
            columna += 1
        else:
            return columna


def proximidad(tablero):
    lista_columnas = []
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if i >= 0 and i < len(tablero) and j >= 0 and j < len(tablero[0]) and tablero[i][j] == ROJA:
                if j + 1 < len(tablero[0]):
                    if tablero[i][j + 1] == 0:
                        lista_columnas.append(j+1)
                if j - 1 >= 0:
                    if tablero[i][j - 1] == 0:
                        lista_columnas.append(j-1)
    return lista_columnas


def tapar_tres_seguidas_vertical(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, 0, ROJA) == 3 and i - 1 >= 0:
                if tablero[i-1][j] == 0:
                    columna_prioridad = j
    return columna_prioridad


def tapar_dos_seguidas_horizontal_ras_de_suelo1(tablero):
    columna_prioridad1 = None
    for j in range(len(tablero[5])):
        if cuenta_fichas(tablero, 5, j, 0, 1, ROJA) == 2 and j - 1 >= 0:
            if tablero[5][j - 1] == 0:
                columna_prioridad1 = j - 1
    return columna_prioridad1


def tapar_dos_seguidas_horizontal_ras_de_suelo2(tablero):
    columna_prioridad1 = None
    for j in range(len(tablero[5])):
        if cuenta_fichas(tablero, 5, j, 0, 1, ROJA) == 2 and j + 2 < len(tablero[5]):
            if tablero[5][j + 2] == 0:
                columna_prioridad1 = j + 2
    return columna_prioridad1


def tapar_dos_obliquas1(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, 1, ROJA) == 2 and j - 1 >= 0 and i - 1 >= 0:
                if tablero[i - 1][j - 1] == 0 and tablero[i][j - 1] != 0:
                    columna_prioridad = j - 1
    return columna_prioridad


def tapar_dos_obliquas2(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, 1, ROJA) == 2 and j + 2 < len(tablero[i]) and i + 3 < len(tablero):
                if tablero[i + 2][j + 2] == 0 and tablero[i + 3][j + 2] != 0:
                    columna_prioridad = j + 2
    return columna_prioridad


def tapar_dos_obliquas3(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, -1, ROJA) == 2 and j + 1 < len(tablero[i]) and i - 1 >= 0:
                if tablero[i - 1][j + 1] == 0 and tablero[i][j + 1] != 0:
                    columna_prioridad = j + 1
    return columna_prioridad


def tapar_dos_obliquas4(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, -1, ROJA) == 2 and j - 2 >= 0 and i + 3 < len(tablero):
                if tablero[i + 2][j - 2] == 0 and tablero[i + 3][j - 2] != 0:
                    columna_prioridad = j - 2
    return columna_prioridad


def colocar_dos_seguidas_vertical(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, 0, AZUL) == 2 and i - 1 >= 0:
                if tablero[i-1][j] == 0:
                    columna_prioridad = j
    return columna_prioridad


def colocar_tres_seguidas_vertical(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, 0, AZUL) == 3 and i - 1 >= 0:
                if tablero[i-1][j] == 0:
                    columna_prioridad = j
    return columna_prioridad


def colocar_tres_seguidas_horizontal_ras_de_suelo1(tablero):
    columna_prioridad1 = None
    for j in range(len(tablero[5])):
        if cuenta_fichas(tablero, 5, j, 0, 1, AZUL) == 3 and j - 1 >= 0:
            if tablero[5][j - 1] == 0:
                columna_prioridad1 = j - 1
    return columna_prioridad1


def colocar_tres_seguidas_horizontal_ras_de_suelo2(tablero):
    columna_prioridad1 = None
    for j in range(len(tablero[5])):
        if cuenta_fichas(tablero, 5, j, 0, 1, AZUL) == 3 and j + 3 < len(tablero[5]):
            if tablero[5][j + 3] == 0:
                columna_prioridad1 = j + 3
    return columna_prioridad1


def colocar_tres_seguidas_horizontal1(tablero):
    columna_prioridad1 = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 0, 1, AZUL) == 3 and j - 1 >= 0 and i + 1 < len(tablero):
                if tablero[i][j - 1] == 0 and tablero[i + 1][j - 1] != 0:
                    columna_prioridad1 = j - 1
    return columna_prioridad1


def colocar_tres_seguidas_horizontal2(tablero):
    columna_prioridad1 = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 0, 1, AZUL) == 3 and j + 3 < len(tablero[i]) and i + 1 < len(tablero):
                if tablero[i][j + 3] == 0 and tablero[i + 1][j + 3] != 0:
                    columna_prioridad1 = j + 3
    return columna_prioridad1


def colocar_tres_obliquas1(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, 1, AZUL) == 3 and j - 1 >= 0 and i - 1 >= 0:
                if tablero[i - 1][j - 1] == 0 and tablero[i][j - 1] != 0:
                    columna_prioridad = j - 1
    return columna_prioridad


def colocar_tres_obliquas2(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, 1, AZUL) == 3 and j + 3 < len(tablero[i]) and i + 4 < len(tablero):
                if tablero[i + 3][j + 3] == 0 and tablero[i + 4][j + 2] != 0:
                    columna_prioridad = j + 3
    return columna_prioridad


def colocar_tres_obliquas3(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, -1, AZUL) == 3 and j + 1 < len(tablero[i]) and i - 1 >= 0:
                if tablero[i - 1][j + 1] == 0 and tablero[i][j + 1] != 0:
                    columna_prioridad = j + 1
    return columna_prioridad


def colocar_tres_obliquas4(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, -1, AZUL) == 3 and j - 3 >= 0 and i + 4 < len(tablero):
                if tablero[i + 3][j - 3] == 0 and tablero[i + 4][j - 3] != 0:
                    columna_prioridad = j - 3
    return columna_prioridad


def colocar_dos_obliquas1(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, 1, AZUL) == 2 and j - 1 >= 0 and i - 1 >= 0:
                if tablero[i - 1][j - 1] == 0 and tablero[i][j - 1] != 0:
                    columna_prioridad = j - 1
    return columna_prioridad


def colocar_dos_obliquas2(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, 1, AZUL) == 2 and j + 2 < len(tablero[i]) and i + 3 < len(tablero):
                if tablero[i + 2][j + 2] == 0 and tablero[i + 3][j + 2] != 0:
                    columna_prioridad = j + 2
    return columna_prioridad


def colocar_dos_obliquas3(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, -1, AZUL) == 2 and j + 1 < len(tablero[i]) and i - 1 >= 0:
                if tablero[i - 1][j + 1] == 0 and tablero[i][j + 1] != 0:
                    columna_prioridad = j + 1
    return columna_prioridad


def colocar_dos_obliquas4(tablero):
    columna_prioridad = None
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if cuenta_fichas(tablero, i, j, 1, -1, AZUL) == 2 and j - 2 >= 0 and i + 3 < len(tablero):
                if tablero[i + 2][j - 2] == 0 and tablero[i + 3][j - 2] != 0:
                    columna_prioridad = j - 2
    return columna_prioridad


def mega_estrategia(tablero):
    puntos_columnas = [0, 2, 4, 5, 4, 2, 0]

    lista_columnas = proximidad(tablero) #se puntua la proximidad a la fichas del oponente
    for i in lista_columnas: puntos_columnas[i] += 4

    columna_prioridad1 = tapar_tres_seguidas_vertical(tablero) #priorizamos el tapar fichas al oponente
    if columna_prioridad1 != None:
        puntos_columnas[columna_prioridad1] = puntos_columnas[columna_prioridad1] + 999

    columna_prioridad2 = tapar_dos_seguidas_horizontal_ras_de_suelo1(tablero)
    if columna_prioridad2 != None:
        puntos_columnas[columna_prioridad2] = puntos_columnas[columna_prioridad2] + 449

    columna_prioridad3 = tapar_dos_seguidas_horizontal_ras_de_suelo2(tablero)
    if columna_prioridad3 != None:
        puntos_columnas[columna_prioridad3] = puntos_columnas[columna_prioridad3] + 449

    tapar1 = tapar_dos_obliquas1(tablero)
    if tapar1 != None:
        puntos_columnas[tapar1] = puntos_columnas[tapar1] + 200

    tapar2 = tapar_dos_obliquas2(tablero)
    if tapar2 != None:
        puntos_columnas[tapar2] = puntos_columnas[tapar2] + 200

    tapar3 = tapar_dos_obliquas3(tablero)
    if tapar3 != None:
        puntos_columnas[tapar3] = puntos_columnas[tapar3] + 200

    tapar4 = tapar_dos_obliquas4(tablero)
    if tapar4 != None:
        puntos_columnas[tapar4] = puntos_columnas[tapar4] + 200


    columna_colocar_vertical1 = colocar_dos_seguidas_vertical(tablero) #puntuamos que nuestras fichas se situen bien
    if columna_colocar_vertical1 != None:
        puntos_columnas[columna_colocar_vertical1] = puntos_columnas[columna_colocar_vertical1] + 201

    columna_colocar_vertical2 = colocar_tres_seguidas_vertical(tablero)
    if columna_colocar_vertical2 != None:
        puntos_columnas[columna_colocar_vertical2] = puntos_columnas[columna_colocar_vertical2] + 9999

    colocar1 = colocar_tres_seguidas_horizontal_ras_de_suelo1(tablero)
    if colocar1  != None:
        puntos_columnas[colocar1] = puntos_columnas[colocar1] + 9999

    colocar2 = colocar_tres_seguidas_horizontal_ras_de_suelo2(tablero)
    if colocar2 != None:
        puntos_columnas[colocar2] = puntos_columnas[colocar2] + 9999

    colocar3 = colocar_tres_seguidas_horizontal1(tablero)
    if colocar3 != None:
        puntos_columnas[colocar3] = puntos_columnas[colocar3] + 9999

    colocar4 = colocar_tres_seguidas_horizontal2(tablero)
    if colocar4 != None:
        puntos_columnas[colocar4] = puntos_columnas[colocar4] + 9999

    colocar5 = colocar_tres_obliquas1(tablero)
    if colocar5 != None:
        puntos_columnas[colocar5] = puntos_columnas[colocar5] + 9999

    colocar6 = colocar_tres_obliquas2(tablero)
    if colocar6 != None:
        puntos_columnas[colocar6] = puntos_columnas[colocar6] + 9999

    colocar6 = colocar_tres_obliquas3(tablero)
    if colocar6 != None:
        puntos_columnas[colocar6] = puntos_columnas[colocar6] + 9999

    colocar7 = colocar_tres_obliquas4(tablero)
    if colocar7 != None:
        puntos_columnas[colocar7] = puntos_columnas[colocar7] + 9999

    colocarr = colocar_dos_obliquas1(tablero)
    if colocarr != None:
        puntos_columnas[colocarr] = puntos_columnas[colocarr] + 200

    colocarr2 = colocar_dos_obliquas2(tablero)
    if colocarr2 != None:
        puntos_columnas[colocarr2] = puntos_columnas[colocarr2] + 200

    colocarr3 = colocar_dos_obliquas3(tablero)
    if colocarr3 != None:
        puntos_columnas[colocarr3] = puntos_columnas[colocarr3] + 200

    colocarr4 = colocar_dos_obliquas4(tablero)
    if colocarr4 != None:
        puntos_columnas[colocarr4] = puntos_columnas[colocarr4] + 200

    return columna_maspuntuada(puntos_columnas)


VACIO = 0
ROJA = 1
AZUL = 2

ficha = AZUL #aquí se elige quien empieza
tablero = rellena_matriz_int(6, 7, 0)

while ganador(tablero) == None and not tablero_lleno(tablero):
    imprime_tablero(tablero)
    print()

    if ficha == AZUL:
        col = mega_estrategia(tablero)

    elif ficha == ROJA:
        col = int(input('columna'))
        #col = random_matrix(1, 1, 0, 7)[0][0]


    coloca_ficha(tablero, col - 1, ficha)
    ficha = ROJA if ficha == AZUL else AZUL


imprime_tablero(tablero)
if ganador(tablero) == ROJA:
    print()
    print('Gana la ficha ROJA')
else:
    print()
    print('Gana la ficha AZUL')
    
    
    