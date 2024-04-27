with source_listings as (
    select * from {{ source('air_bnb', 'listings_raw') }}
),

final as (
    SELECT
    CAST(REPLACE(REPLACE(price, '$', ''), ',', '') AS FLOAT) AS price
FROM
    source_listings)

select * from final