# Напишите программу, которая перебирает последовательность от 1 до 100.
# Для чисел кратных 3 она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5 печатать "Buzz".
# Для чисел которые кратны одновременно и 3 и 5 надо печатать "FuzzBuzz".
# Иначе печатать число.

for i in range(1, 101):  # iterate over the numbers in the loop for from 1 to 101 inclusive
    if i % 3 == 0 and i % 5 == 0:  # check divisibility up to 3 and 5
        print("FuzzBuzz")
    elif i % 3 == 0:  # check divisibility up to 3
        print("fuzz")
    elif i % 5  == 0:  # check divisibility up to 5
        print("buzz")
    else:
        print(i)
