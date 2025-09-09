import sqlite3

#task1
with sqlite3.connect("../db/lesson.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1") 
    cursor=conn.cursor()

        
    sql_statement = """SELECT o.order_id,
    SUM(li.quantity*p.price) AS total_price
    FROM orders o
    JOIN line_items li 
    ON o.order_id = li.order_id
    JOIN products p 
    ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5
    ;"""
    
    cursor.execute(sql_statement)
    result = cursor.fetchall()
    
    print("id total price")
    for row in result:
        print(row)

#task2

    sql_statement1 = """SELECT c.customer_name,
        AVG(subq.total_price) AS average_total_price
        FROM customers c
        LEFT JOIN(
            SELECT o.customer_id AS customer_id_b,
                SUM(li.quantity*p.price) AS total_price
            FROM orders o
            JOIN line_items li  
            ON o.order_id = li.order_id
            JOIN products p  
            ON li.product_id = p.product_id
            GROUP BY o.order_id)
        subq ON c.customer_id = subq.customer_id_b
        GROUP BY c.customer_id
        ;"""
        
    cursor.execute(sql_statement1)
    result1 = cursor.fetchall()
      
    print("  name                avg total price")
    for row in result1[:5]:
        print(row)

#task3
    try:
        customer_name='Perez and Sons'
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name=?",(customer_name,))
        customer_id=cursor.fetchall()[0][0]

        first_name='Miranda'
        last_name= 'Harris'
        cursor.execute("SELECT employee_id FROM employees WHERE first_name=? AND last_name=?",(first_name,last_name))
        employee_id=cursor.fetchall()[0][0]
    
        cursor.execute("SELECT product_id FROM products ORDER BY price LIMIT 5")
        product_ids=cursor.fetchall()

        cursor.execute("INSERT INTO orders (customer_id, employee_id) VALUES (?, ?) RETURNING order_id", (customer_id, employee_id))
        order_id=cursor.fetchall()[0][0]

        for prod_id in product_ids:
            cursor.execute("INSERT INTO line_items(order_id, product_id, quantity) VALUES (?, ?, 10)", (order_id, prod_id[0])) 

        cursor.execute(""" SELECT li.line_item_id, li.quantity, p.product_name
                        FROM line_items li
                        JOIN products p ON li.product_id=p.product_id
                        WHERE li.order_id=?;
                       """, (order_id,))
        result2 = cursor.fetchall()
        print("id    quant  name")
        for row in result2:
         print(row)
        conn.commit()

    except sqlite3.Error as e:
        print(f"Error: {e}")

#task4
    sql_statement2="""SELECT e.employee_id, e.first_name, e.last_name,
                    COUNT(o.order_id) AS order_count
                    FROM employees e
                    JOIN orders o ON e.employee_id=o.employee_id
                    GROUP BY e.employee_id
                    HAVING COUNT(o.order_id) > 5;"""
    cursor.execute(sql_statement2)
    result3=cursor.fetchall()

    print("e_id f_name  l_name o_count")
    for row in result3:
        print(row)