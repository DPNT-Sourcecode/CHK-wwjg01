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
        

def checkout(skus):
    # Build our basket from the str first
    basket = Basket(skus)
    if basket.invalid:
        return -1
    
    return basket.calc_price()




