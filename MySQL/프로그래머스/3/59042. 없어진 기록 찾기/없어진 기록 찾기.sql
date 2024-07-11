-- 코드를 입력하세요
select
    outs.ANIMAL_ID, outs.NAME
from
    ANIMAL_OUTS as outs
left join
    ANIMAL_INS as ins
on 
    ins.ANIMAL_ID = outs.ANIMAL_ID
where
    ins.ANIMAL_ID is null
order by
    ins.ANIMAL_ID;