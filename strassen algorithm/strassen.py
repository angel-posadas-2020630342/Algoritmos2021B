import numpy
def addMatrix(matrixA=[],matrixB=[]):
    n=len(matrixA)
    matrixC=[[0 for j in range(0,n)] for i in range(0,n)]
    for y in range(0,n):
        for z in range(0,n):
            matrixC[y][z]=matrixA[y][z]+matrixB[y][z]
    return matrixC

def subMatrix(matrixA=[],matrixB=[]):
    n=len(matrixA)
    matrixC=[[0 for j in range(0,n)]for i in range(0,n)]
    for y in range(0,n):
        for z in range(0,n):
            matrixC[y][z]=matrixA[y][z]-matrixB[y][z]
    return matrixC

def multiMatrix(matrixA=[],matrixB=[]):
    n=len(matrixA[0])
    matrixC=[[0 for j in range(0,n)]for i in range(0,n)]
    for y in range(0,n):
        for z in range(0,n):
            for x in range(0,n):
                matrixC[y][z]+=matrixA[y][x]*matrixB[x][z]
    return matrixC

def strassen(matrixA=[],matrixB=[]):
    n=len(matrixA)
    newSize=n//2
    #Matriz A
    a = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    b = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    c = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    d = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    #Matriz B
    e = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    f = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    g = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    h = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    #Matriz C
    i = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    j = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    k = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
    l = [[0 for j in range(0, newSize)] for i in range(0, newSize)]

    for y in range(0,newSize):
        for z in range(0,newSize):
            #Matriz A
            a[y][z]=matrixA[y][z]#Arriba Izquierda
            b[y][z]=matrixA[y][z+newSize]#Arriba Derecha
            c[y][z]=matrixA[y+newSize][z]#Abajo Izquierda
            d[y][z]=matrixA[y+newSize][z+newSize]#Abajo Derecha
            #Matriz B
            e[y][z]=matrixB[y][z]#Arriba Izquierda
            f[y][z]=matrixB[y][z+newSize]#Arriba Derecha
            g[y][z]=matrixB[y+newSize][z]#Abajo Izquierda
            h[y][z]=matrixB[y+newSize][z+newSize]#Abajo Derecha

    S1=subMatrix(f,h)
    S2=addMatrix(a,b)
    S3=addMatrix(c,d)
    S4=subMatrix(g,e)
    S5=addMatrix(a,d)
    S6=addMatrix(e,h)
    S7=subMatrix(b,d)
    S8=addMatrix(g,h)
    S9=subMatrix(a,c)
    S10=addMatrix(e,f)

    M1=multiMatrix(a,S1)
    M2=multiMatrix(S2,h)
    M3=multiMatrix(S3,e)
    M4=multiMatrix(d,S4)
    M5=multiMatrix(S5,S6)
    M6=multiMatrix(S7,S8)
    M7=multiMatrix(S9,S10)

    i=addMatrix(subMatrix(addMatrix(M5,M4),M2),M6)
    j=addMatrix(M1,M2)
    k=addMatrix(M3,M4)
    l=subMatrix(subMatrix(addMatrix(M5,M1),M3),M7)
    
    matrixC = numpy.vstack((numpy.hstack((i, j)), numpy.hstack((k, l)))) 
    return matrixC
def main():
    matrixStra2x2u=[[0,1],[2,3]]
    matrixStra2x2t=[[4,5],[6,7]]
    matrixStra4x4u=[[0,1,2,3],[4,5,6,7],[8,9,0,1],[2,3,4,5]]
    matrixStra4x4t=[[6,7,8,9],[0,1,2,3],[4,5,6,7],[8,9,0,1]]
    matrixStra8x8u=[[0,1,2,3,4,5,6,7],[8,9,0,1,2,3,4,5],[6,7,8,9,0,1,2,3],[4,5,6,7,8,9,0,1,2,3],[4,5,6,7,8,9,0,1],[2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7],[8,9,0,1,2,3,4,5]]
    matrixStra8x8t=[[6,7,8,9,0,1,2,3],[4,5,6,7,8,9,0,1],[2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7],[8,9,0,1,2,3,4,5],[6,7,8,9,0,1,2,3],[4,5,6,7,8,9,0,1],[2,3,4,5,6,7,8,9]]
    print(str(strassen(matrixStra2x2u,matrixStra2x2t)))
    print(str(strassen(matrixStra4x4u,matrixStra4x4t)))
    print(str(strassen(matrixStra8x8u,matrixStra8x8t)))
if __name__ == "__main__":
    main()
