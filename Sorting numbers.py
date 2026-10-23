# amir mohammad hossein zade

count = int(input("enter the number of numbers: "))

numbers = [0] * count

for i in range(count):
    numbers[i] = int(input("enter the number: "))

for i in range(count - 1):
    for j in range(count - 1 - i):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("sorted numbers:")
print(numbers)
