# Data Dictionary

| Table | Field | Type | Key / Rule | Meaning |
|---|---|---|---|---|
| customers | customer_id | INTEGER | PK, auto-increment | Unique customer identifier |
| customers | full_name | TEXT | NOT NULL | Customer's display name |
| customers | email | TEXT | UNIQUE, nullable | Optional contact email; duplicates rejected |
| customers | phone | TEXT | nullable | Optional phone number |
| customers | created_at | TEXT | default timestamp | Date/time customer record was created |
| products | product_id | INTEGER | PK, auto-increment | Unique menu item identifier |
| products | product_name | TEXT | NOT NULL, UNIQUE | Product/menu name |
| products | category | TEXT | NOT NULL | Menu grouping, such as Coffee or Bakery |
| products | unit_price | REAL | NOT NULL, CHECK >= 0 | Current menu price |
| products | active | INTEGER | default 1, CHECK 0/1 | Whether product is available for new orders |
| orders | order_id | INTEGER | PK, auto-increment | Unique order identifier |
| orders | customer_id | INTEGER | FK to customers, nullable | Registered customer; NULL means walk-in or removed customer |
| orders | order_date | TEXT | default timestamp, NOT NULL | Time the order was recorded |
| orders | status | TEXT | CHECK allowed values | Order lifecycle state |
| order_items | order_item_id | INTEGER | PK, auto-increment | Unique order line identifier |
| order_items | order_id | INTEGER | FK to orders, NOT NULL | Parent transaction |
| order_items | product_id | INTEGER | FK to products, NOT NULL | Menu item sold |
| order_items | quantity | INTEGER | CHECK > 0 | Number of units sold |
| order_items | unit_price | REAL | CHECK >= 0 | Price captured for this sale |
