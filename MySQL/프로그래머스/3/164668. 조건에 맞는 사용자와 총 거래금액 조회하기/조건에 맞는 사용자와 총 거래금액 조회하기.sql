-- 코드를 입력하세요
select
    user.USER_ID, user.NICKNAME, sum(board.PRICE) as TOTAL_SALES
from
    USED_GOODS_USER as user
inner join
    USED_GOODS_BOARD as board
on
    board.WRITER_ID = user.USER_ID
where
    board.STATUS = "DONE"
group by
    board.WRITER_ID
having
    TOTAL_SALES >= 700000
order by
    TOTAL_SALES;