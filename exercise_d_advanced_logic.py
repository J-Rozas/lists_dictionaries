# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

# 2. Print the difference between the largest and smallest value:
largest = max(numbers)
smallest = min(numbers)
difference_largest_smallest = largest - smallest
print(difference_largest_smallest)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

for index in range(0, len(numbers) - 1):
    if numbers[index] == 2 and numbers[index + 1] == 2:
        print(True)
        break

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

special_sum = 0
ignore_number = False

for number in numbers:
    if number == 6:
        ignore_number = True
        continue

    if number == 7:
        ignore_number = False
        continue

    if ignore_number == False:
        special_sum += number

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

hard_sum = 0

for index in range(0, len(numbers)):
    if index == 0:
        if index == 13:
            pass
        else:
            hard_sum += numbers[index]
    else:
        if numbers[index] == 13 or numbers[index - 1] == 13:
            pass
        else:
            hard_sum += numbers[index]

print(hard_sum)






