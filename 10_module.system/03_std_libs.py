import random
from datetime import datetime, date, time
# generate a random integer between 1 and 100


def game():
    rand_int = random.randint(1, 100)
    steps = 0

    while True:
        user_number = input("Enter a number between 1 and 100: ")
        steps += 1
        # you can separate the validation logic into a function if needed
        if user_number.isdigit():
            user_int = int(user_number)
            if 1 > user_int or user_int > 100:
                print("Please enter a valid number.")
                continue
            if user_int < rand_int:
                print("Too low! Try again.")
            elif user_int > rand_int:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {steps} steps.")
                break
        else:
            print("Please enter a valid number.")


# game()

num_list = [1, 2, 3, 4, 5]
random.shuffle(num_list)
print(num_list)

print(random.choice(num_list))

print(datetime.now())
print(datetime(2020, 5, 6, 15, 12, 12, 50000))
# https://docs.python.org/3/library/datetime.html
print(datetime(2020, 5, 6, 15, 12, 12, 50000).strftime("%Y. %B. %d. %H:%M:%S"))
print(datetime(2020, 5, 6, 15, 12, 12, 50000).isoformat())
d1 = date(2020, 5, 6)
d2 = date(2021, 4, 16)
print((d2 - d1).days)

d = date(2025, 1, 1)
print(d)
t = time(14, 30, 15)
print(t)
dt = datetime.combine(d, t)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
