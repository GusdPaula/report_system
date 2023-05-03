import pandas as pd
from tkinter import filedialog, messagebox
import sqlite3
import os

PATH = str(os.getcwd()).replace('/functions', "") + '/database/products.db'

class Product:
    '''
    Class to help to insert new products into products table.

    '''
    def __init__(self, name) -> None:
        # Connect to the database (create it if it doesn't exist)
        conn = sqlite3.connect(PATH)

        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()

        # Searching if the name already exist
        cursor.execute("""SELECT id FROM product WHERE name = ?""", (name,))
        id = cursor.fetchone()

        if id is None:
            cursor.execute("""INSERT INTO product (name) VALUES (?)""", (name,))
            conn.commit()
            cursor.execute("""SELECT id FROM product WHERE name = ?""", (name,))
            id = cursor.fetchone()

        cursor.close()

        self.id = id[0]

def insert_new_products():
    '''
    This function will insert new products into Products DB.

    '''

    # Getting the excel file
    # Open a file dialog to select an Excel file
    filepath = filedialog.askopenfilename(title="Select Excel file", filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*")))
    if not filepath:
        return

    try:
        df = pd.read_excel(filepath)

        # Convert the date column to datetime format
        df['date'] = pd.to_datetime(df['date'])

        # Convert the date column to 'dd-mm-yyyy' format
        df['date'] = df['date'].dt.strftime('%d-%m-%Y')

        
        for i in range(len(df)):
            # Getting the data to insert into DB
            row = df.iloc[i]
            date = row["date"]
            name = row["name"]
            product = Product(name).id

            while True:
                # This will catch if the values are not numbers
                try:
                    amount = float(row["amount"])
                    price = float(row["price"])
                    total = amount * price
                    break
                
                except ValueError:
                    print('\nUse only numbers to amount and price, please...\n')
                

            # Adding the values into shopping table
            # Connect to the database (create it if it doesn't exist)
            conn = sqlite3.connect(PATH)

            # Create a cursor object to execute SQL commands
            cursor = conn.cursor()

            # Inserting values
            cursor.execute("""INSERT INTO shopping (date, product_id, price, amount, total) VALUES (?, ?, ?, ?, ?)""", (date, product, price, amount, total))
            conn.commit()

        cursor.close()
        
        # Show a message box to indicate that the data was inserted successfully
        messagebox.showinfo("Success", "Data inserted successfully!")

    except Exception as insert_error:
        # Show an error message if there was an error inserting the data
        messagebox.showerror("Error", f"Error inserting data: {str(insert_error)}")
    

if __name__ == '__main__':
    insert_new_products()
