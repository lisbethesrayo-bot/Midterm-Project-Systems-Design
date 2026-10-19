# Requirements Traceability

| Requirement | Implementation | Evidence / how to verify |
|---|---|---|
| Register menu items and prices | Product form and `products` table | `/products`; add a product |
| Register customer details | Customer form and `customers` table | `/customers`; add a customer |
| Record a sale with multiple items | Order form and `orders` + `order_items` | `/orders/new`; add two lines |
| Calculate totals accurately | `quantity * unit_price` per line and summed order total | Order receipt |
| Support walk-in customers | Nullable customer foreign key | Submit order without selecting customer |
| Prevent invalid quantity and negative price | Form validation plus SQL CHECK constraints | Try quantity 0 or negative price |
| Review sales activity | Dashboard and reports | `/` and `/reports` |
| Persist records | SQLite database | Restart app and review saved records |
| Explain design | DFD, ER diagram, dictionary, normalization and theory report | `docs/` |
