from datetime import datetime


def validate_customer(row):
    age = int(row["age"])

    if not (18 <= age <= 65):
        return False, "Age must be between 18 and 65"

    if not row["email"].strip():
        return False, "Email must be provided"

    if row["loyalty_tier"] not in ["Bronze", "Silver", "Gold"]:
        return False, "Tier must be Bronze, Silver or Gold"

    return True, "Valid row"


def validate_product(row):
    cost_price = float(row["cost_price"])
    unit_price = float(row["unit_price"])
    mrp = float(row["mrp"])

    if not (cost_price < unit_price < mrp):
        return False, "Pricing should follow Cost < Unit Price < MRP"

    return True, "Valid row"


def validate_warehouse(row):

    if not row["city"].strip():
        return False, "City cannot be empty"

    if not row["state"].strip():
        return False, "State cannot be empty"

    return True, "Valid row"


def validate_inventory(row):

    stock = int(row["stock_qty"])
    reorder = int(row["reorder_level"])

    if stock < 0:
        return False, "Stock cannot be negative"

    if reorder < 0:
        return False, "Reorder level cannot be negative"

    return True, "Valid row"


def validate_orders(row):

    order_date = datetime.strptime(row["order_date"], "%Y-%m-%d %H:%M:%S")
    delivery_date = datetime.strptime(row["delivery_date"], "%Y-%m-%d")

    if delivery_date.date() < order_date.date():
        return False, "Delivery date cannot be before order date"

    if row["order_status"] not in [
        "Pending",
        "Confirmed",
        "Shipped",
        "Out for Delivery",
        "Delivered",
        "Cancelled",
        "Returned"
    ]:
        return False, "Invalid order status"

    return True, "Valid row"


def validate_order_items(row):

    quantity = int(row["qty"])
    unit_price = float(row["unit_price"])
    discount = float(row["discount"])

    if quantity <= 0:
        return False, "Quantity must be greater than zero"

    if unit_price <= 0:
        return False, "Unit price must be greater than zero"

    if not (0 <= discount <= 20):
        return False, "Discount should be between 0 and 20"

    return True, "Valid row"


def validate_payments(row):

    if row["payment_status"] not in [
        "Paid",
        "Pending",
        "Failed",
        "Refunded"
    ]:
        return False, "Invalid payment status"

    return True, "Valid row"

validators = {
    "warehouse": validate_warehouse,
    "customer": validate_customer,
    "product": validate_product,
    "orders": validate_orders,
    "order_items": validate_order_items,
    "inventory": validate_inventory,
    "payments": validate_payments,
}
def validate_row(table_name, row):
    is_valid, msg = validators[table_name](row)
    return is_valid, msg

if __name__ == "__main__":
    print("Validation function script for ingestion tables")