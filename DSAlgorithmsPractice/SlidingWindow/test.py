from collections import defaultdict

arr = [1, 2, 4, 4]
k = 2

mp = defaultdict(lambda: 0)

dist_count = 0

res = []

for i in range(k):
    if mp[arr[i]] == 0:
        dist_count += 1
    mp[arr[i]] += 1

res.append(dist_count)

print(mp)
print(res)