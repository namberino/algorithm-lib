def insertion_sort(students):
    for i in range(1, len(students)):
        key = students[i];
        value = key["gpa"];
        j = i - 1;

        while j >= 0 and students[j]["gpa"] < value:
            students[j + 1] = students[j];
            j -= 1;

        students[j + 1] = key;

students = [
    {"name": "Nam", "id": "A001", "gpa": 3.5},
    {"name": "Nick", "id": "B002", "gpa": 3.8},
    {"name": "Nathan", "id": "C003", "gpa": 3.2},
    {"name": "Norton", "id": "D004", "gpa": 4.0}
];

print("Unsorted");
for student in students:
    print(student);

insertion_sort(students);
print();

print("Sorted");
for student in students:
    print(student);
