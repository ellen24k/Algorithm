-- 코드를 작성해주세요
select
    concat(
    case 
        when month(DIFFERENTIATION_DATE) <= 3 then 1
        when month(DIFFERENTIATION_DATE) <= 6 then 2
        when month(DIFFERENTIATION_DATE) <= 9 then 3
        else 4
    end, 'Q') as QUARTER,
    count(*) as ECOLI_COUNT
from
    ECOLI_DATA
group by
    QUARTER
order by
    QUARTER;