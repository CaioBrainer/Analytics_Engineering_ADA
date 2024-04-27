with source_reviews as (
    select * from {{ source('air_bnb', 'reviews_raw') }}
),

final AS (
    SELECT listing_id,
           CAST(date AS DATE) AS date
           FROM source_reviews
)

select * from final