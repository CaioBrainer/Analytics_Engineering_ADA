WITH calendar_bronze_not AS (SELECT *, price * 5.12 AS price_real FROM {{ ref('calendar_bronze') }}
    WHERE listing_id NOTNULL
    AND price NOTNULL
    AND adjusted_price NOTNULL
    AND data NOTNULL
    AND minimum_nights NOTNULL
    AND maximum_nights NOTNULL
    AND available NOTNULL
      AND price > 0),

stats_cte AS (
    SELECT
        AVG(price) AS avg_price,
        STDDEV(price) AS std_dev
    FROM calendar_bronze_not
)

SELECT listing_id, price as price_dolar, price_real, data, available
FROM calendar_bronze_not, stats_cte
WHERE price BETWEEN avg_price - 2 * std_dev AND avg_price + 2 * std_dev
