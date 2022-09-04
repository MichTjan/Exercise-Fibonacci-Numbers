#My solution
def fib(number):
    for i in range(number):
        fibonacci = int(((1.618034)**i-(1-1.618034)**i)/5**(1/2))
        yield fibonacci

for item in fib(20):
    print(item)

#Andrei's solution
def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        yield a 
        temp = a 
        a = b
        b = temp + b

for x in fibo(10):
    print(x)
        