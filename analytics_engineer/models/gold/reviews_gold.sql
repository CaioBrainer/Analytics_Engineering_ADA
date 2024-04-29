WITH final AS (
    SELECT *
    FROM {{ ref('reviews_silver') }}
)

SELECT * FROM final