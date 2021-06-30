def list_comprehension():
    # Crear una lista de números pares del 2 al 100

    numbers = [i for i in range(1, 101) if i%2 == 0]
    print(numbers)

if __name__ == '__main__':
    list_comprehension()