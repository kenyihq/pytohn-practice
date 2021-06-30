def list_comprehension():
    # Crear una lista de números pares del 2 al 100

    numbers = [i for i in range(1, 101) if i%2 == 0]
    print(numbers)

def fibonacci(n):
    # Crear una lista con los números de Fibonacci hasta el 100

    a, b = 0, 1
    fib = []
    while a < n:
        fib.append(a)
        a, b = b, a+b
    print(fib)

if __name__ == '__main__':
    fibonacci(100)