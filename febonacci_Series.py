def f1():
    a,b=0,1
    while True :
        yield a 
        a,b=b,a+b

it = f1()
fib_list = []
while True:
    ans = input("generate y/n")
    if ans == 'y' :
        fib_list.append(next(it))
    else :
        break

print(fib_list)