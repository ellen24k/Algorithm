-- 코드를 입력하세요
select 
    hour(DATETIME) as HOUR, count(*) as COUNT 
from 
    ANIMAL_OUTS 
where 
    hour(DATETIME) >= 9 && hour(DATETIME) < 20
group by 
    HOUR 
order by 
    HOUR;