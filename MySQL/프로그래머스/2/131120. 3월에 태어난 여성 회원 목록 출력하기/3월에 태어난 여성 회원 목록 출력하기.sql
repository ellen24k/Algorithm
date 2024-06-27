-- 코드를 입력하세요
select MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH,"%Y-%m-%d") from member_profile where GENDER = 'W' && month(DATE_OF_BIRTH) = '03' && TLNO is not null order by MEMBER_ID;