-- 코드를 입력하세요
select
    truncate(PRICE,-4) as PRICE_GROUP, count(*) as PRODUCTS
from
    PRODUCT
group by
    PRICE_GROUP
order by
    PRICE_GROUP;
    