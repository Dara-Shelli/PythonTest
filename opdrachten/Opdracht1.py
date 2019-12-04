from random import randint, random

sick_days = randint(0, 10)
print(sick_days)
calling_in_sick = False

while not calling_in_sick and sick_days > 0:
    actually_sick = bool(random)
    kinda_sick = bool(random)
    dont_feel_like_it = bool(random)
    if actually_sick and sick_days > 0:
        calling_in_sick = True
        sick_days -= 1
    elif kinda_sick and dont_feel_like_it:
        calling_in_sick = True
        sick_days -= 1

    print(f'Sick sad world {calling_in_sick}')

else:
    print(f'You still have {sick_days}')
