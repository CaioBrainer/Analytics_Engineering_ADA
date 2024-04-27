with source_calendar as (
    select * from {{ source('air_bnb', 'calendar_raw') }}
),

final AS (
    SELECT listing_id,
           CAST(REPLACE(REPLACE(price, '$', ''), ',', '') AS FLOAT) AS price,
           CAST(REPLACE(REPLACE(adjusted_price, '$', ''), ',', '') AS FLOAT) AS adjusted_price,
           CAST(date AS DATE) AS Data,
           CAST(minimum_nights AS INTEGER) AS minimum_nights,
           CAST(maximum_nights AS INTEGER) AS maximum_nights,
           available

    FROM source_calendar
)

select * from final