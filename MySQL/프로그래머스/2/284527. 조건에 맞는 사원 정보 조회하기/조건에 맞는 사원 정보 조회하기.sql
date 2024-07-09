-- 코드를 작성해주세요
select
    sum(grade.SCORE) as SCORE, 
    employees.EMP_NO, 
    employees.EMP_NAME, 
    employees.POSITION, 
    employees.EMAIL
from
    HR_EMPLOYEES as employees
inner join
    HR_GRADE as grade
on 
    employees.EMP_NO = grade.EMP_NO
group by
    employees.EMP_NO
having
    SCORE = (select sum(SCORE) as SUM from HR_GRADE group by EMP_NO order by SUM desc limit 1);