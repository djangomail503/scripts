def even_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num  # Yield even numbers

for even_num in even_numbers(0, 10):
    print(even_num)  # Output: 0 2 4 6 8 10
