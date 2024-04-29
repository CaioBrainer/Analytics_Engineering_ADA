with final as (
    SELECT reviewer_id, reviewer_name, count(*)
    FROM {{ ref('reviews_silver')}}
    GROUP BY reviewer_id, reviewer_name
    ORDER BY count DESC
    LIMIT 10
)

select reviewer_name, count from final