-- 코드를 작성해주세요
select i.ID, n.FISH_NAME, i.LENGTH
from
    FISH_INFO as i
join
    FISH_NAME_INFO as n
on
    i.FISH_TYPE = n.FISH_TYPE
where (i.FISH_TYPE, i.LENGTH) in (
    select FISH_TYPE, MAX(LENGTH)
    FROM FISH_INFO
    GROUP BY FISH_TYPE)
order by
    i.ID;