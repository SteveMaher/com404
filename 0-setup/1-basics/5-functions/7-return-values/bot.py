# Return Values
# Function to sum the weights
def sum_weights(beep, bop):
    totalweight = beep + bop
    return totalweight
    print("The sum of Beep and Bop's weight is", sum_weights())

# Function to average the weights
def calc_avg_weight(beep, bop):
    averageweight = beep + bop / 2
    return averageweight
    print("The aveage weight of Beep and Bop is", calc_avg_weight())

# Function for user to input weights, decide if sum or average and the call correct function
def run():
    beep = int(input('What is the weight of Beep?\n'))
    bop = int(input('What is the weight of Bop?\n'))
    question = input('What would you like to calculate (sum or average)?\n')
    if question == 'sum':
        sum_weights(beep, bop)
    elif question == 'average':
        calc_avg_weight(beep, bop)
    else:
        print('Invalid entry, I can only sum or average. Please try again')

# Run the program
run()