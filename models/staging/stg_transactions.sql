with source as (
  SELECT * FROM {{ source('my_source', 'seed_data') }}
)

SELECT
  customer_id,
  customer_name,
  cast(transaction_date as date) as transaction_date,
  amount
FROM source
