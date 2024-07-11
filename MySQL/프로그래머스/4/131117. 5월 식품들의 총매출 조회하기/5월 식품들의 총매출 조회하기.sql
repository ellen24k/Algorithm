-- 코드를 입력하세요
select 
    pd.PRODUCT_ID, pd.PRODUCT_NAME, (pd.PRICE * sum(od.AMOUNT)) as TOTAL_SALES
from
    FOOD_PRODUCT as pd
inner join
    FOOD_ORDER as od
on 
    pd.PRODUCT_ID = od.PRODUCT_ID
where 
    date_format(od.PRODUCE_DATE, "%Y-%m") = '2022-05'
group by
    od.PRODUCT_ID
order by
    TOTAL_SALES desc, pd.PRODUCT_ID;

