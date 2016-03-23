class Customer(object):
    '''customer class, we have many customers
    '''

    def __init__(self, money_in_account, favorite_item='cotton-candy'):
        self.money_in_account = money_in_account
        self.favorite_item = favorite_item
        self.items_bought = []

    def add_bought_item(self, bought_item):
        self.items_bought.append( bought_item ) 

    def add_money(self, amount):
        self.money_in_account += amount

    @property
    def future_money(self):
        return self.money_in_account * 3

    #def __add__(self, other):
    #    return str(self.favorite_item) * 5

    def __repr__(self):
        return "Customer with {0} money\nitems bought: {1}\nfavorite item {2}" \
            .format(
                self.money_in_account,
                self.items_bought,
                self.favorite_item)

arik_smith = Customer(1000, "popcorn")

#print dir(customer)

print arik_smith.money_in_account
print arik_smith.favorite_item
print arik_smith.items_bought


arik_smith.add_bought_item("apple")
print arik_smith.items_bought

arik_smith.add_money(122)
print arik_smith.money_in_account

arik_smith.money_in_account -= 555
print arik_smith.money_in_account


def new_function( attr1, key_word1="string values"):
    return attr1, key_word1

new_f = new_function("this is attr1", "key word value")
print new_f

#print arik_smith.__add__("bananas")

#print arik_smith + "bananas"
print '\n\n\n'

print dir(arik_smith)
print "\n"
print arik_smith.__doc__
print arik_smith.__class__
print "\n"
print arik_smith.__dict__
arik_smith.__dict__['favorite_item'] = 'blue balloons'
print "\n"
print arik_smith.__dict__


print arik_smith.__class__
print type(arik_smith)

print arik_smith.future_money