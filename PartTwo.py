amount = 75
coins = [50, 20, 10, 5] 
total = 0

while total < amount:
    coin = int(input("Insert coin (50p, 20p, 10p, 5p): "))
    
    if coin in coins:
        total += coin
        if total < amount:
            print(f"Amount due: {amount - total}p")
    else:
        print("Please insert a 50p, 20p, 10p or 5p coin.")

change = total - amount

if change > 0:
    print(f"Change = {change}p.")
