class Customer(object):
    '''customer class, we have many customers
    '''

    def __init__(self, money_in_account, interest_products, favorite_item='cotton-candy'):
        self.money_in_account = money_in_account
        self.favorite_item = favorite_item
        self.items_bought = []
        self.interest_products = interest_products

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
        return "Customer with {0} money\nitems bought: {1}\nfavorite item {2}\ninterest products {3}" \
            .format(
                self.money_in_account,
                self.items_bought,
                self.favorite_item,
                self.interest_products)

class Product(object):  

    manufacturer = "our factory seal"

    def __init__(self, price, sku, title=None, amount=0):
        self.price = price 
        self.sku = sku 
        self.title = title
        self.amount = amount
        self.in_stock = True

    def set_price(self, new_price):
        self.price = new_price

    def change_amount(self, new_amount):
        self.amount = new_amount
        if self.amount <= 0:
            self.in_stock = False
        return "amount left: {0}\n in stock: {1}".format(self.amount, self.in_stock)

    def __repr__(self):
        return "self.price {}".format(self.price)

apple = Product(10.99, bin(23), "granny smith", 100)
banana = Product(13.59, bin(34), "yellow", 33)

arik_smith = Customer(55, [apple, banana])

print arik_smith





