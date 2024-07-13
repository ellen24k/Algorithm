-- 코드를 입력하세요
select
    apnt.APNT_NO, pt.PT_NAME, apnt.PT_NO, apnt.MCDP_CD, dr.DR_NAME, apnt.APNT_YMD
from
    APPOINTMENT as apnt
inner join 
    PATIENT as pt
on
    apnt.PT_NO = pt.PT_NO
inner join
    DOCTOR as dr
on 
    apnt.MDDR_ID = dr.DR_ID
where
    apnt.MCDP_CD = 'CS'
    and
    date_format(apnt.APNT_YMD, "%Y-%m-%d") = "2022-04-13"
    and
    apnt.APNT_CNCL_YN = "N"
order by
    apnt.APNT_YMD;