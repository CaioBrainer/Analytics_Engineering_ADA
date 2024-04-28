with source_reviews as (
    select * from {{ source('air_bnb', 'reviews_raw') }}
),

final AS (
    SELECT listing_id,
           id,
           CAST(date AS DATE) AS date,
           reviewer_id,
           reviewer_name,
           comments
    FROM source_reviews
)

select * from final