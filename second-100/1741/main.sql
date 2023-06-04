SELECT emp_id, event_day as day, sum(out_time - in_time) as total_time
FROM Employees
GROUP BY event_day, emp_id