# Design Decisions and Course Theory

| Requirement / principle | Design decision | Evidence in repository |
|---|---|---|
| Users need a quick operating overview | Dashboard shows sales, completed orders, active products, recent transactions | `app/routes.py`, `dashboard.html` |
| Users need accurate transaction records | Each order has a header and separate item rows | `schema.sql`, `/orders` route |
| Walk-in sales must be possible | `orders.customer_id` is nullable and the order form includes Walk-in customer | `new_order.html`, schema |
| Historical sales should remain stable | Sale-time price is copied to `order_items.unit_price` | `create_order()` |
| Data must remain consistent | PKs, FKs, UNIQUE, CHECK, NOT NULL, transaction rollback | `schema.sql`, `db.py`, `routes.py` |
| Staff should make fewer input errors | Required fields, numeric minimums, dropdowns, clear form labels and feedback | HTML templates |
| Reports should support decisions | Daily sales and best-selling product summaries | `reports()` route |
| Frequently used lookups should remain practical | Index on order date and order-item order reference | `schema.sql` |

## Systems Design concepts
- **Requirements analysis:** the system's main user tasks are managing menu products, customer records, order entry, and reviewing sales.
- **Process modeling:** the context DFD treats the staff member as the external entity and the application as the process, with product/customer/order inputs and receipt/report outputs.
- **Data modeling:** the ER model identifies entities, attributes, keys, and cardinalities before implementation.
- **Input design:** dropdowns constrain choices, numeric fields constrain quantity and price, required attributes are marked, and confirmation/error messages explain the result.
- **Normalization:** separate entities reduce update, insert, and delete anomalies.
- **Data integrity:** database constraints complement interface validation because requests may originate from sources other than the visible form.
- **Implementation evidence:** the diagrams and this report are linked to concrete files and routes, rather than only describing a hypothetical system.
