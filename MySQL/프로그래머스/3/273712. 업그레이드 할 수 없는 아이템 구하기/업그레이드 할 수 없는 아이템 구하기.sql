-- 코드를 작성해주세요
select 
    info.ITEM_ID, info.ITEM_NAME, info.RARITY 
from 
    ITEM_INFO info 
where 
    info.ITEM_ID not in (select distinct parent_item_id from item_tree where parent_item_id is not null)
order by
    info.ITEM_ID desc;
    