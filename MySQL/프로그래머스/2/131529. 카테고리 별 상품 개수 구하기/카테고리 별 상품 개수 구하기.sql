-- 코드를 입력하세요
select left(PRODUCT_CODE,2) as CATEGORY, count(*) as PRODUCTS from PRODUCT group by CATEGORY;

# select substr(product_code,1,2) , count(*) from product group by substr(product_code,1,2)