def media(arr):
    counter = total_sum = 0
    for value in arr:
        counter += 1
        total_sum += value
    return total_sum / counter


if __name__ == '__main__':
    arr = [float(x) for x in input(
        "Ingrese los datos separados por coma (,): ").split(',')]
    m = media(arr)
    print(f"La media del arreglo de números {arr} es {m}")
