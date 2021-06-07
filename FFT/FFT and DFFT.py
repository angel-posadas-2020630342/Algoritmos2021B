import math
import numpy


def dft(arr):
    n = len(arr)
    if n == 1:
        return arr
    X = numpy.zeros((n), dtype=numpy.complex128)
    for m in range(0, n):
        for k in range(0, n):
            X[m] = X[m]+arr[k]*numpy.exp((-2j*math.pi*k*m)/n)
    return X


def fft(arr):
    n = len(arr)
    if n == 1:
        return arr
    wn = numpy.exp((-2j*math.pi)/n)
    print(wn)
    w = 1
    a0=arr[1::2]; 
    a1=arr[::2];
    odds = fft(a0)
    evens = fft(a1)
    for k in range((n//2)):
        arr[k] = evens[k]+(w*odds[k])
        arr[k+(n//2)] = evens[k]-(w*odds[k])
        w = w*wn
    return arr


def main():
    arrin=[1,2,3,4]
    print(fft(arrin))


if __name__ == "__main__":
    main()
