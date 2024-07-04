-- 코드를 입력하세요
select
    half.FLAVOR
from
    FIRST_HALF as half
left join
    ICECREAM_INFO as info
on
    half.FLAVOR = info.FLAVOR
where
    half.TOTAL_ORDER >= 3000
    and
    info.INGREDIENT_TYPE = 'fruit_based'
order by
    half.TOTAL_ORDER desc;