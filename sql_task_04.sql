SELECT
    neighborhood_id,
    name
FROM 
    neighborhoods
WHERE 
    name LIKE '%Hare' OR name LIKE 'Loop'
