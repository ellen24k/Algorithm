-- 코드를 작성해주세요
with TOTAL_LENGTH as (
select 
    ifnull(length,10) as LENGTH
from 
    FISH_INFO
)

select round(avg(LENGTH),2) as AVERAGE_LENGTH from TOTAL_LENGTH;

# select round(avg(ifnull(LENGTH,10)),2) as AVERAGE_LENGTH from FISH_INFO;
