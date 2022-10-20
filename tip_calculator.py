#here we import all our functions from another page
from functions import *

#here we get the users name
name = input('What is your name?: ')
print(f'Let get started with find the amount you will be paying today {name}!')
# this input just grabs the value of the meal and converts it to a float number and uses that input for our initial cost
#the initial cost is needed because it is used in the first function which is the tip function
#feedback: don't use float() but take input and put in loop
#feedback: use "try" "except"
#feeback: try abnormal test cases for bad behavior & unsual inputs
cost_intial =  float(input('What was the total cost of the meal? Numbers only: '))
# this tip variable is given the value of the functions that validates the the tip is tip the user wants
tip = validate_tip(cost_intial)
# the cost varaible is given the value of the cost of the meal that the user wants
cost = validate_cost(cost_intial)
# here we print out the total bill in a nice sentence for the customer
print(f'Well your total today {name} will be ${total_bill(tip, cost)}!!')