
def discount(price, discount):
    
    if not (isinstance(price, (int, float)) and isinstance(discount, (int, float))):
        raise ValueError("price and discount must be numeric.")

    if price < 0 or discount < 0:
        raise ValueError("Price and discount should not be negative.")

    final_price = price - (price * (discount / 100))
    return final_price
