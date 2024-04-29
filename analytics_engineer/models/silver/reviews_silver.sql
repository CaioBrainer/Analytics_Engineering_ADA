WITH
    reviews_bronze_notnull AS (
        SELECT *
        FROM {{ ref('reviews_bronze') }}
        WHERE
            listing_id IS NOT NULL
            AND id IS NOT NULL
            AND date IS NOT NULL
            AND reviewer_id IS NOT NULL
            AND reviewer_name IS NOT NULL
            AND comments IS NOT NULL
    ),
    final AS (
        SELECT DISTINCT
            listing_id, id, date, reviewer_id, reviewer_name, comments
        FROM reviews_bronze_notnull
    )

SELECT * FROM final
