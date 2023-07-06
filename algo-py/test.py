def permute(arr):
    stack = [(arr, [])]

    while stack:
        arr2, perm = stack.pop()

        if not arr2:
            yield perm
        
        for i in range(len(arr2)):
            newArr2 = arr2[:i] + arr2[i+1:]
            newPerm = perm + [arr2[i]]
            stack.append((newArr2, newPerm))

count = 0

for i in permute([1, 2, 3, 4]):
    count += 1
    print(i)
print(count)
