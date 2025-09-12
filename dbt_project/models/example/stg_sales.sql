-- This model cleans up the raw sales data
SELECT
    order_id,
    product_name,
    amount,
    CAST(order_date AS DATE) AS order_date -- Casting to a proper date type
FROM
    {{ source('raw', 'raw_sales') }}