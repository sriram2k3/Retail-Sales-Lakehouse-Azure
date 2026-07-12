# Source System Schema v1.0

## Database

MySQL 8 Community Edition

## Purpose

Operational database for the Retail Sales Pipeline project.

## Business Domain

Retail / E-Commerce

## Tables

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

## Relationships

Customer (1) ------ (M) Orders

Orders (1) ------ (M) Order Items

Product (1) ------ (M) Order Items

Warehouse (1) ------ (M) Inventory

Product (1) ------ (M) Inventory

Orders (1) ------ (1) Payments

## Notes

This schema serves as the OLTP source system for Azure Data Factory ingestion into Azure Data Lake Storage Gen2.