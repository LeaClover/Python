# Суперсдвиг


n = int(input())
list_first = list()
list_result = [0] * n
for i in range(n):
    list_first.append(int(input()))
print(*list_first)

k = int(input())
k = k % n
if k < 0:
    k = -k
for i in range(k):
    list_result[i] = list_first[n - k + i]
for i in range(n - k):
    list_result[k + i] = list_first[i]
print(*list_result)