WITH final AS (SELECT
CASE
        WHEN review_scores_rating >= 0 AND review_scores_rating < 1 THEN '0-1'
        WHEN review_scores_rating >= 1 AND review_scores_rating < 2 THEN '1-2'
        WHEN review_scores_rating >= 2 AND review_scores_rating < 3 THEN '2-3'
        WHEN review_scores_rating >= 3 AND review_scores_rating < 4 THEN '3-4'
        WHEN review_scores_rating >= 4 AND review_scores_rating <= 5 THEN '4-5'
    END AS rating_interval,
    COUNT(*) AS count_reviews
FROM
    {{ ref('listings_silver') }}
GROUP BY
    CASE
        WHEN review_scores_rating >= 0 AND review_scores_rating < 1 THEN '0-1'
        WHEN review_scores_rating >= 1 AND review_scores_rating < 2 THEN '1-2'
        WHEN review_scores_rating >= 2 AND review_scores_rating < 3 THEN '2-3'
        WHEN review_scores_rating >= 3 AND review_scores_rating < 4 THEN '3-4'
        WHEN review_scores_rating >= 4 AND review_scores_rating <= 5 THEN '4-5'
    END
ORDER BY
    rating_interval)

select * FROM final