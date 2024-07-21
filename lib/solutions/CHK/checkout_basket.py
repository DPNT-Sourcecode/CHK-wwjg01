#main basket class - stores basket info and applies offers


class Basket():
    bulk_offers_list = ["A.3.130", "A.5.200", "B.2.45"]
    gof_offers_list = ["E.2.B"]
    price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}
    def __init__(self, skus):
        self.invalid = False
        self.items = {}
        self.gof_offers = []
        
        # Build our dict of items, first by determining item amounts
        for item in skus:
            if not self.price_table.get(item, False):
                self.invalid = True
            else:
                self.items[item] = [self.items.get(item, [0])[0] + 1, []]
        
        # Then add on bulk offers
        for offer in self.bulk_offers_list:
            temp = BulkOffer(offer)
            if temp.item in self.items:
                self.items[temp.item][1].append(temp)
            
        for offer in self.gof_offers_list:
            temp = GofOffer(offer)
            if temp.item in self.items:
                self.gof_offers.append(temp) 
            
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
        this_item_total += this_item_left*self.price_table[item]
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
            if offer.bonus in self.items:
                prices[offer.bonus] = min(prices[offer.item], self.calc_bulk_price(offer.bonus, free_item_amt))
               
        final_price = 0
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
        


