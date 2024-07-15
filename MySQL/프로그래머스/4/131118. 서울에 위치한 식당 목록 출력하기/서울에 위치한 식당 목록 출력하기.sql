-- 코드를 입력하세요
select 
    info.REST_ID, info.REST_NAME, info.FOOD_TYPE, info.FAVORITES, info.ADDRESS, round(avg(review.REVIEW_SCORE),2) as SCORE
from
    REST_INFO as info
inner join
    REST_REVIEW as review
on
    info.REST_ID = review.REST_ID
group by
    info.REST_ID
having
    info.ADDRESS like '서울%'
order by
    SCORE desc, info.FAVORITES desc;