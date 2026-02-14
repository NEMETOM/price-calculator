def apply_discount(price: float, discount_percent: float) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    
    return price * (1 - discount_percent / 100)

def add_vat(price: float, var_percent: float) -> float:
    if var_percent < 0:
        raise ValueError("VAT cannot be negative")
    
    return price * (1 + var_percent / 100)