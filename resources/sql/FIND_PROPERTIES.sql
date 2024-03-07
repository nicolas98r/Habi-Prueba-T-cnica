SELECT address, city, status, price, description FROM property p 
INNER JOIN 
(SELECT sh.update_date, sh.property_id, sh.status_id, s.name AS status
FROM status_history sh
INNER JOIN (
    SELECT MAX(update_date) AS update_date, property_id
    FROM status_history
    GROUP BY property_id
) max ON sh.property_id = max.property_id AND sh.update_date = max.update_date
INNER JOIN status s ON s.id = sh.status_id
) sh ON p.id = sh.property_id
WHERE status IN ("pre_venta", "en_venta", "vendido") AND price != 0 {filter_query};