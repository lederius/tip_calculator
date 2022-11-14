
def user_input():
    print('Welcome to LeDerius Tip Calculator')
    try:
        cost_intial = float(input('What was the total cost of the cost_intial? '))
        amount_of_people = int(input('How man people are splitting the bill?: '))
    except ValueError:
        print('Please enter a valid number')
        return user_input()
    return validate_tip(cost_intial, amount_of_people)


# the cost varaible is given the value of the cost of the cost_intial that the user wants
# cost = validate_cost(cost_intial)
# print('cost -->', cost)
# this tip variable is given the value of the functions that validates the the tip is tip the user wants
# tip = validate_tip(cost_intial)
# here we print out the total bill in a nice sentence for the customer
# print(f'Well your total today {name} will be ${total_bill(tip, cost)}!!')




#this first function is used to validate the tip cost. 
# i wanted to figure out if the user was using a percentage or exact amount to tip
#here we pass the user submitted cost as an arguement
def validate_tip(cost_intial, amount_of_people):
    #to determine between percent and exact amount
    tip_type =  input('Will your tip be based off percentange?: y/n ')
    # the correct variable is used to determine when the tip is correct and to exit the while loop
    correct = 'n'
    # i went with the isistnace to determine is the tip_type is a string or not
    #i want to exit the while when the tip_type is no longer a string
    while isinstance(tip_type, str) and correct != 'y':
        #there are 3 if statements if, elif, else all dealing with tip_tpe
        if tip_type == 'y':
            #tip converted to a float to be in unison whenever a user gave an amount that was a whole number
            tip = float(input('How much percent do you want to tip? Numbers only: '))
            #correct here is to verify the tip amount is correct
            correct = input(f'Is the tip amount of {tip}% correct?: y/n: ')
            if correct == 'y':
                #feedback: dont redeclare tip 3 dif times
                #here the tip is chagned from percent to a float
                tip = tip * 0.01
                #here tip is multiplied by cost becuase we need to get a tip amount based of the cost of the cost_intial
                tip = tip * cost_intial
                #here tip is rounded to a 2 digit decimal because floats can become rather long.
                tip = round(tip,2)
        # elif is used incase the user deems the tip value to be incorrect
        elif tip_type == 'n':
            #tip converted to a float to be in unison whenever a user gave an amount that was a whole number
            tip = float(input('What is the exact amount you want to tip?: '))
            #correct here is to verify the tip amount is correct
            correct = input(f'Is the tip amount of ${tip} correct?: y/n: ')
            #here the use deems the tip is correct
            if correct == 'y':
                ##here tip is multiplied by cost becuase we need to get a tip amount based of the cost of the cost_intial
                #tip *= cost
                ##here tip is rounded to a 2 digit decimal because floats can become rather long.
                #tip = round(tip, 2)    
                #feedback: above code broken, tip doesn't need to be multiplied when exact amount
                return total_bill(tip,cost_intial, amount_of_people)
        #edge cases can happen and i want to be prepared 
        else:
            tip_type =  input('Error, we just need a "y" or a "no for if your type will be a percentage.: ')
    #here we are outside of the while and we return tip
    #i might not need this now that I think about it
    return total_bill(tip,cost_intial, amount_of_people)
#this funciton validates the cost to assure it was the customer is paying for thier cost_intial
#we pass the cost that the user inputted earlier as a paramter


def repeat():
    start_over = input('Do you want to start over? Please enter y/n: ')
    try:
        if start_over == 'n':
            print('Thank you for using my calculator')
        elif start_over == 'y':
            user_input()
        else:
            raise Exception
    except Exception:
        print('Your entry was invalid. Try again')
        repeat()

#here is the function that takes the tip and cost_intial cost as parameters to determine the final value
def total_bill(tip,cost_intial, amount_of_people):
    #this is the only time the sales tax is needed so it didnt make sense to have this value anywhere else in this code
    #sales tax is a give rate of 10% 
    #sales tax value is then multipled by the cost of cost_intial 
    #maybe sales tax is a poor name. Subtotal would have been better
    sales_tax = round((cost_intial * 0.1),2)
    print(f'cost_intial-->{cost_intial}, tip-->{tip}, tax-->{sales_tax}')
    # amount_of_people = int(input('How man people are splitting the bill? Numbers only: '))
    #toatl bill is turned 
    total_bill = float(tip + cost_intial + sales_tax)
    #the total bill is divided by the amount of people to determine the value of each person
    total_bill = round((total_bill /amount_of_people), 2)
    #take the total bill and return it as a float number with 2 decimals because that has change is
    print(f'{total_bill} per person')
    repeat()    
user_input()