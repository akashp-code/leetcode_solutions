# Write your MySQL query statement below
select name, unique_id
from employees
left join employeeuni 
on employees.id = employeeuni.id;