#main basket class - stores basket info and applies offers

class Basket():
    # Ideally we'd have a simple db or more elegant storage, but for now a dict + 2 lists will do
    bulk_offers_list = ["A.3.130", "A.5.200", "B.2.45", "H.5.45", "H.10.80", "K.2.150", "P.5.200", "Q.3.80", "V.2.90", "V.3.130"]
    gof_offers_list = ["E.2.B", "F.2.F", "N.3.M", "R.3.Q", "U.3.U"]
    group_offers_list = ["STXYZ.3.45"]
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
        
        # Very bruteforcy, basically enforcing one single group offer rather than allowing adding more,
        # but due to time constraints of the assignment, do this for now
        self.group_offer = GroupOffer(self.group_offers_list[0])
        
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
    def calc_single_group_price(self, item, free_amt = 0):
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
        group_offer_items = []
        # Calculate prices for each item group
        for item in self.items:
            if item in self.group_offer.items:
                for i in range(self.items[item][0]):
                    group_offer_items.append(self.price_table[item])
                continue
            price = self.calc_single_group_price(item)
            prices[item] = price
            
        # Apply 'buy X get one free' type offers        
        for offer in self.gof_offers:
            amt = self.items[offer.item][0]
            free_item_amt = amt//offer.amt
            if offer.bonus in self.items:
                prices[offer.bonus] = min(prices[offer.item], self.calc_single_group_price(offer.bonus, free_item_amt))
               
        final_price = 0
        for price in prices:
            final_price += prices[price] 
            
        #how much the customer paid for items discounted by the group offer
        group_offers_num = len(group_offer_items)//self.group_offer.amt
        final_price += group_offers_num*self.group_offer.price
        
        #see if any items were left over and add them, assume the offer applied to the most expensive ones
        print(group_offer_items)
        print(sorted(group_offer_items)[:len(group_offer_items) - group_offers_num*self.group_offer.amt])
        for item in sorted(group_offer_items)[:len(group_offer_items) - group_offers_num*self.group_offer.amt]:
            final_price += item
        
        return final_price
        
# example bulk offer format - A.3.130
class BulkOffer():
    def __init__(self, offer):
        item, amt, price = offer.split('.')
        self.item = item
        self.amt = int(amt)
        self.price = int(price)
    
    def value(self):
        return self.price / self.amt
        
# type for '... get one free' offers. Examopke fornat - E.2.B
class GofOffer():
    def __init__(self, offer):
        item, amt, bonus = offer.split('.')
        self.item = item
        self.amt = int(amt)
        self.bonus = bonus

class GroupOffer():
    def __init__(self, offer):
        items, amt, price = offer.split('.')
        self.items = items
        self.amt = int(amt)
        self.price = int(price)


