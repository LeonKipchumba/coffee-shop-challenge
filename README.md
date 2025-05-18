# ☕ Coffee Shop Challenge

A Python object-oriented programming project that models the relationships between `Customer`, `Coffee`, and `Order` classes in a simulated coffee shop environment. This mock challenge is part of Phase 3 coursework and is designed to demonstrate class design, data validation, object relationships, and basic data aggregation techniques.

---

## 📚 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Running Tests](#-running-tests)
- [Usage](#-usage)
- [Bonus](#-bonus)
- [License](#-license)

---

## ✅ Features

- `Customer` class with name validation (1–15 characters).
- `Coffee` class with immutable names and validation (minimum 3 characters).
- `Order` class linking `Customer` and `Coffee` with valid prices (1.0–10.0).
- Object relationships:
  - `Customer.orders()`, `Customer.coffees()`
  - `Coffee.orders()`, `Coffee.customers()`
- Aggregated methods:
  - `Customer.create_order()`
  - `Coffee.num_orders()`, `Coffee.average_price()`
- Bonus method: `Customer.most_aficionado(coffee)` returns the biggest spender on a given coffee.

---

## 📁 Project Structure

