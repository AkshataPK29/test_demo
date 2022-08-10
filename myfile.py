def fact(n):
    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    fact=1
    while (n>1):
        fact*=n
        n-=1
    return fact

def armstrong(n):
    s=n
    b=len(str(n))
    sum1=0
    while(n!=0):
        r = n%10
        sum1=sum1+(r**b)
        n=n//10
    if(sum1==s):
        print("yes, number is armstrong")
    else:
        print("number is not armstrong")        


if __name__=="__main__":
    n=int(input("Enter number: "))
    #factorial= fact(n)
    #print("factorial of n is :", factorial)
    arms= armstrong(n)
