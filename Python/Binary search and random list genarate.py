import random

random_lsit = []
n = 10

for i in range(n):
    random_lsit.append(random.randint(0,9))
random_lsit.sort(reverse=True)
print(random_lsit)

query = int(input())

low = 0
high = len(random_lsit) - 1

while low <= high:

    mid = (low + high) // 2

    if random_lsit[mid] == query:
        print(mid, random_lsit[mid])
        break
    elif random_lsit[mid] < query:
        high = mid - 1
    elif random_lsit[mid] > query:
        low = mid + 1


