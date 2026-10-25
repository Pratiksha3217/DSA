# Write your MySQL query statement below

-- with cte(
--     select player_id, event_date
--     from activity
-- )
select player_id,
     min(event_date) as first_login
from activity
group by player_id
