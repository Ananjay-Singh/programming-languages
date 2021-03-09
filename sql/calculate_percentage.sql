Problem statement :
If the preferred delivery date of the customer is the same as the order date then the order is called immediate otherwise it called scheduled.
Write an SQL query to find the percentage of immediate orders in the table, rounded to 2 decimal places.

Approach -1
SELECT 
  ROUND(AVG(CASE WHEN order_date=customer_pref_delivery_date THEN 1 ELSE 0 END)*100,2) AS immediate_percentage
FROM
  Delivery

Approach -2
Select
    Round(Sum(order_date = customer_pref_delivery_date)/Count(order_date)*100,2) as immediate_percentage
From
    Delivery

Approach -3
SELECT
   ROUND((d.count_imm*100) / d1.total_count ,2) as immediate_percentage
FROM
(
   SELECT
       sum(x.immediate) as count_imm
   FROM
   (
       SELECT
           *
           ,case when order_date=customer_pref_delivery_date then 1 else 0 end as immediate
       FROM
           Delivery
   )x
)d
LEFT OUTER JOIN
(
   SELECT
       count(*) as total_count
   FROM
       Delivery
)d1
ON 1= 1
