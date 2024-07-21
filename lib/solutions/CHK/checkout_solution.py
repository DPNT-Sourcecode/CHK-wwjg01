from lib.solutions.CHK.checkout_basket import Basket

# noinspection PyUnusedLocal
# skus = unicode string

# skus - a string containing items in basket
'''
Our price table and offers: 
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
'''

# Implement the price table as a dict
price_table = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}


bulk_offers_list = ["A.3.130", "A.5.200", "B.2.45"]
gof_offers_list = ["E.2.B"]

def checkout(skus):
    # Build our basket from the str first
    basket = Basket(skus, bulk_offers_list, gof_offers_list)
    if basket.invalid:
        return -1
    
    return basket.calc_price()

            
        
