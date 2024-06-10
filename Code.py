def get_string_length(s):
    length = 0
    for _ in s:
        length += 1
    return length

def filter_strings(arr):
    new_arr = []
    for s in arr:
        if get_string_length(s) <= 3:
            new_arr.append(s)
    return new_arr

n = int(input("Введите количество строк в массиве: "))
strings = []

for i in range(n):
    strings.append(input(f"Введите строку {i + 1}: "))

new_strings = filter_strings(strings)

print("Новый массив строк с длиной <= 3 символов:")
for s in new_strings:
    print(s)