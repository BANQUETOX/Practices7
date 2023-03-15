# Haga un programa que lea un arreglo de números reales e imprima: cuántos números del arreglo son
# positivos, cuántos son negativos y cuántos son iguales a cero. Para resolver esto usted debe hacer:
# una rutina llenarArreglo que lee un arreglo de números reales, una rutina contarPositivos que
# recibe un arreglo de números reales y retorna cuántos números del arreglo son mayores a cero, una
# rutina contarNegativos que recibe un arreglo de números reales y retorna cuántos números del
# arreglo son menores que cero, una rutina contarCeros que recibe un arreglo de números reales y
# retorna cuántos números del arreglo son iguales a cero.
def llenarArreglo():
    numbers_list = []
    for number in range(0,int(input("Cuantos numeros desea agregar? "))):
        numbers_list.append(int(input(f"Ingrese su numero #{number + 1} ")))
    return numbers_list
def contarPositivos(numbers_list:list):
    total_positives = 0
    for number in numbers_list:
        if number > 0:
            total_positives += 1
    return total_positives

def contarNegativos(numbers_list:list):
    total_negatives = 0
    for number in numbers_list:
        if number < 0:
            total_negatives += 1
    return total_negatives

def contarCeros(numbers_list:list):
    total_ceros = 0
    for number in numbers_list:
        if number == 0:
            total_ceros += 1
    return total_ceros

my_list = llenarArreglo()
print(contarPositivos(my_list))
print(contarNegativos(my_list))
print(contarCeros(my_list))