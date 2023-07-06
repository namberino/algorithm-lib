import random as rnd

length = int(input("Enter the length of the array: "))
print()


arr = [0] * length
print(f"Initialized an array of size {length}")
print(arr)
print()


print("Inserting a value into a certain spot of the array")
arr[1] = 42
arr[5] = 92

print(arr)
print()


print("Inserting some extra elements to the array to make the next assignments more coherent")
for i in range(len(arr)):
    if arr[i]:
        continue
    rand = rnd.randint(1, 10)
    arr[i] = rand
print(arr)
print()


print("Removing an element at a specific position in the array")
arr.pop(6)

print(arr)
print()


print("Removing an element of a specified value in the array")
print("Removing element \"42\"")
arr.remove(42)

print(arr)
print()


print("Specifying the position of the element with the specified value in the array") 
print("Position of a value \"92\" in the array is %i" % arr.index(92))

print(arr)
