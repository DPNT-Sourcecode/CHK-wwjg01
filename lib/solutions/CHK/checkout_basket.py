#main basket class - stores basket info and applies offers

price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

class Basket():
    invalid = False #whether this is an invalid basket
    items = {} # "item" : [amount, [bulk offers]]
    gof_offers =[]
    def __init__(self, skus, bulk_offers=[], gof_offers=[]):
        # Build our dict of items, first by determining item amounts
        for item in skus:
            if not price_table.get(item, False):
                self.invalid = True
            else:
                self.items[item] = [self.items.get(item, [0])[0] + 1, []]
        # Then add on bulk offers
        for offer in bulk_offers:
            temp = BulkOffer(offer)
            self.items[temp.item][1].append(temp)
        for offer in gof_offers:
            self.gof_offers.append(GofOffer(offer)) 
    
    def calc_price(self):
        final_price = 0
        for item in self.items:
            offers = sorted(item[1], key=BulkOffer.value)
            print(offers)
        return 0
        
# example bulk offer format - A.3.130
class BulkOffer():
    def __init__(self, offer):
        item, amt, price = offer.split('.')
        self.item = item
        self.amt = amt
        self.price = price
    
    def value(self):
        return self.price/self.amt
        
# type for '... get one free' offers. Supports getting more than one free.
class GofOffer():
    def __init__(self, offer):
        item, amt, bonus = offer.split('.')
        self.item = item
        self.amt = amt
        self.bonus = bonus