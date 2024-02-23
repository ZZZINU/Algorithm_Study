SELECT YEAR(O.SALES_DATE) YEAR, MONTH(O.SALES_DATE) MONTH,
COUNT(DISTINCT O.USER_ID) AS PUCHASED_USERS,
ROUND(COUNT(DISTINCT O.USER_ID) / (SELECT COUNT(*) FROM USER_INFO WHERE JOINED LIKE "2021%"), 1) AS PUCHASED_RATIO
FROM USER_INFO U
JOIN ONLINE_SALE O ON U.USER_ID = O.USER_ID
WHERE U.JOINED LIKE "2021%"
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH