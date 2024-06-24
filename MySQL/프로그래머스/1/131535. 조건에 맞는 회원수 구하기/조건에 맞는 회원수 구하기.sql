-- 코드를 입력하세요
SELECT count(*) as USERS from user_info where extract(year from joined) = 2021 && age >= 20 && age <= 29;