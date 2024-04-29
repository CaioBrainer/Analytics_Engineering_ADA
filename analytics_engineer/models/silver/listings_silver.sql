WITH
    listings_bronze_notnull AS (
        SELECT *
        FROM {{ ref('listings_bronze') }}
        WHERE
            id IS NOT NULL
            AND host_id IS NOT NULL
            AND host_name IS NOT NULL
            AND host_since IS NOT NULL
            AND host_response_rate IS NOT NULL
            AND host_acceptance_rate IS NOT NULL
            AND neighbourhood_cleansed IS NOT NULL
            AND property_type IS NOT NULL
            AND accommodates IS NOT NULL
            AND bedrooms IS NOT NULL
            AND beds IS NOT NULL
            AND price IS NOT NULL
            AND number_of_reviews IS NOT NULL
            AND review_scores_rating IS NOT NULL
            AND reviews_per_month IS NOT NULL
    ),
    final AS (
        SELECT
            CAST(REPLACE(host_response_rate, '%', '') AS INTEGER) AS host_response_rate,
            CAST(REPLACE(host_acceptance_rate, '%', '') AS INTEGER) AS host_acceptance_rate,
            id,
            host_id,
            host_name,
            host_since,
            neighbourhood_cleansed,
            property_type,
            accommodates,
            bedrooms,
            beds,
            price,
            number_of_reviews,
            review_scores_rating,
            reviews_per_month
        FROM listings_bronze_notnull
    )

SELECT DISTINCT * FROM final