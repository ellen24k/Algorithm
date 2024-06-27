-- 코드를 입력하세요
select
    board.TITLE, reply.BOARD_ID, reply.REPLY_ID, reply.WRITER_ID, reply.CONTENTS, date_format(reply.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from
    USED_GOODS_REPLY as reply
inner join
    USED_GOODS_BOARD as board
on 
    board.BOARD_ID = reply.BOARD_ID
where 
    date_format(board.CREATED_DATE, '%Y-%m') = '2022-10'
order by
    reply.CREATED_DATE, board.TITLE;
