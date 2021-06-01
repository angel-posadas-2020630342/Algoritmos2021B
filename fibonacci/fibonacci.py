fiboarr = [0, 1]


def fibonacci(n):
    if n <= 0:
        print("Valor Incorrecto")
    if n <= len(fiboarr):
        return fiboarr[n-1]
    else:
        temp = fibonacci(n-1)+fibonacci(n-2)
        fiboarr.append(temp)
    return temp


def main():
    print("how many numbers of fibonacci's serie you want to see?")
    fibonacci(int(input()))
    print(fiboarr)


if __name__ == "__main__":
    main()
