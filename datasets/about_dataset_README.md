# Retail Sales Lakehouse - Synthetic Dataset

This folder contains the synthetic source data used for the **Retail Sales Lakehouse** Azure Data Engineering project. The dataset simulates an Indian retail company's OLTP system and serves as the source for Azure Data Factory ingestion into the Bronze layer.

## Dataset Information

- **Project:** Retail Sales Lakehouse
- **Data Type:** Synthetic Retail Transaction Data
- **Time Period:** January 1, 2026 – July 11, 2026
- **Source Database:** MySQL
- **Target Platform:** Azure Data Lake Storage Gen2

---

## Dataset Summary

| File | Description | Record Count |
|------|-------------|-------------:|
| `warehouse.csv` | Warehouse master data | **5** |
| `customer.csv` | Customer master data | **1,000** |
| `product.csv` | Product master data | **200** |
| `inventory.csv` | Inventory records across warehouses | **1,000** |
| `orders.csv` | Customer orders | **5,000** |
| `order_items.csv` | Products purchased in each order | **9,970*** |
| `payments.csv` | Payment transactions | **5,000** |

### Total Records

**22,175 Records**

> **Note:** Each order contains **1–3 products**, resulting in multiple records in `order_items.csv`.

---

## Business Rules Implemented

- Customer registrations span **January 2026 to July 2026**.
- Orders increase progressively month by month.
- Five warehouses serve all products.
- Every warehouse stocks every product.
- Loyalty tier distribution:
  - Bronze – 65%
  - Silver – 25%
  - Gold – 10%
- Payment preference gradually shifts from **Cash** to **UPI**.
- Product pricing follows:
  - **Cost Price < Unit Price < MRP**
- Warehouse IDs are business codes (`WH001`–`WH005`).
- All primary keys except `warehouse_id` are generated using **AUTO_INCREMENT**.

---

## Database Import Order

Load the CSV files in the following sequence:

1. `warehouse.csv`
2. `customer.csv`
3. `product.csv`
4. `inventory.csv`
5. `orders.csv`
6. `order_items.csv`
7. `payments.csv`

---

## Database Preparation

Before importing the dataset:

1. Execute `reset_database.sql`.
2. This will:
   - Clear existing records.
   - Reset `AUTO_INCREMENT` values.
   - Preserve foreign key relationships.

---

## Project Architecture

```text
CSV Files
    │
    ▼
MySQL OLTP Database
    │
    ▼
Azure Data Factory
    │
    ▼
Azure Data Lake Storage Gen2 (Bronze)
    │
    ▼
Azure Databricks (Silver)
    │
    ▼
Gold Layer
    │
    ▼
Power BI
```

---

## Author

**Sri Ram B**

Azure Data Engineering Portfolio Project