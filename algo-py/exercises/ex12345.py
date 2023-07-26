# câu 1:
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


'''
2. Độ phức tạp thời gian sẽ là O(1) khi chèn 1 phần từ dữ liệu sau một phần tử được chỉ bởi con trỏ trong danh sách được liên kết
nếu như mình biết vị trí của phần tử đó. Nếu như không thì độ phức tạp sẽ là O(n) bởi vì chúng ta phải duyệt qua các phần tử trong
danh sách để tìm phần tử đó.

3. Độ phức tạp về thời gian khi xác định độ dài của danh sách liên kết đã cho là O(1) bởi vì ta biết số phần tử trong danh sách.

4. Độ phức tạp thời gian trong trường hợp xấu nhất để tìm kiếm một phần tử đã cho trong danh sách liên kết đơn có độ dài n là O(n).
Bởi vì ta phải duyệt qua các phần tử trong danh sách để tìm được 1 phần từ mà ta muốn tìm. 

5. Nếu như một danh sách liên kết cho trước chỉ có một con trỏ head trỏ tới điểm bắt đầu của danh sách thì độ phức tạp về thời gian
cho các thao tác sau sẽ là O(1) cho các thao tác như chèn phần tử vào đầu danh sách, truy cập phần tử đầu tiên và xóa 1 phần tử đầu
danh sách. Tuy nhiên, truy cập phần tử bất kì trong danh sách thì sẽ là O(n).
'''
