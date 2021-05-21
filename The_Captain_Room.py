k = int(input())
room_number = list(map(int, input().split()))
c_room_number = ( sum(set(room_number))*k - sum(room_number) ) // (k - 1)
print(c_room_number)