"""
Now coin price is 100 taka.
30 minus ago its down to 80 taka and 10 minutes ago its highest price was 120 taka.
How much percentage the price goes and down?
"""

current_price = int(input("What is current price ? :"))
# TODO : Use input for high_price and low_price
high_price = 110
low_price = 90


price_increase = high_price-current_price
high_percentage = (price_increase*100)/current_price
print(f"Height percentage: {high_percentage} %")


lost_price = low_price-current_price
lost_percentage = (lost_price*100)/current_price
print(f"Lost percentage: {lost_percentage} %")
