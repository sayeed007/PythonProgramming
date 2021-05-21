from typing import OrderedDict


N = int(input())

ord_dic = OrderedDict()

for i in range(N):
    item = input().split()
    item_name = " ".join(item[:-1])
    net_price = int( item[-1] )
    if ord_dic.get(item_name):
        ord_dic[item_name] += net_price
    else:
        ord_dic[item_name] = net_price

for i in ord_dic.keys():
    print (i, ord_dic[i])
