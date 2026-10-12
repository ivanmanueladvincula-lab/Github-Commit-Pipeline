{{ config(materialized='table') }}

SELECT
    CAST(commit_timestamp AS DATE) as commit_date,
    author_name,
    COUNT(commit_hash) as total_commits
FROM {{ ref('silver_commits') }}
GROUP BY 1, 2
ORDER BY commit_date DESC

