import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT li.line_item_id,
           li.quantity,
           li.product_id,
           p.product_name,
           p.price
    FROM line_items li
    JOIN products p
    ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head(5))

df['total'] = df['quantity'] * df['price']
print(df.head(5))  

group_df=df.groupby('product_id').agg({'line_item_id':'count','total':'sum', 'product_name':'first'})
print(group_df.head(5))

sort_df=group_df.sort_values(by='product_name')
#not required, printing for debugging
print(sort_df.head(5))

sort_df.to_csv("order_summary.csv", index=False)