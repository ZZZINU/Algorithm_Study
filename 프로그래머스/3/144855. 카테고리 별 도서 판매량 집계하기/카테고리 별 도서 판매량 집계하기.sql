SELECT B.CATEGORY, SUM(BS.SALES)
FROM BOOK B
JOIN BOOK_SALES BS ON B.BOOK_ID = BS.BOOK_ID
WHERE BS.SALES_DATE LIKE '2022-01%'
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY