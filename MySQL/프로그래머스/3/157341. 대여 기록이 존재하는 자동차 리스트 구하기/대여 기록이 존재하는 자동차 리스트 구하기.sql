-- 코드를 입력하세요
# set profiling = 1;

select
    distinct car.CAR_ID
from
    CAR_RENTAL_COMPANY_CAR as car
inner join
    CAR_RENTAL_COMPANY_RENTAL_HISTORY as history
on
    car.CAR_ID = history.CAR_ID
where
    car.CAR_TYPE = "세단"
    and
    month(history.START_DATE) = "10"
order by
    car.CAR_ID desc;
    
# show profiles