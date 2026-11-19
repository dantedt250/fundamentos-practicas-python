def calculate_total_price(price, tax_rate):
    """ Calculate the final price including tax. """
    total = price + (price * tax_rate)
    return total


if __name__ == "__main__":
    print ("=== HEALTHY PRODUCTION SYSTEM V1.0 ===")
    item_price =  100.0
    tax = 0.16
    final_amount = calculate_total_price(item_price, tax)
    print(f"the total price including tax is: {final_amount}")