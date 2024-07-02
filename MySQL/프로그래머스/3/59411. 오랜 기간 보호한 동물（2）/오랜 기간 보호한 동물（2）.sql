-- 코드를 입력하세요
select 
    ins.ANIMAL_ID, ins.NAME
from
    ANIMAL_INS as ins
right join
    ANIMAL_OUTS as outs
on
    ins.ANIMAL_ID = outs.ANIMAL_ID
order by
    datediff(outs.DATETIME, ins.DATETIME) desc
limit 2;