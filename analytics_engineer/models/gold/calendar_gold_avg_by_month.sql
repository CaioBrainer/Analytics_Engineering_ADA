WITH final AS (
    SELECT 
        EXTRACT(MONTH FROM data) AS mes,
        AVG(price_real) AS average_price
FROM 
    {{ ref('calendar_silver') }}
GROUP BY 
	mes
ORDER BY 
	mes
)

SELECT * FROM final