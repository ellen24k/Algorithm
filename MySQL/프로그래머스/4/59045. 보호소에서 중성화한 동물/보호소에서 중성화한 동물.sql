-- 코드를 입력하세요
# explain select 
select 
    ins.ANIMAL_ID, ins.ANIMAL_TYPE, ins.NAME
from
    ANIMAL_INS as ins
inner join 
    ANIMAL_OUTS as outs
on 
    ins.ANIMAL_ID = outs.ANIMAL_ID
where
    ins.SEX_UPON_INTAKE like "Intact%"
    and
    outs.SEX_UPON_OUTCOME not like "Intact%"
order by
    ins.ANIMAL_id;