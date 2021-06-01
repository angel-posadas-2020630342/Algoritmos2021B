def gloutonAlgorithm(n):
    coins=[10,5,2,1];
    k=0
    while(n>0):
        if(coins[k]>n):
            k+=1
        else:
            print(str(coins[k]))
            n-=coins[k]

def main():
    print("enter amoung")
    gloutonAlgorithm(int(input()))

if __name__ == "__main__":
    main()
