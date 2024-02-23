SELECT H.HISTORY_ID,
ROUND(CASE WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 7 
 THEN DAILY_FEE * (DATEDIFF(END_DATE, START_DATE) + 1) 
WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 30 
  THEN DAILY_FEE * (DATEDIFF(END_DATE, START_DATE) + 1)  * 0.95
 WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 90
  THEN DAILY_FEE * (DATEDIFF(END_DATE, START_DATE) + 1) * 0.92
 ELSE DAILY_FEE * (DATEDIFF(END_DATE, START_DATE) + 1) * 0.85 END
) AS FEE

FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON C.CAR_TYPE = P.CAR_TYPE
WHERE C.CAR_TYPE = "트럭"
GROUP BY H.HISTORY_ID
ORDER BY FEE DESC, H.HISTORY_ID DESC