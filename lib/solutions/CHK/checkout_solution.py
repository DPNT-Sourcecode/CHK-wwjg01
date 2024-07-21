from solutions.CHK.checkout_basket import Basket

# noinspection PyUnusedLocal
# skus = unicode string

# skus - a string containing items in basket  

def checkout(skus):
    # Build our basket from the str first
    basket = Basket(skus)
    if basket.invalid:
        return -1
    
    return basket.calc_price()