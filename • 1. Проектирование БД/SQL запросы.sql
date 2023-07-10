-- 2.1 Получение информации о сумме товаров заказанных под каждого клиента:
SELECT 
	client.title, 
	SUM(product.price * order.amount)
FROM client
JOIN order ON client.id = order.id_client
JOIN product ON order.id_product = product.id
GROUP BY client.title;

-- 2.2 Найти количество дочерних элементов первого уровня вложенности для категорий номенклатуры:

-- • Если под первым уровнем вложенности имеются в виду категории, у которых нет родительской категории
-- («Бытовая техника» и «Компьютеры» из примера), то запрос будет такой
	SELECT 
		category.title,
	    COUNT(DISTINCT cat_copy.id) AS childs_counter
	FROM category
	LEFT JOIN category AS cat_copy ON category.id = cat_copy.parent_cat
	WHERE category.parent_cat IS NULL
	GROUP BY category.title;

-- • Если нужно отобразить полную структуру, как показано в таблице примера
	WITH RECURSIVE CategoryTree AS (
	  SELECT id, title, parent_cat, 0 AS level
	  FROM category
	  WHERE parent_cat IS NULL
	  UNION ALL
	  SELECT cat.id, cat.title, cat.parent_cat, CT.level + 1
	  FROM category AS cat
	  JOIN CategoryTree AS CT ON CT.ID = cat.parent_cat
	)
	SELECT RPAD('', level * 4, ' ') || CT.title AS category, COUNT(DISTINCT child_cat.id) AS child_counter
	FROM CategoryTree AS CT
	LEFT JOIN category AS child_cat ON CT.id = child_cat.parent_cat
	GROUP BY CT.id, CT.title, CT.level
	ORDER BY CT.id;