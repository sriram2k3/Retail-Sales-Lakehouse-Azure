# Retail Sales Lakehouse Pipeline using Microsoft Azure

## 📌 Project Overview

Retail Sales Lakehouse Pipeline is an end-to-end Azure Data Engineering project that demonstrates how operational retail data is ingested, transformed, and analyzed using Microsoft Azure cloud services.

The project follows enterprise data engineering practices by implementing a modern Lakehouse architecture using Azure Data Lake Storage Gen2, Azure Data Factory, Azure Databricks, Delta Lake, Azure Synapse Analytics, and Power BI.

The objective is to build a scalable, production-inspired analytics platform capable of ingesting retail sales data, transforming it through Bronze, Silver, and Gold layers, and serving business insights through interactive dashboards.

---

# 🏢 Business Scenario

A retail organization receives daily operational data from multiple warehouses and stores.

Current challenges include:

- Manual Excel reporting
- Inconsistent business metrics
- Lack of centralized analytics
- Poor visibility into customer behavior
- Inventory planning challenges
- Time-consuming report generation

This project modernizes the analytics platform using Microsoft Azure.

---

# 🎯 Project Objectives

- Build an enterprise-scale Azure Lakehouse architecture.
- Implement Bronze, Silver and Gold data layers.
- Design an end-to-end ETL pipeline using Azure Data Factory.
- Perform data transformation using PySpark in Azure Databricks.
- Store curated datasets in Delta Lake format.
- Enable analytical querying through Azure Synapse.
- Build reusable semantic models.
- Develop executive dashboards using Power BI.

---

# 🏗️ Current Progress

## ✅ Phase 1 - Foundation & Infrastructure

Completed

- Azure Resource Group
- Azure Storage Account (ADLS Gen2 Enabled)
- Bronze, Silver and Gold Containers
- Archive, Logs and Rejected Containers
- Enterprise Folder Structure
- GitHub Repository Initialization
- Business Requirement Analysis
- Source System Design
- OLTP Schema v1.0 Finalized

## ✅ Phase 2 - Enterprise Data Generation

Completed

- Business Requirement Analysis
- Source System Design
- OLTP Schema v1.0 Finalized
- Enterprise Business Rules Defined
- Synthetic Retail Dataset Generated
- Python Batch CSV Loader Developed
- Dynamic SQL Ingestion into MySQL
- Batch Processing using `executemany()`
- Basic Data Validation Framework
- Environment Variable Configuration using `.env`

---

# 🏢 Source System

The source system for this project is a normalized MySQL 8 operational database representing a retail organization.

### Master Tables

- Customer
- Product
- Warehouse

### Operational Tables

- Inventory

### Transaction Tables

- Orders
- Order Items
- Payments

This database acts as the source system for Azure Data Factory ingestion.

---

# ☁️ Azure Resources

| Resource | Status |
|----------|--------|
| Resource Group | ✅ Created |
| Storage Account | ✅ Created |
| ADLS Gen2 | ✅ Enabled |
| Bronze Container | ✅ Created |
| Silver Container | ✅ Created |
| Gold Container | ✅ Created |
| Archive Container | ✅ Created |
| Logs Container | ✅ Created |
| Rejected Container | ✅ Created |

---

# 🗂️ Data Lake Storage Structure

## Bronze Layer (Raw Data)

```text
bronze/
│
└── retail/
    │
    ├── customers/
    │   └── 2026/
    │       └── 07/
    │           └── 11/
    │               └── customers_20260711.csv
    │
    ├── orders/
    │   └── 2026/
    │       └── 07/
    │           └── 11/
    │               └── orders_20260711.csv
    │
    ├── products/
    │   └── master/
    │       └── products.csv
    │
    ├── warehouses/
    │   └── master/
    │       └── warehouses.csv
    │
    ├── inventory/
    │   └── 2026/
    │       └── 07/
    │           └── 11/
    │               └── inventory_20260711.csv
    │
    ├── order_items/
    │   └── 2026/
    │       └── 07/
    │           └── 11/
    │               └── order_items_20260711.csv
    │
    └── payments/
        └── 2026/
            └── 07/
                └── 11/
                    └── payments_20260711.csv
```

---

## Silver Layer (Clean & Standardized Data)

```text
silver/
│
└── retail/
    ├── customers/
    ├── products/
    ├── warehouses/
    ├── inventory/
    ├── orders/
    ├── order_items/
    └── payments/
```

---

## Gold Layer (Business Ready Data)

```text
gold/
│
└── retail/
    ├── sales_summary/
    ├── customer_summary/
    ├── product_summary/
    ├── inventory_summary/
    ├── regional_summary/
    └── executive_dashboard/
```

---

# 🏛️ High-Level Architecture

```text
MySQL (OLTP)
        │
        ▼
Azure Data Factory
        │
        ▼
Azure Data Lake Storage Gen2
        │
        ▼
Bronze Layer
        │
        ▼
Azure Databricks (PySpark)
        │
        ▼
Silver Layer
        │
        ▼
Gold Layer (Delta)
        │
        ▼
Azure Synapse Analytics
        │
        ▼
Semantic Model
        │
        ▼
Power BI
```

---

# 🚀 Technology Stack

- Microsoft Azure
- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks
- Delta Lake
- Azure Synapse Analytics
- Power BI
- MySQL
- Python
- mysql-connector-python
- python-dotenv
- CSV Processing
- PySpark
- SQL
- Git & GitHub

---

# 📅 Project Roadmap

| Phase | Status |
|--------|--|
| Phase 1 – Foundation & Infrastructure | ✅ Completed |
| Phase 2 – Enterprise Data Generation | ✅ Completed |
| Phase 3 – Azure Data Factory Ingestion | ⏳ Planned |
| Phase 4 – Bronze → Silver Transformation | ⏳ Planned |
| Phase 5 – Gold Layer Analytics | ⏳ Planned |
| Phase 6 – Synapse Analytics | ⏳ Planned |
| Phase 7 – Semantic Model | ⏳ Planned |
| Phase 8 – Power BI Dashboard | ⏳ Planned |
| Phase 9 – Production Readiness | ⏳ Planned |

---

# 📸 Screenshots

Project screenshots are available under the **screenshots/** directory.

---

# 📖 Documentation

Detailed documentation is available under the **docs/** directory.

Current documentation includes:

- Source Schema v1.0

Additional documentation will be added as each phase is completed.

---

# 👨‍💻 Author

**Sri Ram B**

Azure Data Engineering Portfolio Project