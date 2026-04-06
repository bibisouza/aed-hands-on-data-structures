from src.my_array import MyArray


def linear_search(array: MyArray, target: int) -> int:
    """
    Realiza uma busca em um MyArray.

    Deve retornar o índice da primeira ocorrência do valor,
    ou -1 caso o valor não esteja presente.
    """
    for index in range(len(array)):
        if array[index] == target:
            return index
    return -1
