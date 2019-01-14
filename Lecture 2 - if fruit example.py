total_cash = 15
price_orange = 1.00
qty_orange = 0
price_apple = 1.50
qty_apple = 0
price_mango = 4.00
qty_mango = 0

if price_orange <= total_cash:
    qty_orange = 1
    total_cash = total_cash - price_orange
    
    if price_apple <= total_cash:
        qty_apple = 1
        total_cash = total_cash - price_apple

        if price_mango <= total_cash:
            qty_mango = 1
            total_cash = total_cash - price_mango
    

if price_mango <= total_cash:
    qty_mango = qty_mango + 1
    total_cash = total_cash - price_mango
    
if price_apple <= total_cash:
    qty_apple = qty_apple + 1
    total_cash = total_cash - price_apple

if price_orange <= total_cash:
    qty_orange = qty_orange + 1
    total_cash = total_cash - price_orange

print ("Total oranges bought: %d\nTotal apples bought: %d\nTotal mango bought: %d\n" % (qty_orange, qty_apple, qty_mango))
print ("Remaining money: RM%.2f" % (total_cash))
