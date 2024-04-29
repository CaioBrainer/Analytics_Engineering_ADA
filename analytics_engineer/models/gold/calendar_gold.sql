WITH final AS (
    SELECT 
    data,
	COUNT(*) AS number_of_reservations,
	ROUND(MIN(price_real)::numeric, 2) as min_price_real,
	ROUND(MAX(price_real)::numeric, 2) as max_price_real,
    ROUND(avg(price_dolar)::numeric, 2) as avg_price_real
FROM 
    {{ ref('calendar_silver') }}
GROUP BY 
	data
ORDER BY 
	data DESC
)

SELECT * FROM final