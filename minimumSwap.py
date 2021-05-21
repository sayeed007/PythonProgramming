# Complete the minimumSwaps function below.
def minimumSwaps(A):
    if len(arr) == 1:
        return 0

    swapCount = 0
    position = 1
    n = len(arr)

    # map position to element
    posMap = {}
    for i in range(1, n+1):
        posMap[i] = arr[i-1]

    # create isVisited list
    isVisited = [False] * (n+1)

    # loop over and find cycle
    for pos in range(1, n+1):
        # if a node is already visited there is no point in computing anything -> just skip
        if (not(isVisited[pos])):
            isVisited[pos] = True
            if pos == posMap.get(pos):
                continue
            else:
                c = posMap.get(pos)
                while (not(isVisited[c])):
                    isVisited[c] = True
                    swapCount += 1
                    c = posMap.get(c)

    return swapCount

if __name__ == '__main__':

    n = 4#int(input())

    arr = [3,4,1,2]#list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)
