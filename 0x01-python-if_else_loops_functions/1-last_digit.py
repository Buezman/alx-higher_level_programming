#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = ""
if number < 0:
    number *= -1
    sign = "-"
last_digit = number % 10
end = ""
if last_digit > 5:
    end += "greater than 5"
elif last_digit == 0:
    end += "0"
else:
    end += "less than 6 and not 0"
print(f"Last digit of {number} is {sign}{last_digit} and is {end}")
