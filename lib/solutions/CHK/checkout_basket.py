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
