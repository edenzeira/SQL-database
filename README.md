# 🛒 SPL Assignment 4 – BGU Mart Supermarket Management System

This Python + SQLite3 project simulates a full management system for a supermarket chain.  
It was developed as part of the **SPL course** at Ben-Gurion University.

---

## 🧭 Overview

BGU Mart is a lightweight database-backed system to manage:
- Employees and branches
- Suppliers and product inventory
- Sales and delivery activities

The system includes:
- 🗂 `bgumart.db` – SQLite database
- 🛠️ `initiate.py` – builds the database and loads initial configuration
- 📦 `action.py` – handles buying/selling product activities
- 🧾 `printdb.py` – prints detailed reports from the database

---

## 🧱 Database Structure

The database contains 5 tables:
- `employees(id, name, salary, branche)`
- `branches(id, location, number_of_employees)`
- `suppliers(id, name, contact_information)`
- `products(id, description, price, quantity)`
- `activities(product_id, quantity, activator_id, date)`

---

## ⚙️ Modules

### `initiate.py`
- Run:  
```bash
python3 initiate.py config.txt
```
- Creates a fresh `bgumart.db` and populates tables using a config file with lines starting with:
  - `B` = branch
  - `E` = employee
  - `P` = product
  - `S` = supplier

### `action.py`
- Run:  
```bash
python3 action.py actions.txt
```
- Performs supply/sale actions from file:
  - Quantity > 0: delivery from supplier  
  - Quantity < 0: sale by employee (only if quantity is available)

### `printdb.py`
- Run:
```bash
python3 printdb.py
```
- Prints all tables in the following order: `Activities`, `Branches`, `Employees`, `Products`, `Suppliers`
- Also prints:
  - **Employee report**: name, salary, branch location, total sales income
  - **Activity report**: date, product, quantity, seller name / supplier name (as applicable)

---

## 📄 File Format Examples

### Configuration file (`config.txt`)
```
B,3,Chicago,40  
E,106,Sue Davis,75000,3  
P,5,Mango,2,7  
S,6,Jkl Enterprises,(678) 901-2345
```

### Action file (`actions.txt`)
```
3, 500, 56, 20230110      # delivery: supplier 56 delivers 500 units of product 3  
100, -500, 1234, 20230110  # sale: employee 1234 sells 500 units of product 100
```

---

## ✅ Status

✔️ Fully functional SQLite3-based DB  
✔️ Command-line runnable modules  
✔️ Data validation and error handling  
✔️ Complex JOIN queries and ordering for reports  
✔️ Designed for UNIX terminal execution  

---
