
def getTotalX(a, b):
    lowerL = max(a)
    upperL = min(b)
    count = 0

    for i in range(lowerL,upperL+1):
        temp = 0
        for m in a:
            if i % m != 0:
                temp = 1
                break
            for j in b:
                if j % i != 0:
                    temp = 1
                    break
        if(temp == 0):
            count += 1          
            
    print(count)
    # Write your code here

if __name__ == '__main__':

    n = 2

    m = 3

    arr = [2, 4]

    brr = [16, 32, 96]

    total = getTotalX(arr, brr)