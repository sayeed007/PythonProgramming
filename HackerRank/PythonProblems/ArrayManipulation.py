# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = []
    for i in range(n):
        arr.append(0)
    
    for j in range(3):
        a = queries[j][0]
        b = queries[j][1]
        k = queries[j][2]
        
        for p in range(a-1,b):
            arr[p] = arr[p] + k
        print(arr)
        
    return (max(arr))

if __name__ == '__main__':
    n = 5

    m = 3

    queries = [ [1, 2, 100], [2, 5, 100], [3, 4, 100] ]
    
    result = arrayManipulation(n, queries)

    print (result)