# Bean & Brew Coffee Shop Management System
**ISM4113 – Systems Design Midterm Project**

A small Flask + SQLite application for managing a coffee shop's products, customers, orders, and sales reports. The project is designed to demonstrate systems analysis and design decisions, not to depend on a particular framework.

## Features
- Dashboard with total recorded sales, completed order count, active product count, and recent orders.
- Product catalogue with input validation and unique product names.
- Customer directory with optional email and phone; duplicate emails are prevented by the database.
- Order entry with optional customer, multiple items, quantity validation, and stored sale-time unit prices.
- Order receipt with calculated line totals and order total.
- Sales report by day and top-selling products.
- SQLite relational data model, primary/foreign keys, constraints, and indexes.
- Responsive interface with sample menu products seeded automatically.

## Requirements
- Python 3.10 or newer
- pip

## Run locally
1. Extract the project ZIP and open a terminal in the project folder.
2. Create a virtual environment:
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows: `py -m venv .venv` then `.venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Start the app: `python run.py`
5. Open `http://127.0.0.1:5000` in your browser.

The database is created automatically at `instance/coffee_shop.sqlite`. Six sample products are inserted on first run. Customer and order data are stored locally.

## Main routes
| Route | Purpose |
|---|---|
| `/` | Dashboard and recent orders |
| `/products` | Browse and add products |
| `/customers` | Browse and add customers |
| `/orders/new` | Create a sale |
| `/orders/<id>` | View a receipt |
| `/reports` | Daily sales and best sellers |

## Repository map
```text
app/
  __init__.py          Flask application factory
  db.py                SQLite schema, connection, seed data
  routes.py             Request handling and business logic
  templates/            HTML templates for each screen
  static/style.css      Shared responsive styling
docs/
  system_design_report.pdf
  system_design_report.md
  context_dfd.png
  er_diagram.png
  input_design_screenshot.png
  data_dictionary.md
  requirements_traceability.md
  normalization_and_integrity.md
  design_decisions.md
tests/
  test_app.py
schema.sql              Standalone database schema
run.py                  Development entry point
requirements.txt        Python dependency list
```

## Design notes
- `orders` represents the transaction header; `order_items` represents the products within a transaction. This resolves the many-to-many relationship between orders and products.
- `order_items.unit_price` stores the price charged at the time of sale. A future menu-price update therefore does not rewrite historical receipts.
- A customer is optional so walk-in sales can be recorded. If a registered customer is deleted, the order remains and its customer reference becomes `NULL`.
- Foreign-key checks are enabled for each SQLite connection.
- The app is a classroom prototype. Before production use, add authentication, authorization, CSRF protection, automated backups, audit logging, tax/discount handling, and deployment secrets.

## Testing
Run:
```bash
pip install -r requirements.txt
python -m unittest discover -s tests -v
```

## GitHub submission
Create a new GitHub repository, commit the project files, and paste the repository URL into the course submission. If private, grant the instructor GitHub user `jdanieln` access before the deadline. The PDF report is included under `docs/`.

## Author
Student: Lisbeth Espinales Rayo
Course: ISM4113 – Systems Design  
Instructor:Prof. José Narváez  
Project: Coffee Shop Management System
