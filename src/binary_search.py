from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    """
    Realiza busca binária em um array ordenado.

    Deve retornar o índice do elemento ou -1 caso não encontrado.
    """
    right = len(array) - 1
    left = 0

    while left <= right:
        med = (left + right) // 2
        med_val = array[med]

        if med_val == target:
            return med
        elif med_val < target:
            left = med + 1
        else:
            right = med - 1
    return -1
