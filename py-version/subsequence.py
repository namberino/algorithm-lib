def longest_increasing_subsequence(array):
    n = len(array)
    L = [1] * n

    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j]:
                L[i] = max(L[i], L[j] + 1)
                
    max_length = max(L)
    result = []

    for i in range(n - 1, -1, -1):
        if L[i] == max_length:
            result.append(i)
            max_length -= 1
            
    result.reverse()
    return result


array = [1, 2, 3, 8, 9, 4, 5, 6, 2, 3, 9, 10]
print(f"Length: {len(array)}")
result = longest_increasing_subsequence(array)
for i in result:
    print(f'a[{i + 1}] = {array[i]}')
