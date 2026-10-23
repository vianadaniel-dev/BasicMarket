def calculate_payment(water_qty: int, fruit_qty: int) -> dict:
    """Calculate the subtotal, discount, and total payment."""
    # Unit prices and business constraints
    WATER_PRICE = 2500
    FRUIT_PRICE = 1800
    DISCOUNT_THRESHOLD = 10000
    DISCOUNT_AMOUNT = 1000

    # Calculate item subtotals
    water_subtotal = water_qty * WATER_PRICE
    fruit_subtotal = fruit_qty * FRUIT_PRICE
    subtotal = water_subtotal + fruit_subtotal

    # Apply conditional promotion rule
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


def print_receipt(data: dict, order_title: str) -> None:
    """Print a clean, easy-to-read ticket breakdown in the terminal."""
    line_width = 38

    print("\n" + "=" * line_width)
    print(f" {order_title.upper()}")
    print("=" * line_width)

    # Line items
    print(f" Water  (x{data['water_qty']}){' ' * 16} ${data['water_subtotal']:>7,}")
    print(f" Fruit  (x{data['fruit_qty']}){' ' * 16} ${data['fruit_subtotal']:>7,}")

    print("-" * line_width)

    # Calculation breakdown
    print(f" Subtotal:{' ' * 17} ${data['subtotal']:>7,}")

    if data["discount"] > 0:
        print(f" Discount (>= $10,000):    -${data['discount']:>7,}")
    else:
        print(f" Discount:{' ' * 17}  ${data['discount']:>7,}")

    print("=" * line_width)
    print(f" TOTAL TO PAY:{' ' * 12} ${data['total']:>7,}")
    print("=" * line_width)


if __name__ == "__main__":
    # Test Case 1: Original problem (3 waters, 2 fruits)
    order_1 = calculate_payment(water_qty=3, fruit_qty=2)
    print_receipt(order_1, "Case 1: Standard Order")

    # Test Case 2: Under discount threshold (2 waters, 1 fruit)
    order_2 = calculate_payment(water_qty=2, fruit_qty=1)
    print_receipt(order_2, "Case 2: Low-value Order")
    