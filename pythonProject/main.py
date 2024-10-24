'''pongo este comentario porque el primero sale mas claro y en cursiva no se porque'''

'''
Ejercicio 1. Crea una función que obtenga el máximo de una lista de números
'''


def ej1(lista) -> int:
    max = lista[0]
    for num in lista:
        if num > max:
            max = num

    return max


'''
Ejercicio 2. Crea una función que obtenga la sumatoria de una lista de números
'''


def ej2(lista) -> int:
    res = 0

    for num in lista:
        res += num

    return res


'''
Ejercicio 3. Crea una función que dada una distancia en millas calcule su
correspondiente en kms.
'''


def ej3(millas) -> float:
    return millas * 1.62137


'''
Ejercicio 4. Crea una función que determina si una letra es una vocal
'''


def ej4(caracter) -> bool:
    vocales = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    return vocales.__contains__(caracter)


'''
Ejercicio 5. Crea una función que cuenta la cantidad de números pares de una lista de
números.
'''


def ej5(lista) -> int:
    res = 0

    for num in lista:
        if num % 2 == 0:
            res += 1

    return res


'''
Ejercicio 6. Crea una función que dados un número y un intervalo (inicio, fin) cuente la
cantidad de múltiplos del número en dicho intervalo
'''


def ej6(num, intervalo) -> int:
    res = 0

    for it in range(num, intervalo):
        if intervalo % it == 0:
            res += 1

    return res


'''
Ejercicio 7. Crea una función que dada la longitud de los tres lados de un triángulo
determine si el triangulo es rectángulo 😱
'''


def ej7(a, b, c) -> bool:
    return a * a + b * b == c * c


'''
Ejercicio 8. Crea una función que calcule el máximo común divisor de dos números
naturales 😱
'''


def ej8(num1, num2) -> int:
    max = num1 if num1 > num2 else num2

    mcd = 0

    for it in range(1, max):
        if num1 % it == 0 and num2 % it == 0:
            mcd = it

    return mcd


'''
Ejercicio 9. Crea una función que dado un número n imprima los siguientes
‘mosaicos’: 😱
'''


def ej9(vueltas : int):
    for it in range(1, vueltas):
        print(str(it) * it)


'''
Ejercicio 10. Crea una función que imprima un mosaico rombo de anchura variable. 😱😱😱
'''

def ej10(vueltas):

    esPar = vueltas % 2 == 0
    for it in range(1, vueltas + 1):
        if esPar:
            if it % 2 == 0:
                print(" " * int(vueltas - it / 2), "*" * it)
        else:
            if it % 2 != 0:
                print(" " * int(vueltas - it / 2), "*" * it)

    contador = vueltas
    while(contador > 0):
        if esPar:
            if it % 2 == 0:
                print(" " * int(vueltas - it / 2), "*" * it)
        else:
            if it % 2 != 0:
                print(" " * int(vueltas - it / 2), "*" * it)
        contador -= 1
'''
    esPar = vueltas % 2 == 0
    print(vueltas)
    for it in range(1, vueltas):
        print("askiodhfadsk")
        if esPar:
            print(" " * ((vueltas - it) / 2), "*" * it)
        else:
            print("polla")
            '''

def ej10Variacion(vueltas):

    for it in range(1, vueltas + 1):
        print(" " * (vueltas - it), "*" * (it + it - 1))

    contador = vueltas - 1
    while contador > 0:
        print(" " * (vueltas - contador), "*" * (contador + contador - 1))
        contador -= 1


print(

    "Ejercicio 1: " + str(ej1([3,5,7,8,5,3,3,6,8])) + "\n",
    "Ejercicio 2: " + str(ej2([3,56,7,7,5,4,3,5,78,3])) + "\n",
    "Ejercicio 3: " + str(ej3(123)) + "\n",
    "Ejercicio 4: " + str(ej4('d')) + "\n",
    "Ejercicio 5: " + str(ej5([3,4,6,67,3,2,23,35,67,5,3,3,5])) + "\n",
    "Ejercicio 6: " + str(ej6(4,30)) + "\n",
    "Ejercicio 7: " + str(ej7(3,3,3)) + "\n",
    "Ejercicio 8: " + str(ej8(23,65)) + "\n",
    "Ejercicio 9: " + "\n"
)
ej9(5)
print("Ejercicio 10: ")
ej10(5)