from functions import *

#name = input('What is your name?: ')
#print(name)
#print(f'Let get started with find the amount you will be paying today {name}!')
cost_intial =  float(input('What was the total cost of the meal? Numbers only: '))

tip = validate_tip(cost_intial)
cost = validate_cost(cost_intial)


#initial_cost(cost_intial, sales_tax, tip)
#print(total_bill(tip, cost), 'total bill')