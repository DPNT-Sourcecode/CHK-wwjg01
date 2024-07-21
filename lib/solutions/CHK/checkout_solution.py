

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
    "A": [50, (3, 130)],
    "B": [30, (2, 45)],
    "C": [20],
    "D": [15]
}
def checkout(skus):
    final_price = 0
    basket = {}
    # Build our basket from the str first
    for item in skus:
        if not price_table.get(item, False):
            return -1
        else:
            basket[item] = basket.get(item, 0) + 1
    
    # Iterate over our basket and determine final price:
    for item in basket:
        num_of_deals = 0
        remainder = 0
        
        if len(price_table[item]) > 1:
            return 

            
        
