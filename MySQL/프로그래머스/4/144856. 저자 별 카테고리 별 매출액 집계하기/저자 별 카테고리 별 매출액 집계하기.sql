-- 코드를 입력하세요
SELECT
    b.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, SUM(bs.SALES * b.PRICE) as TOTAL_SALES
FROM
    BOOK AS b
JOIN
    AUTHOR as a ON b.AUTHOR_ID = a.AUTHOR_ID
JOIN
    BOOK_SALES as bs ON b.BOOK_ID = bs.BOOK_ID
WHERE 
    DATE_FORMAT(bs.SALES_DATE, '2022-01-%d') = DATE_FORMAT(bs.SALES_DATE, '%Y-%m-%d')
GROUP BY b.AUTHOR_ID, b.CATEGORY 
ORDER BY b.AUTHOR_ID, b.CATEGORY DESC