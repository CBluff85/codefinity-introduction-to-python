def apply_discount(price,discount=0.05):
    disprice = price*discount
    price = price - disprice
    return price
def apply_tax (price, tax=0.07):
    tax_price = price * tax
    price = price + tax_price
    return price
def calculate_total(price, discount =0.05, tax=0.07):
    discounted = apply_discount(price, discount)
    total = apply_tax(discounted, tax)
    return total
calculate_total(120)
calculate_total(100,discount=0.10, tax=0.08)
print("Total cost with default discount and tax: $", calculate_total(120))
print("Total cost with custom discount and tax: $", calculate_total(100,discount=0.10, tax=0.08))
    