# Local Data Ingestion Design

## Overview

Before data is ingested into Azure, synthetic retail datasets are generated and loaded into a normalized MySQL 8 operational database. This database serves as the source system for Azure Data Factory.

The ingestion process provides a repeatable and configurable mechanism for loading synthetic retail datasets into the MySQL operational database.

---

## Objectives

- Load synthetic CSV datasets into MySQL.
- Preserve table relationships using a predefined loading sequence.
- Clear existing data before each load to support repeatable execution.
- Improve insertion performance using batch processing.
- Perform row-level data validation before insertion.
- Prepare the source database for Azure Data Factory ingestion.

---

## Source Datasets

The following CSV files are loaded into the source database:

- warehouse.csv
- customer.csv
- product.csv
- inventory.csv
- orders.csv
- order_items.csv
- payments.csv

---

## Loading Sequence

To maintain referential integrity, tables are loaded in the following order:

1. Warehouse
2. Customer
3. Product
4. Inventory
5. Orders
6. Order Items
7. Payments

---

## Ingestion Workflow

```text
Synthetic Data
      │
      ▼
CSV Files
      │
      ▼
Python Loader
      │
      ▼
Row-Level Validation
      │
      ▼
Batch Data Loading
      │
      ▼
MySQL 8 Operational Database
```

---

## Features

- Database configuration using `.env`
- Dynamic SQL generation from CSV headers
- Batch insertion using `executemany()`
- Transaction management using commit and rollback
- Foreign key checks disabled during table truncation
- Row-level data validation
- Modular validation functions

---

## Technologies Used

- Python
- MySQL Connector/Python
- CSV Module
- pathlib
- python-dotenv
- MySQL 8 Community Edition

---

## Azure Integration

The populated MySQL operational database serves as the source system for Azure Data Factory. In the next phase of the project, Azure Data Factory will ingest the source data into the Bronze layer of Azure Data Lake Storage Gen2.