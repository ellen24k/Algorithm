-- 코드를 입력하세요
select
    i.INGREDIENT_TYPE, sum(f.TOTAL_ORDER) as TOTAL_ORDER
from 
    FIRST_HALF as f
inner join
    ICECREAM_INFO as i
on
    f.FLAVOR = i.FLAVOR
group by
    i.INGREDIENT_TYPE
order by
    TOTAL_ORDER ;