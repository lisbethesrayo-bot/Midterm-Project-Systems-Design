# Normalization and Data Integrity

## Example of avoidable duplication
A single flat sales table could repeat customer name, phone, product name, category, and current price on every item line. If a customer made 20 purchases, their contact information could be stored 20 times. Changing the phone number would require updating many rows, creating an update anomaly.

## Design response
The design separates data into `customers`, `products`, `orders`, and `order_items`. Customer attributes depend on `customer_id`; menu attributes depend on `product_id`; transaction header attributes depend on `order_id`; and each order line records its own quantity and sale-time unit price. The `order_items` table connects orders and products and resolves their many-to-many relationship.

## Normalization
- **First Normal Form (1NF):** each field contains a single value; multiple purchased products are stored as separate order-item rows rather than a comma-separated list.
- **Second Normal Form (2NF):** the schema uses single-column surrogate primary keys. Non-key attributes in each table describe that table's identified entity rather than only part of a composite key.
- **Third Normal Form (3NF):** customer contact data is kept in `customers`, and product descriptions/category/current price are kept in `products`, avoiding transitive dependencies in transaction records. `order_items.unit_price` is an intentional historical snapshot of the price charged, not a duplicate of the current product price.

## Integrity controls
- Primary keys uniquely identify rows.
- Foreign keys connect order headers to customers and order lines to orders/products.
- `NOT NULL` protects required values.
- `UNIQUE` prevents duplicate product names and duplicate non-null customer emails.
- `CHECK` constraints reject negative prices, non-positive quantities, invalid active flags, and unsupported order statuses.
- The application validates required fields and quantity before writing.
- Order header and item rows are committed together; on failure, the transaction is rolled back.
- SQLite foreign-key enforcement is enabled per connection.

## Cardinality
One customer can have zero or many orders; an order can belong to zero or one registered customer. One order has one or many order items. One product can appear on many order items. Orders and products are therefore many-to-many through `order_items`.
