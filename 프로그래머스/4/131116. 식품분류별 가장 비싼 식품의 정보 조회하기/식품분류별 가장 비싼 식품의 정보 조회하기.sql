-- 코드를 입력하세요
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT 
where price in (select max(price) from FOOD_PRODUCT group by category)
and category in ('과자', '국', '김치', '식용유')
ORDER BY MAX_PRICE DESC