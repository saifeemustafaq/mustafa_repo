from itertools import permutations

a,b = input().split()

#lim = int(lim)
arr = [str(x) for x in a]
arr1 = []
ans = -1
perm = list(permutations(arr))

for x in perm:
    str1 = ''.join(x)
    arr1.append(str1)

arr1.sort()

for x in arr1:
    if x > b:
        ans = int(x)
        break


print(ans)
#second problem of TCS
#input: 459 500
#output: 549
