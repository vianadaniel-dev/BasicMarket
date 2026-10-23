def get_positive_int(prompt_text):
    """Prompt the user until a valid non-negative integer is entered."""
    while True:
        try:
            value = int(input(prompt_text))
            if value >= 0:
                return value
            print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


def calculate_payment(water_qty, fruit_qty):
    """Calculate the subtotal, discount, and grand total."""
    # 1. Constants
    WATER_PRICE = 2500
    FRUIT_PRICE = 1800
    DISCOUNT_THRESHOLD = 10000
    DISCOUNT_AMOUNT = 1000

    # 2. Subtotals
    water_subtotal = water_qty * WATER_PRICE
    fruit_subtotal = fruit_qty * FRUIT_PRICE
    subtotal = water_subtotal + fruit_subtotal

    # 3. Discount condition
    if subtotal >= DISCOUNT_THRESHOLD:
        discount = DISCOUNT_AMOUNT
    else:
        discount = 0

    total = subtotal - discount

    return {
        "water_qty": water_qty,
        "water_subtotal": water_subtotal,
        "fruit_qty": fruit_qty,
        "fruit_subtotal": fruit_subtotal,
        "subtotal": subtotal,
        "discount": discount,
        "total": total,
    }


def print_receipt(data):
    """Display the clean receipt breakdown."""
    line_width = 38

    print("\n" + "=" * line_width)
    print(" ORDER SUMMARY")
    print("=" * line_width)
    print(f" Water  (x{data['water_qty']}){' ' * 16} ${data['water_subtotal']:>7,}")
    print(f" Fruit  (x{data['fruit_qty']}){' ' * 16} ${data['fruit_subtotal']:>7,}")
    print("-" * line_width)
    print(f" Subtotal:{' ' * 17} ${data['subtotal']:>7,}")

    if data["discount"] > 0:
        print(f" Discount (>= $10,000):    -${data['discount']:>7,}")
    else:
        print(f" Discount:{' ' * 17}  ${data['discount']:>7,}")

    print("=" * line_width)
    print(f" TOTAL TO PAY:{' ' * 12} ${data['total']:>7,}")
    print("=" * line_width)


if __name__ == "__main__":
    print("=== Welcome to the Store ===")

    # User inputs
    waters = get_positive_int("Enter number of water bottles: ")
    fruits = get_positive_int("Enter number of fruits: ")

    # Process and output
    result = calculate_payment(waters, fruits)
    print_receipt(result)