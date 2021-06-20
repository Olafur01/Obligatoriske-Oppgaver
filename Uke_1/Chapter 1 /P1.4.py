year = 0
initial_balance = 1000
interest = 0.05
while year < 3:
    initial_balance = initial_balance * (1 + interest)
    year += 1
print(initial_balance)
