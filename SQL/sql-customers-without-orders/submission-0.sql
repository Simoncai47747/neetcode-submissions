-- Write your query below
Select
    name
FROM
    customers
WHERE
    customers.id NOT IN (
        SELECT customer_id
        FROM orders
    )