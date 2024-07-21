#main basket class - stores basket info and applies offers
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+

class Basket():
    # Ideally we'd have a simple db or more elegant storage, but for now a dict + 2 lists will do
    bulk_offers_list = ["A.3.130", "A.5.200", "B.2.45", "H.5.45", "H.10.80", "K.2.150"]
    gof_offers_list = ["E.2.B", "F.2.F", "N.3.M"]
    price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50
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
                
        # Build the '.. get one free' offers list
        for offer in self.gof_offers_list:
            temp = GofOffer(offer)
            # If a 'get one free' offer has the same letter for the offer and bonus, it's a bulk buy offer
            if temp.item == temp.bonus:
                self.bulk_offers_list.append(f'{temp.item}.{temp.amt+1}.{temp.amt*self.price_table[temp.item]}')
                continue
            
            if temp.item in self.items:
                self.gof_offers.append(temp)   
                  
        # Then add on bulk offers
        for offer in self.bulk_offers_list:
            temp = BulkOffer(offer)
            if temp.item in self.items:
                self.items[temp.item][1].append(temp)
            
            
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
        
