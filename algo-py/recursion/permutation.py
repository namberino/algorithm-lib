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

for perm in permute([1, 2, 3]):
    print(perm)


'''
We basically generate a stack, each iteration of the stack would have 2 arrays, 1st is the array2, 2nd is the permutation array.
Each iteration, we grab the first elemnent on the stack and iterate through it using a for loop, and we would grab the ith element
of the array2 and put it into the permutation array.
We do this until the array2 is empty, then we can yield the permutation array.
Repeat till stack is empty.

This would take O(n * n!) because n! for the amount of permutations and O(n) for time it takes to reach a permutation
'''
