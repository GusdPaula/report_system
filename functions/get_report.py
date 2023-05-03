import sqlite3
import pandas as pd
import os

PATH_DB = str(os.getcwd()).replace('/functions', "") + '/database/products.db'
PATH_REPORT = str(os.getcwd()).replace('/functions', "") + "/reports"

def get_report(start_date, end_date):
    '''
    This will generate an excel report for a specif date range.

    '''

    # Doing the query
    conn = sqlite3.connect(PATH_DB)
    cursor = conn.cursor()
    cursor.execute("""SELECT shopping.id, 
    shopping.date, 
    shopping.product_id, 
    product.name, 
    shopping.price, 
    shopping.amount, 
    shopping.total 
    FROM shopping INNER JOIN product ON shopping.product_id = product.id 
    WHERE shopping.date BETWEEN ? AND ?""", (start_date, end_date))
    
    data = cursor.fetchall()
    conn.close()

    # Saving the query
    df = pd.DataFrame(data, columns=['id', 'date', 'product_id', 'product_name', 'price', 'amount', 'total'])
    file_name = PATH_REPORT + '\products_report.xlsx'
    df.to_excel(file_name, index=None)
    