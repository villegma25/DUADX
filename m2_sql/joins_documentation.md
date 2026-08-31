# SELECT, ORDER BY, LIMIT, GROUP BY AND JOINs

| Function | Description | Basic Syntax | Example |
|----------|-------------|--------------|---------|
| SELECT | Used to retrieve data from one or more tables. | SELECT columns FROM table; | SELECT * FROM Books; |
| ORDER BY | Sorts the results in ascending or descending order. | SELECT ... ORDER BY column ASC/DESC; | SELECT * FROM Books ORDER BY Name ASC; |
| LIMIT | Limits the number of records returned by the query. | SELECT ... LIMIT number; | SELECT * FROM Books LIMIT 5; |
| GROUP BY | Groups rows that have the same values in specified columns. It is commonly used with aggregate functions such as COUNT, SUM, AVG, MIN and MAX. | SELECT column, COUNT(*) FROM table GROUP BY column; | SELECT Author, COUNT(*) FROM Books GROUP BY Author; |
| INNER JOIN | Returns only records that have matching values in both tables. | SELECT ... FROM table1 INNER JOIN table2 ON condition; | SELECT Books.Name, Authors.Name FROM Books INNER JOIN Authors ON Books.Author = Authors.ID; |
| LEFT JOIN | Returns all records from the left table and the matching records from the right table. If there is no match, NULL is returned. | SELECT ... FROM table1 LEFT JOIN table2 ON condition; | SELECT Books.Name, Authors.Name FROM Books LEFT JOIN Authors ON Books.Author = Authors.ID; |
| RIGHT JOIN | Returns all records from the right table and matching records from the left table. | SELECT ... FROM table1 RIGHT JOIN table2 ON condition; | SELECT Authors.Name, Books.Name FROM Books RIGHT JOIN Authors ON Books.Author = Authors.ID; |

## Explanation

SELECT:
Used to select the information that we want to retrieve from
a database.

ORDER BY:
Used to sort the results. ASC sorts from lowest to highest or
alphabetically, while DESC sorts from highest to lowest.

LIMIT:
Used to restrict the number of rows returned.

GROUP BY:
Used to group records with the same value. It is commonly used
with functions such as COUNT, SUM, AVG, MIN and MAX.

INNER JOIN:
Returns only records that have a matching relationship between
the two tables.

LEFT JOIN:
Returns every record from the left table and matching records
from the right table. When there is no match, the right-side
columns contain NULL.

RIGHT JOIN:
Returns every record from the right table and matching records
from the left table. When there is no match, the left-side
columns contain NULL.