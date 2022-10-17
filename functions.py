
def validate_tip(cost):
    tip_type =  input('Will your tip be based off percentange?: y/n ')
    correct = 'n'
    while isinstance(tip_type, str) and correct != 'y':
        if tip_type == 'y':
            tip = float(input('How much percent do you want to tip? Numbers only: '))
            correct = input(f'Is the tip amount of {tip}% correct?: y/n: ')
            if correct == 'y':
                tip = tip * 0.01
                print(f'the tip before cost {tip}')
                tip = tip * cost
                tip = round(tip,2)
                print(f'the tip {tip}')
        elif tip_type == 'n':
            tip = float(input('What is the exact amount you want to tip? Numbers only: '))
            correct = input(f'Is the tip amount of ${tip} correct?: y/n: ')
            if correct == 'y':
                tip *= cost
                tip = round(tip, 2)     
        else:
            input('Error, we just need a "y" or a "no for if your type will be a percentage.: ')
            print(f'the tip --> {tip}')
        print(f'tip-->{tip}')
    return tip

def validate_cost(cost):
    correct = input(f'Is ${cost} the correct price of your meal? y/n: ')
    while isinstance(cost, str) or isinstance(cost, complex) or correct != 'y':
        cost = input('We need an exct number for the cost of your meal!: ')
        correct = input(f'The meal cost was ${cost}, is this correct? y/n : ')
    return round(cost, 2)


def total_bill(tip, meal):
    sales_tax = round((meal * 0.1),2)
    print(f'meal-->{meal}, tip-->{tip}, tax-->{sales_tax}')
    amount_of_people = int(input('How man people are splitting the bill? Numbers only: '))
    print(type(amount_of_people), "!!!")
    while isinstance(amount_of_people, str):
        print('ERROR, Can only be numbers')
        amount_of_people = input('How man people are splitting the bill? Numbers only :')
    total_bill = float(tip + meal + sales_tax)
    total_bill /= amount_of_people
    return round(total_bill, 2)
