-- 코드를 입력하세요
SELECT 
    NAME, count(*) as COUNT 
from 
    ANIMAL_INS 
group by 
    NAME 
having 
    COUNT > 1 and NAME is not null
order by 
    NAME;
