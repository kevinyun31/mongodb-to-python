# 1. 리스트 list1 = []
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

print(list1[2])
print("="*50)

# 더하기 (중요)
list3 = list1 + list2
print(list3)

# 3 스칼라
# [1,3,4] 벡터

# 2차원 배열 만들기 (중요)
# 2차원 matrix, 3차원 tensor
list4 = [
    list1,
    list2
]

print(list4)

list1.append(10)

print(list1)

del list1[0]
print(list1)

list1.remove(2)

print(list1)

list6 = list(range(10))
print(list6)

list7 = list(range(1, 12))  # 마지막 인덱스 직전까지
print(list7)

list7[0] = 100

# 2. 튜플 - 리스트 같음 !! 데이터 변경이 불가능
tuple1 = (1, 2, 3)
print(tuple1)

tuple2 = (4, 5, 6)

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = (tuple1, tuple2)
print(tuple4)

list10 = list(tuple1)
print(list10)
