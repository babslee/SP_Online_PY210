'''This script stores a list of donors and their donations and creates a report upon command'''
donors = [[]]*5
donors[0] = ['Alan', 234.32, 23433.93, 46480.43]
donors[1] = ['Ben', 565.34, 233905.49]
donors[2] = ['Charlie', 213820.43]
donors[3] = ['Dan', 238924.23, 970597.44, 291.49]
donors[4] = ['Eddy', 1830.32, 2084.49]
align_name = '{:20}'
align_sum = '{:11.2f}'
align_num = '{:9.0f}'
align_avg = '{:12.2f}'
align_sum_text = '{:11}'
align_num_text = '{:9}'
align_centerstring = '{:^15}'
dollar_string = ' $'

'''Takes the sum of all donor's donations'''
def donor_sum(donor_tuple):
    donators = 0
    for i in range(len(donor_tuple)):
        if i != 0:
            donators = donators + float(donor_tuple[i])
    return donators

'''Takes the average of all donors donations'''
def donor_average(donor_tuple):
    donor_avg = donor_sum(donor_tuple) / (len(donor_tuple)-1)
    return donor_avg

'''Outputs a list of all donor names'''
def donor_full_names(donor_tuple):
    donators = []
    for i in range(len(donor_tuple)):
        donators.append(donor_tuple[i][0])
    return donators

action_input = 'Choose from the following 3 actions: Send a Thank You, Create a Report, quit > '

if __name__ == '__main__':
    response = input(action_input)
    '''Will execute while the response is 'Send a Thank You' or 'Create a Report'''
    while response == 'Send a Thank You' or 'Create a Report':
        if response == 'Send a Thank You':
            '''Prompts for name'''
            name = input('What is the full name > ')
            '''Prints the donors when asked to list'''
            while name == 'list':
                for i in range(len(donors)):				
                    print(donors[i][0])
                name = input('What is the full name > ')
            donor_names = donor_full_names(donors)
            '''Adds names to donors list if not there already'''
            if name not in donor_names:
                donors.append([])
                donors[len(donors)-1].append(name)
            '''Prompts for donation amount'''
            amount = input('What is the donation amount > ')
            amount = float(amount)
            i = 0
            while donors[i][0] != name:
                i += 1
            donors[i].append(amount)
            '''Outputs message thanking donors for donation'''
            print('Hello {}, thank you for your generous donation of {:.2f}!'.format(name, amount))
            response = input(action_input)
        '''Creates the report'''
        if response == 'Create a Report':
            middle_string = ''
            '''Title string of the report'''
            top_string = align_name.format('Donor Name') + '  ' + 'Total Given' + '  ' + 'Num Gifts' + '  ' + 'Average Gift' + '\n' + '\n'
            print (top_string)
            '''Loops through all donors and outputs their donation information'''
            for i in range(len(donors)):
                donator_names = donor_full_names(donors)
                middle_string = middle_string + align_name.format(donator_names[i]) + dollar_string + align_sum.format(donor_sum(donors[i])) + '  ' + align_num.format(len(donors[i])-1) + dollar_string + align_avg.format(donor_average(donors[i])) + '\n'
            print (top_string + middle_string)
            response = input(action_input)
        else:
            break