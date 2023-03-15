# Haga una rutina que invierta un arreglo de enteros, sin usar un arreglo adicional. Pruébela en un
# programa que lea el arreglo original, invierta el arreglo e imprima el arreglo invertido.

def invert_list(numbers_list:list)->bool:
    print(numbers_list)
    print(numbers_list[::-1])
    
invert_list([1,2,3,4,5])