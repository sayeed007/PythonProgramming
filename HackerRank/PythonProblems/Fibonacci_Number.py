import timeit
"""
    timeit.timeit(stmt, setup,timer, number)
    print(timeit.repeat(stmt=testcode, setup=import_module, repeat=5))
"""
def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = fib(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst


def fib_dp(num):
    arr = [0,1]

    if num== 1:
        print('0')

    elif num == 2:
        print('[0,','1]')
        
    else:
        while(len(arr)<num):
            arr.append(0)
        if(num==0 or num==1):
            return 1
        else:
            arr[0]=0
            arr[1]=1
            for i in range(2,num):
                arr[i]=arr[i-1]+arr[i-2]
            print(arr)    
#RECURSIVE
start = timeit.default_timer()
x = fib(10)
print(x)
stop = timeit.default_timer()
print('Time: ', stop - start)  
x =  stop - start
print("\n\nDynamic Method")
#DYNAMIC
start = timeit.default_timer()
fib_dp(10)
stop = timeit.default_timer()
print('\n\nTime: ', stop - start)  
y =  stop - start

if (x<y):
    print("\nRecursive is better")
else:
    print("\nDynamic is better")