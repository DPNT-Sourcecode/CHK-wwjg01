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
            
    # Calculate price for single item group, accounting for bulk offers
    def calc_bulk_price(self, item, free_amt = 0):
        this_item_total = 0
        this_item_left = self.items[item][0] - free_amt
        if this_item_left <= 0:
            return 0
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
        prices = dict.fromkeys(self.items.keys(), 0)
        
        # Calculate prices for each item group
        for item in self.items:
            price = self.calc_bulk_price(item)
            prices[item] = price
            
        # Apply 'buy X get one free' type offers        
        for offer in self.gof_offers:
            amt = self.items[offer.item][0]
            free_item_amt = amt//offer.amt
            prices[offer.bonus] = min(prices[offer.item], self.calc_bulk_price(offer.bonus, free_item_amt))
               
        final_price = 0
        print(prices)
        for price in prices:
            final_price += prices[price] 
            
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
        
# type for '... get one free' offers. Examopke fornat - E.2.B
class GofOffer():
    def __init__(self, offer):
        split_list = offer.split('.')
        self.item = split_list[0]
        self.amt = int(split_list[1])
        self.bonus = split_list[2]
        

