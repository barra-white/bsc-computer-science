import math

monthly_cost = 0.023 # per whole GB (in USD)
data_per_month = 0.830448 # in GB

n = 1 # month
cost = 0 # cost per month
total = 0 # total cost
while n < 13:
    data = data_per_month * n # data per month (accumulated)
    # always round up as it is charged per whole GB
    rounded_data = math.ceil(data) # rounded data per month 
    cost = rounded_data * monthly_cost
    total += cost
    print('Month', n, 'cost:', cost, 'USD')
    print('Month', n, 'data:', data, 'GB')
    print("Rounded Data", n, ":", rounded_data, "GB\n")
    n += 1

print('Total cost:', total, 'USD')