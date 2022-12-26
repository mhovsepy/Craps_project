import random
a = random.randint(1,6)
b = random.randint(1,6)
sum_numbers = a + b
i = 3
print("The sum of dice is", a, "+", b, "=", sum_numbers)
if sum_numbers == 7 or sum_numbers == 11:
        print("You won")
elif sum_numbers == 2 or sum_numbers == 3 or sum_numbers == 12:
        print('Casino win')
else:
        print("Your goal number is",  sum_numbers)
        while i != 0:
            d = random.randint(1,6)
            c = random.randint(1,6)
            sum_goals = d + c
            print("The sum of dice is", d, "+", c, "=", sum_goals)
            if sum_goals == 7:
                break
            elif sum_goals == sum_numbers:
                print("You won")
                raise SystemExit
            i -= 1
        print('You lose')