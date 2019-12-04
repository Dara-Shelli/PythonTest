group_of_people = ['Alex', 'Elliot', 'Veronica', 'Lucy', 'Wouter', 'Bart']
first_chars = [x[0] for x in group_of_people]

print(first_chars)

numbers = list(range(100))
sum = 0
for number in numbers:
    sum += number
print(f'the sum is: {sum}')