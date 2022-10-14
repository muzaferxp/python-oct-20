import random

fixed_salary = 25000
incentive = 5
            
total_sales = 0

for i in range(1,31):
    todays_sale = random.randint(150,200)
    print(f"Day  {i} Sales : {todays_sale}")
    total_sales = total_sales + todays_sale

print("Total no. of sales", total_sales)

total_incentive = total_sales * incentive
total_salary = fixed_salary + total_incentive
print("Total salary:", total_salary)
