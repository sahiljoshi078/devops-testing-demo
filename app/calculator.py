def apply_discount(amount: float, discount_percent: float) -> float:
    """
    Rules:
    - amount must be > 0
    - discount_percent must be between 0 and 80 inclusive
    - return rounded to 2 decimals
    """
    if amount <= 0:
        raise ValueError("amount must be > 0")
    if discount_percent < 0 or discount_percent > 80:
        raise ValueError("discount_percent must be between 0 and 80")

    discounted = amount * (1 - discount_percent / 100)
    return round(discounted, 2)
