from sys import argv

script, hours, rate, prize = argv

def salary(hours, rate, prize):
    salary = (int(hours) * int(rate)) + int(prize)
    return salary

print(salary(hours, rate, prize))