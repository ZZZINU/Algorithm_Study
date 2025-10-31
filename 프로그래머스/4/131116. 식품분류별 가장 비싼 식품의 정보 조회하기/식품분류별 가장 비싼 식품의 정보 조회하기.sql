-- 코드를 입력하세요
with my_sql as (SELECT CATEGORY, price, PRODUCT_NAME, 
ROW_NUMBER() over (partition by CATEGORY order by price desc) as ranked_category
FROM FOOD_PRODUCT)

select CATEGORY, price, PRODUCT_NAME
from my_sql
where ranked_category = 1 and CATEGORY IN ('과자', '국', '김치', '식용유')
order by price desc

