# Active Pause Purchase Calculator

Simple Python program to calculate the total cost of a purchase with a conditional discount.

---

## 1. Inputs, Process, and Output

* **Inputs:**
  * Water bottle: $2,500 each.
  * Fruit: $1,800 each.
  * Discount: $1,000 off if subtotal is $10,000 or more.
* **Process:**
  * `subtotal = (water_qty * 2500) + (fruit_qty * 1800)`
  * `discount = 1000` if `subtotal >= 10000`, else `0`
  * `total = subtotal - discount`
* **Output:** Total amount to pay.

---

## 2. Execution Steps

1. Set the quantities for water and fruit.
2. Define unit prices and discount rules.
3. Compute item subtotals.
4. Sum both values to get the overall subtotal.
5. Check if the subtotal is >= $10,000 to apply the $1,000 discount.
6. Subtract the discount from the subtotal.
7. Print the final total.

---

## 3. Variables Used

* `WATER_PRICE`: $2,500
* `FRUIT_PRICE`: $1,800
* `DISCOUNT_THRESHOLD`: $10,000
* `DISCOUNT_AMOUNT`: $1,000
* `water_qty`: Number of water bottles
* `fruit_qty`: Number of fruits
* `subtotal`: Cost before discount
* `discount`: Applied discount ($0 or $1,000)
* `total`: Final amount to pay

---

## 4. Test Case 1 (Problem Statement)

* **Cart:** 3 waters, 2 fruits
* **Subtotal:** (3 × 2,500) + (2 × 1,800) = 7,500 + 3,600 = $11,100
* **Discount:** $1,000 (since $11,100 >= $10,000)
* **Total:** $10,100

---

## 5. Test Case 2 (Alternative Test)

* **Cart:** 2 waters, 1 fruit
* **Subtotal:** (2 × 2,500) + (1 × 1,800) = 5,000 + 1,800 = $6,800
* **Discount:** $0 (since $6,800 < $10,000)
* **Total:** $6,800

---

## 6. Question on Ambiguity

> *"Is the $1,000 discount applied only once per purchase, or does it multiply for every $10,000 spent (e.g., $2,000 off for a $20,000 subtotal)?"*

---

## How to Run

```bash
python market.py