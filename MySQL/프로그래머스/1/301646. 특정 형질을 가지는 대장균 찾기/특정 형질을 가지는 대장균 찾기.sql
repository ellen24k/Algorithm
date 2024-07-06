-- 코드를 작성해주세요
select
    count(ID) as COUNT
from
    ECOLI_DATA
where
    conv(GENOTYPE,10,2) = '1'
    or
    conv(GENOTYPE,10,2) like '%01' 
    or 
    conv(GENOTYPE,10,2) like '%100' 
    or 
    conv(GENOTYPE,10,2) like '%101' 