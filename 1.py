# Haga una función que reciba dos arreglos de enteros y que retorne true si los arreglos son iguales o
# false si no. Pruebe la función en un programa.

def same_list(list_one:list, list_two:list)-> bool:
    for number in list_one:
        if number == list_two[list_one.index(number)]:
            continue
        else:
            return False
            break
    return True

print(same_list([1,2,3],[1,2,4]))