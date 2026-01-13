WITH cte AS (
    SELECT
        departmentId,
        MAX(salary) AS max_salary
    FROM employee
    GROUP BY departmentId
)
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM employee e
JOIN cte
    ON e.departmentId = cte.departmentId
   AND e.salary = cte.max_salary
JOIN department d
    ON e.departmentId = d.id;
