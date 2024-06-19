# for loop
# for item in ['Mosh', 'John', 'Sarah']:
#     print(item)


# exercise - imaginary shopping cart
# prices = [10, 20, 30]

# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")


# write a program to remove the duplicates in a list
numbers = [5, 3, 2, 5, 6, 2, 7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
