{{ config(materialized='table') }}

SELECT
    sha as commit_hash,
    commit__author__name as author_name,
    commit__author__email as author_email,
    CAST(commit__author__date AS TIMESTAMP) as commit_timestamp,
    commit__message as commit_message
FROM {{ source('bronze_layer', 'get_commits') }}
WHERE commit__author__name IS NOT NULL