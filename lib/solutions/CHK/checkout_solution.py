

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
# key - item SKU / id, value - list where 0th index is price, following indexes are tuples representing bulk deal, if any
price_table = {
    "A": [50, (3, 130)],
    "B": [30, (2, 45)],
    "C": [20],
    "D": [15]
}
def checkout(skus):
    final_price = 0
    basket = {}
    for item in skus:
        if not price_table.get(item, False):
            return -1
        else:
            basket[item] = basket.get(item, 0) + 1

            
        


