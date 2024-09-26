numbers = []
for numbers in numbers:
    print(numbers, range(1, 21))

numbers_1 = list(range(1, 1000000))
for num in numbers_1:
    print(num)
min_value = min(numbers_1)
max_value = max(numbers_1)
sum_value = sum(numbers_1)
print(min_value, max_value, sum_value)


odd_numbers = list(range(1, 20, 2))
for num in odd_numbers:
    print(num)

multiples = list(range(3, 30, 3))
for num in multiples:
    print(num)

cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

cubes = [value**3 for value in range(1, 11)]
print(cubes)