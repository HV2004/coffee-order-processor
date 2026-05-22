#Coffee Order Processsing System

## Overview

This project processes coffee orders from JSON input, generates CSV reports, analytics summaries, and supports real-time currency conversion using ExchangeRate API .
## Features

-JSON input processing 
-CSV rerport generation
-Order validation
-Analytics generation
-Convert USD prices into other currencies.
-Secure API key handling 
-LOgging support
-Centralized data handling

## Project Structure

```text
Coffee_Order/
│
├── API
│   ├── exchange_rate_api.py
├── CsvReport
│   ├── reader.py
│   └── writer.py
├── Data
│   ├── data_exchange.py
├── main.py
├── Models
│   ├── order.py
├── orders.json
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── report.csv
├── summary.json
├── Tasks
│   ├── analytics.py
│   ├── processor.py
│   ├── service.py
│   └── validator.py
├── Tests
│   ├── test_data_exchange.py
│   ├── test_exchange_api.py
│   ├── test_analytics.py
│   ├── test_order.py
│   ├── test_processor.py
│   ├── test_reader.py
│   ├── test_service.py
│   ├── test_validator.py
│   └── test_writer.py
└── test_summary
````
---

# How To Run The Project

## Generate CSV Report

```bash
python3 main.py --input order.json --output report.csv
```

---

## Generate CSV + Analytics Summary

```csv
python3 main.py --input order.json --output report.csv --summary sumary.json
```

## Get ExchangeRate API Key

1. Visit: [ExchangeRate API](https://app.exchangerate-api.com/sign-up)
2. Create free account.
3. Copy API key.

## Currency Conversion

```bash
pytho```json
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
```n3 main.py --input order.json --output report.csv --currency EUR
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
# Example Currency Conversion Output

```json
[
    {
        "order_id":"ORD-001",
        "drink":"latte",
        "size":"large",
        "price":5.50,
        "converted_total":5.06,
        "currency":"EUR",
        "timestamp":"2026-05-07 09:15",
        "extras":["extra_shot","oat_milk"]
    }
]
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