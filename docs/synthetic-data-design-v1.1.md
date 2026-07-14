# Retail-Sales-Lakehouse-Pipeline Project

# Synthetic Data Design - Business Rules (Version 1.1)

## Customer Table
- Data timeline: January 1, 2026 to July 11, 2026.
- Customers belong only to India.
- Phone numbers should not include country code (+91).
- Customer registration date should fall between January 2026 and July 2026.
- Customer ages: 18–65.
- Email and mobile number should be unique.
- Customers should belong only to supported warehouse cities.
- Customer registrations should gradually increase month by month.

### Loyalty Tier Distribution
- Bronze – 65%
- Silver – 25%
- Gold – 10%

---

## Product Table
- Categories:
  - Electronics
  - Home Appliances
  - Fashion
  - Books
  - Groceries
  - Cosmetics
- Pricing rule:
  - MRP > Unit Price > Cost Price
- Currency: INR.
- Brand and manufacturer can be domestic or international.
- Products should contain Budget, Mid-range and Premium pricing segments.

---

## Warehouse Table
- Warehouses should be located only within India.
- Five warehouses:
  - Chennai
  - Bengaluru
  - Hyderabad
  - Pune
  - Mumbai
- Each warehouse belongs to one city and one state.
- Every warehouse stocks every product.
- Initial stock: 100–500 units.
- Reorder level: 25 units.

---

## Orders Table
- Orders generated between January 2026 and July 11, 2026.
- Orders begin from January 3, 2026.
- Monthly order volume should gradually increase.
- Order Status:
  - Pending
  - Confirmed
  - Shipped
  - Out for Delivery
  - Delivered
  - Cancelled
  - Returned

### Business Behaviour
- Customer satisfaction improves over time.
- Early months have relatively higher Pending and Returned orders.
- Delivered orders gradually increase.
- Approximate distribution:
  - Delivered – 90%
  - Cancelled – 3%
  - Returned – 2%
  - Remaining split among Pending, Confirmed, Shipped and Out for Delivery.
- Returned orders should only originate from Delivered orders.

### Shipping Rules
- Standard: Delivery in 3–5 days.
- Express: Delivery in 1–2 days.
- Same Day: Delivered on the order date.
- Pickup: Delivery date equals order date.

---

## Order Items Table
- Each order contains 1–5 products.
- Quantity:
  - Jan–Mar: Mostly 1–2 units.
  - Apr–Jul: Mostly 2–4 units.
- Line Total in INR.
- Discount Rules:
  - Bronze: 0–5%
  - Silver: 5–10%
  - Gold: 10–20%
- Additional clearance discounts may be applied for high-stock products.
- Maximum discount should never exceed 20%.

---

## Inventory Table
- Inventory decreases as orders are generated.
- Stock should never become negative.
- Products below reorder level should be flagged for replenishment.

---

## Payments Table

### Payment Status
- Paid – 95%
- Pending – 3%
- Failed – 1%
- Refunded – 1%

### Payment Methods
- UPI
- Card
- Cash

### Business Behaviour
- January: Cash transactions dominate.
- By July: UPI becomes the preferred payment method.
- Payment date should be on or after the order date.

---

# Business Story

The synthetic dataset should demonstrate:

- Business growth from January to July.
- Increasing customer registrations.
- Higher monthly order volume.
- Increasing digital payment adoption.
- Reduced cancellations and returns over time.
- Better customer satisfaction.
- Higher spending by Gold customers.
- Inventory movement and clearance discounts.
- Different purchasing patterns across cities.

This dataset will serve as the OLTP source system for the Azure Retail Sales Lakehouse Pipeline.
