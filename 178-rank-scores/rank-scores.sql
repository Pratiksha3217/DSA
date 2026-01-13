-- # Write your MySQL query statement below
-- SELECT score, 
--         DENSE_RANK() OVER(order by score DESC ) AS Rank
-- FROM Scores
-- ORDER BY score DESC;

SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
FROM Scores
ORDER BY score DESC;
