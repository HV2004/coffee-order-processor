#Coffee Order Processsing System

## Overview

This project processes coffee orders from JSON input and generates CSV reports and analytics summaries.

## Features

-JSON input processing 
-CSV rerport generation
-Order validation
-Analytics generation

## Project Structure

```text
Coffee_Order/
├── CsvReport
│   ├── reader.py
│   └── writer.py
├── main.py
├── Models
│   ├── order.py
├── orders.json
├── README.md
├── report.csv
├── summary.json
├── Tasks
│   ├── analytics.py
│   ├── processor.py
│   ├── service.py
│   └── validator.py
├── Tests
│   ├── test_analytics.py
│   ├── test_order.py
│   ├── test_processor.py
│   ├── test_reader.py
│   ├── test_service.py
│   ├── test_validator.py
│   └── test_writer.py
└── test_summary
```
---

# How To Run The Project

## Generate CSV Report

```bash
python3 main.py --input order.json --output report.csv
```

---

## Generate CSV + Analytics Summary

```bash
python3 main.py --input order.json --output report.csv --summary sumary.json
```

# How To Run Unit Tests

Run all Tests:

```bash
python3 -m pytest -v
```

---

# Example input JSON

```json
[
    {
        "order_id":"ORD-001",
        "drink":"latte",
        "size":"large",
        "price":5.50,
        "timestamp":"2026-05-07 09:15",
        "extras":["extra_shot","oat_milk"]
    }
]
```

---

# Example of CSV Output

```csv
order_id,drink,size,price,timestamp,extras_count
ORD-001,latte,large,5.50,2026-05-07 09:15,2
```

---

# Example Analytics Output

```json
{
    "total_orders":1,
    "total_revenue":5.5,
    "average_order_value":5.5,
    "orders_by_drink":{
        "latte":1
    },
    "orders_by_size":{
        "large":1
    }
}
```

---

# Validation Rules

## Valid Drinks

- espresso
- latte
- cappuccino
- americano

## Valid Sizes

- small
- medium
- large

Orders are rejected if:
- drink is invalid
- size is invalid
- price is less than or equal to 0
