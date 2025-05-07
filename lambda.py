from functools import reduce


numbers = [3, 7, 12, 18, 20, 21]
squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))
print(20 *"==")
###############################

odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(odd_nums)
print(list(odd_nums))
print(20 *"==")

#############################


numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)
print(sum(numbers, 10))
print(20 *"==")


names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)




