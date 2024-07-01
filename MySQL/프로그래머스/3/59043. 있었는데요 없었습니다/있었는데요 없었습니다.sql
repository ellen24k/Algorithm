-- 코드를 입력하세요
select
    ins.ANIMAL_ID, ins.NAME
from 
    ANIMAL_INS as ins
inner join
    ANIMAL_OUTS as outs
on 
    ins.ANIMAL_ID = outs.ANIMAL_ID
where
    ins.DATETIME > outs.DATETIME
order by
    ins.DATETIME;
    