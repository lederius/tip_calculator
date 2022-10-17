
#this first function is used to validate the tip cost. 
# i wanted to figure out if the user was using a percentage or exact amount to tip
#here we pass the user submitted cost as an arguement
def validate_tip(cost):
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
                #here the tip is chagned from percent to a float
                tip = tip * 0.01
                #here tip is multiplied by cost becuase we need to get a tip amount based of the cost of the meal
                tip = tip * cost
                #here tip is rounded to a 2 digit decimal because floats can become rather long.
                tip = round(tip,2)
        # elif is used incase the user deems the tip value to be incorrect
        elif tip_type == 'n':
            #tip converted to a float to be in unison whenever a user gave an amount that was a whole number
            tip = float(input('What is the exact amount you want to tip? Numbers only: '))
            #correct here is to verify the tip amount is correct
            correct = input(f'Is the tip amount of ${tip} correct?: y/n: ')
            #here the use deems the tip is correct
            if correct == 'y':
                #here tip is multiplied by cost becuase we need to get a tip amount based of the cost of the meal
                tip *= cost
                #here tip is rounded to a 2 digit decimal because floats can become rather long.
                tip = round(tip, 2)    
        #edge cases can happen and i want to be prepared 
        else:
            tip_type =  input('Error, we just need a "y" or a "no for if your type will be a percentage.: ')
    #here we are outside of the while and we return tip
    #i might not need this now that I think about it
    return tip
#this funciton validates the cost to assure it was the customer is paying for thier meal
#we pass the cost that the user inputted earlier as a paramter
def validate_cost(cost):
    #here we want to verify the user has the cost they accept
    correct = input(f'Is ${cost} the correct price of your meal? y/n: ')
    #i use while once agian to contine loop until all the values are correct
    #i used isinstance beacause if it is ever a string or complex number those need to become float numbers
    while isinstance(cost, str) or isinstance(cost, complex) or correct != 'y':
        #cost is a user input value
        cost = input('We need an exct number for the cost of your meal!: ')
        #make sure the user accepts that cost.
        correct = input(f'The meal cost was ${cost}, is this correct? y/n : ')
    #outside the while loop all the values are correct so the cost is turned to a float then returned
    return round(cost, 2)

#here is the function that takes the tip and meal cost as parameters to determine the final value
def total_bill(tip, meal):
    #this is the only time the sales tax is needed so it didnt make sense to have this value anywhere else in this code
    #sales tax is a give rate of 10% 
    #sales tax value is then multipled by the cost of meal 
    #maybe sales tax is a poor name. Subtotal would have been better
    sales_tax = round((meal * 0.1),2)
    print(f'meal-->{meal}, tip-->{tip}, tax-->{sales_tax}')
    amount_of_people = int(input('How man people are splitting the bill? Numbers only: '))
    print(type(amount_of_people), "!!!")
    while isinstance(amount_of_people, str):
        print('ERROR, Can only be numbers')
        amount_of_people = input('How man people are splitting the bill? Numbers only :')
    #toatl bill is turned 
    total_bill = float(tip + meal + sales_tax)
    #the total bill is divided by the amount of people to determine the value of each person
    total_bill /= amount_of_people
    #take the total bill and return it as a float number with 2 decimals because that has change is
    return round(total_bill, 2)
