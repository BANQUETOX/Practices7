# Haga una rutina que reciba un arreglo de caracteres y retorne true si el arreglo es palíndrome o false
# si no. Un arreglo es palíndrome si se puede leer igual de izquierda a derecha que de derecha a
# izquierda. Ejemplo: “Anita lava la tina”, “Odio la luz azul al oído”, etcétera. Suponga que el arreglo no
# guarda los espacios en blanco entre palabras. Pruebe esta función en un programa que lea el arreglo y
# diga si es palíndrome o no.
def is_palidrome(word_list:list)->bool:
    reversed_list = []
    for word in reversed(word_list):
        reversed_list.append(word)
    for index,_ in enumerate(word_list):
        if word_list[index] == reversed_list[index]:
            continue
        else:
            return False
            break
    return True

print(is_palidrome(["a","n","i","t","a","l","a","v","a","l","a","t","i","n","a"]))