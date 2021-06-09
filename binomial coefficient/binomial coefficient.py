def binomialCoefficient(a,b,memo=[]):
    if memo[b][a]!=0:
        return memo[b][a]
    if a==0 or a==b:
        memo[b][a]=1
        return memo[b][a]
    memo[b][a]=binomialCoefficient(a-1,b-1,memo)+binomialCoefficient(a,b-1,memo)
    return memo[b][a]


def main():
    j=5
    n=2
    memoization=[[0 for j in range(n+1)] for x in range(j+1)]
    print("El coeficiente numero: "+str(n)+" del renglon "+str(j)+" es "+str(binomialCoefficient(n,j,memoization)))

if __name__ == "__main__":
    main()
