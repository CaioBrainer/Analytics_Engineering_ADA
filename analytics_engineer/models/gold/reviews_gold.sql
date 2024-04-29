WITH final AS (
    SELECT reviewer_id, reviewer_name
    FROM {{ ref('reviews_silver') }}
    GROUP BY reviewer_id, reviewer_name
)

SELECT * FROM final