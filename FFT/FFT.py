import math
import numpy

def fft(arr):
    n = len(arr)
    if n == 1:
        return arr
    wn = numpy.exp((2j*math.pi)/n)
    w = 1
    odds = fft(arr[1::2])
    evens = fft(arr[::2])
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
