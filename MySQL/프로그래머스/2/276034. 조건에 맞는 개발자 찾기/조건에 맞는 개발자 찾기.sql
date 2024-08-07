-- 코드를 작성해주세요
select 
    ID, EMAIL, FIRST_NAME, LAST_NAME
from
    DEVELOPERS 
where
    SKILL_CODE & (select distinct CODE from SKILLCODES where NAME = 'Python') != 0
    or
    SKILL_CODE & (select distinct CODE from SKILLCODES where Name = 'C#') != 0
order by
    ID;