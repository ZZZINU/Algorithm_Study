-- 코드를 입력하세요
with row_table as (SELECT CATEGORY, PRICE, PRODUCT_NAME, ROW_NUMBER() over (partition by CATEGORY order by PRICE desc) as row_num

from FOOD_PRODUCT
where CATEGORY IN ('과자', '국', '김치', '식용유'))

SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from row_table
where row_num = 1
order by MAX_PRICE desc


