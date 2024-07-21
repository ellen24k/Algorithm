-- 코드를 입력하세요
select
    year(s.SALES_DATE) as YEAR, month(s.SALES_DATE) as MONTH, i.GENDER as GENDER, count(distinct s.USER_ID) as USERS
from
    ONLINE_SALE as s
join
    USER_INFO as i
on 
    s.USER_ID = i.USER_ID and i.GENDER is not null
group by
    YEAR, MONTH, GENDER
order by
    YEAR, MONTH, GENDER;