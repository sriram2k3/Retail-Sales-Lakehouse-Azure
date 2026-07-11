# Retail Sales Lakehouse Pipeline using Microsoft Azure

## 📌 Project Overview

This project demonstrates an end-to-end Azure Data Engineering solution for a retail organization using Microsoft Azure cloud services.

The objective is to design a scalable Lakehouse architecture capable of ingesting daily retail sales data, transforming it through Bronze, Silver, and Gold layers, and serving analytics through Azure Synapse and Power BI.

---

## 🏗️ Current Progress

### ✅ Phase 1 - Infrastructure Setup

Completed

- Azure Resource Group
- Azure Storage Account (ADLS Gen2 Enabled)
- Bronze, Silver and Gold Containers
- Archive, Logs and Rejected Containers
- Enterprise Folder Structure
- GitHub Repository Initialization

---

## ☁️ Azure Resources

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
    ├── stores/
    │   └── master/
    │       └── stores.csv
    │
    └── inventory/
        └── 2026/
            └── 07/
                └── 11/
                    └── inventory_20260711.csv
```

---

## Silver Layer (Clean & Standardized Data)

```text
silver/
│
└── retail/
    │
    ├── customers/
    ├── orders/
    ├── products/
    ├── stores/
    └── inventory/
```

---

## Gold Layer (Business Ready Data)

```text
gold/
│
└── retail/
    │
    ├── sales_summary/
    ├── customer_summary/
    ├── product_summary/
    ├── regional_summary/
    └── executive_dashboard/
```

---

## Archive Layer

```text
archive/
│
└── YYYY/
    └── MM/
        └── DD/
```

---

## Rejected Layer

```text
rejected/
│
├── missing_customer/
├── duplicate_orders/
├── invalid_product/
└── invalid_records/
```

---

## Logs Layer

```text
logs/
│
├── adf/
├── databricks/
├── synapse/
└── pipeline/
```

---

# 🏛️ Lakehouse Architecture

```
Source CSV Files
        │
        ▼
Azure Data Lake Storage Gen2
        │
        ▼
Bronze Layer
(Raw Data)
        │
        ▼
Azure Data Factory
        │
        ▼
Azure Databricks
(PySpark)
        │
        ▼
Silver Layer
(Cleansed Data)
        │
        ▼
Gold Layer
(Business Ready Data)
        │
        ▼
Azure Synapse Analytics
        │
        ▼
Semantic Model
        │
        ▼
Power BI Dashboard
```

---

# 🎯 Project Objectives

- Build an enterprise-scale Azure Lakehouse architecture.
- Implement Bronze, Silver and Gold data layers.
- Develop automated ETL pipelines using Azure Data Factory.
- Perform transformations using PySpark in Azure Databricks.
- Store curated datasets in Delta Lake format.
- Enable analytical queries using Azure Synapse.
- Build reusable semantic models.
- Create executive dashboards in Power BI.

---

# 🚀 Technology Stack

- Microsoft Azure
- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks
- Delta Lake
- Azure Synapse Analytics
- Power BI
- Python
- PySpark
- SQL
- Git & GitHub

---

# 📅 Project Status

| Phase | Status |
|--------|--------|
| Phase 1 - Infrastructure | ✅ Completed |
| Phase 2 - Data Engineering | ⏳ Planned |
| Phase 3 - Analytics | ⏳ Planned |
| Phase 4 - Production Readiness | ⏳ Planned |

---

# 📸 Screenshots

Project screenshots are available in the **/screenshots** directory.

---

# 📖 Documentation

Detailed project documentation will be added under the **/docs** directory as each phase is completed.

---

## 👨‍💻 Author

**Sri Ram B**

Azure Data Engineering Portfolio Project