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
    def calc_bulk_price(self, item):
        this_item_total = 0
        this_item_left = self.items[item][0]
        # sort our offers by their value, so that we can ensure customer gets best deal
        offers = sorted(self.items[item][1], key=BulkOffer.value)
        for offer in offers:
            if offer.amt > this_item_left:
                continue
            this_item_total += (this_item_left//offer.amt)*offer.price
            this_item_left = this_item_left%offer.amt
        this_item_total += this_item_left*price_table[item]
        return this_item_total
    
    def calc_price(self):
        final_price = 0
        prices = {
        "A": -1,
        "B": -1,
        "C": -1,
        "D": -1,
        "E": -1
        }
        for item in self.items:
            price = self.calc_bulk_price(item)
            final_price += price
            prices[item] = price
                
        for offer in self.gof_offers:
            pass
                
        return final_price
        
# example bulk offer format - A.3.130
class BulkOffer():
    def __init__(self, offer):
        split_list = offer.split('.')
        self.item = split_list[0]
        self.amt = int(split_list[1])
        self.price = int(split_list[2])
    
    def value(self):
        return self.price / self.amt
        
# type for '... get one free' offers. Supports getting more than one free.
class GofOffer():
    def __init__(self, offer):
        split_list = offer.split('.')
        self.item = split_list[0]
        self.amt = split_list[1]
        self.bonus = split_list[2]
        
bask = Basket("AAABB", ["A.3.130", "A.5.200", "B.2.45"])
print(bask.calc_price())
