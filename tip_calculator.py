#initial function that takes inputs for intial cost and peole qunatity
def user_input():
    print('Welcome to LeDerius Tip Calculator')
    try:
        cost_intial = float(input('What was the total cost of the cost_intial? '))
        amount_of_people = int(input('How man people are splitting the bill?: '))
    except ValueError:
        print('Please enter a valid number')
        return user_input()
    return validate_tip(cost_intial, amount_of_people)

# function that takes in cost of meal & people quantity to return
# tip amount.Passes these values to another function
def validate_tip(cost_intial, amount_of_people):
    tip_type =  input('Will your tip be based off percentange?: y/n ')
    # the correct variable is used to determine when the tip is correct and to exit the while loop
    correct = 'n'
    while isinstance(tip_type, str) and correct != 'y':
        if tip_type == 'y':
            tip = float(input('How much percent do you want to tip? Numbers only: '))
            #correct here is to verify the tip amount is correct
            correct = input(f'Is the tip amount of {tip}% correct?: y/n: ')
            if correct == 'y':
                tip = round(((tip * 0.01)*cost_intial),2)
        elif tip_type == 'n':
            tip = float(input('What is the exact amount you want to tip?: '))
            correct = input(f'Is the tip amount of ${tip} correct?: y/n: ')
            if correct == 'y':
                return total_bill(tip,cost_intial, amount_of_people)
        else:
            tip_type =  input('Error, we just need a "y" or a "no for if your type will be a percentage.: ')
    return total_bill(tip,cost_intial, amount_of_people)
# function that let users decide if they want to run a new calculation
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

#takes the tip and cost_intial & amount of people to
#determine final amount user will pay.
def total_bill(tip,cost_intial, amount_of_people):
    subtotal = round((cost_intial * 0.1),2)
    print(f'cost_intial-->{cost_intial}, tip-->{tip}, tax-->{subtotal}')
    # amount_of_people = int(input('How man people are splitting the bill? Numbers only: '))
    #toatl bill is turned 
    total_bill = float(tip + cost_intial + subtotal)
    total_bill = round((total_bill /amount_of_people), 2)
    print(f'{total_bill} per person')
    repeat()    
user_input()