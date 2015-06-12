item_prices = [6.9512394087, 19.45, 4.0, 4.0, 13.95]

def calc_20perc_tax_allitems(items):
    tax_items_ls = []
    for i in items:
        if 2.0 > i * .20:
            tax_items_ls.append( i * 2.0 )
        else:
             tax_items_ls.append( 0.0 )

    return tax_items_ls


#print calc_20perc_tax_allitems(item_prices)



total_tax_items = [round(x * .2, 1) for x in 
            item_prices if x * .2 > 2.0]

print total_tax_items









'''
print '\n'
print round(13.9087294, 2) #round to 2 decimal points for US Dollar standard
print '\n'

empty_list = []

for ltr in 'abcdefg':
    empty_list.append(ltr)

print empty_list


'''