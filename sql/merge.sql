MERGE `ajay-project-493013.sales_dataset.processed_sales` T
USING `ajay-project-493013.sales_dataset.staging_sales` S
ON T.order_id = S.order_id

WHEN MATCHED THEN
UPDATE SET
    product = S.product,
    amount = S.amount,
    city = S.city,
    order_date = S.order_date,
    amount_with_tax = S.amount_with_tax

WHEN NOT MATCHED THEN
INSERT (
    order_id,
    product,
    amount,
    city,
    order_date,
    amount_with_tax
)
VALUES (
    S.order_id,
    S.product,
    S.amount,
    S.city,
    S.order_date,
    S.amount_with_tax
);