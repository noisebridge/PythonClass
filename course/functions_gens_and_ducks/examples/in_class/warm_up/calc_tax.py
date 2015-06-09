def print_15perc_total_tax(bill):
    '''return the amount of money to pay in tax in US dollars
    '''
    bill = float(bill)

    total_tax = str( bill * .15 )
    

    return "please graciously pay at least the amount of {} in total tax ".format(total_tax)



print print_15perc_total_tax(79)



