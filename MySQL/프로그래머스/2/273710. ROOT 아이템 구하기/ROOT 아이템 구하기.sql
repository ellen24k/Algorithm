-- 코드를 작성해주세요
select 
    item_info.ITEM_ID, ITEM_NAME 
from 
    ITEM_INFO 
inner join 
    ITEM_TREE 
on 
    item_info.item_id = item_tree.item_id 
where 
    parent_item_id is null;