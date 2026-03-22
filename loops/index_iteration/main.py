prices = [29.99, 45.50, 12.75, 38.20]

for price in range(len(prices)):
    if price == 0:
        discounted = prices[price] * 0.9
        prices[price] = discounted
        print(f"Updated price for item {price}: ${prices[price]:.2f}")
    elif price == 1:
        discounted = prices[price] * 0.8
        prices[price] = discounted
        print(f"Updated price for item {price}: ${prices[price]:.2f}")
    elif price == 2:
        discounted = prices[price] * 0.85
        prices[price] = discounted
        print(f"Updated price for item {price}: ${prices[price]:.2f}")
    elif price == 3:
        discounted = prices[price] * 0.95
        prices[price] = discounted
        print(f"Updated price for item {price}: ${prices[price]:.2f}")
        
        
        