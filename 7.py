'''
Question:
What is the 10,001-st prime?
'''
number = 1
which = 0
while which != 10001:
    number += 1
    divisors = 0
    for i in range (number):
        if number % (i+1) == 0:
            divisors += 1
    if divisors == 2:
        which += 1
        print(f"{which}-th prime is {number}")
print(number)