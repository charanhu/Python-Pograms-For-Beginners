 

def factorial(n):
    try:
        if n==1 or n==0:
            return 1
        else:
            return n*factorial(n-1)
    except:
        return
    
              

n=int(input("n="))             
print(factorial(n))