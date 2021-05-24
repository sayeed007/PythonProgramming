def whatFlavors(cost, money):
    cost_dict = {}
    for i,icost in enumerate(cost):
        if money-icost in cost_dict:
            print(str(cost_dict[money-icost]+1) + ' ' + str(i+1))
            return 
        else:
            cost_dict[icost] = i

if __name__ == '__main__':
    #t = int(input())
    money = 4   #int(input())

    n = 5   #int(input())

    cost =  [2, 2, 5, 3, 2]    #list(map(int, input().rstrip().split()))

    whatFlavors(cost, money,n)