-- 코드를 입력하세요
SELECT MONTH(START_DATE) as MONTH, CAR_ID, COUNT (*) AS RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where DATE_FORMAT(START_DATE, '%Y-%m') between '2022-08' and '2022-10'
AND CAR_ID IN (SELECT CAR_ID
              from CAR_RENTAL_COMPANY_RENTAL_HISTORY
               where DATE_FORMAT(START_DATE, '%Y-%m') between '2022-08' and '2022-10'
               group by CAR_ID
               having count(CAR_ID) >= 5
              )
group by CAR_ID, MONTH(START_DATE)
# HAVING RECORDS >= 1
ORDER BY MONTH, CAR_ID DESC