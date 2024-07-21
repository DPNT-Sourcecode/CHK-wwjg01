

# noinspection PyUnusedLocal
# skus = unicode string

# skus - a string containing items in basket
'''
Our price table and offers: 
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
'''

# Implement the price table as a dict
# key - item SKU / id, value - list where 0th index is price, following index is tuple representing bulk deal, if any
price_table = {
    "A": [50],
    "B": [30],
    "C": [20],
    "D": [15]
}
#main basket class - stores basket info and applies offers
class Basket():
    total = 0 #total price of our basket
    invalid = False #whether this is an invalid basket
    items = {} # "item" : amount
    bulk_offers = []
    gof_offers =[]
    def __init__(self, skus, bulk_offers=[], gof_offers=[]):
        for item in skus:
            if not price_table.get(item, False):
                self.invalid = True
            else:
                self.items[item] = self.items.get(item, 0) + 1
                
        for offer in bulk_offers:
            self.bulk_offers.append(BulkOffer(offer))
        for offer in gof_offers:
            self.gof_offers.append(GofOffer(offer)) 
        
        
# example bulk offer format - A.3.130
class BulkOffer():
    def __init__(self, offer):
        item, amt, price = offer.split('.')
        self.item = item
        self.amt = amt
        self.price = price
        
# type for '... get one free' offers. Supports getting more than one free.
class GofOffer():
    def __init__(self, offer):
        item, amt, bonus = offer.split('.')
        self.item = item
        self.amt = amt
        self.bonus = bonus

bulk_offers_list = [""]
gof_offers_list = []

def checkout(skus):
    final_price = 0
    # Build our basket from the str first
    basket = Basket(skus)
    if basket.invalid:
        return -1
    # Iterate over our basket and determine final price:
    for item in basket.items:
        num_items = basket.items[item]
        price = price_table[item][0]
        
        if len(price_table[item]) > 1:
            bulk_amt = price_table[item][1][0]
            bulk_price = price_table[item][1][1]
            final_price += (num_items//bulk_amt)*bulk_price + (num_items%bulk_amt)*price
        else:
            final_price += num_items*price
    
    return final_price

            
        

