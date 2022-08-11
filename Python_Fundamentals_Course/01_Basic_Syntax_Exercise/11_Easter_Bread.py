# •	On the 1st line you will receive the budget – a real number in the range [0.0…100000.0]
# •	On the 2nd line you will receive the price for 1 kg flour – a real number in the range [0.0…100000.0]
# •	The input will always be in the right format.
# •	You will always have a remaining budget.
# •	There will not be a case in which the eggs become a negative count.

budget = float(input())
price_1kg_flour = float(input())
price_1pack_eggs = 0.75 * price_1kg_flour
price_1l_milk = 1.25 * price_1kg_flour
cozonac_price = price_1kg_flour + price_1pack_eggs + price_1l_milk / 4
cozonacs_count = 0
colored_eggs = 0
# Start cooking the cozonacs (Easter bread) and keep making them until you have enough budget. Keep in mind that:
# •	For every cozonac that you make, you will receive 3 colored eggs.
# •	For every 3rd cozonac that you make, you will lose some of your colored eggs after you have received
# the usual 3 colored eggs for your cozonac. The count of eggs you will lose is calculated
# when you subtract 2 from your current count of cozonacs – ({currentCozonacsCount} – 2)

while budget > 0:
    budget -= cozonac_price
    cozonacs_count += 1
    colored_eggs += 3
    if cozonacs_count % 3 == 0 and budget >= 0:
        colored_eggs -= cozonacs_count - 2

if budget < 0:
    budget += cozonac_price
    cozonacs_count -= 1
    colored_eggs -= 3

print(f"You made {cozonacs_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget :.2f}BGN left.")
