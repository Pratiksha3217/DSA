# Write your MySQL query statement below

-- select salary as SecondHighestSalary
-- FROM (SELECT SALARY,ROW_NUMBER() OVER(ORDER BY SALARY DESC) AS RNBR from  employee e) t
-- WHERE RNBR =2

select max(salary) as SecondHighestSalary 
from employee
where salary < (select max(salary)from employee);