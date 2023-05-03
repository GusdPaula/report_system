import tkinter as tk
from functions import get_report, create_data_base, insert_data

# Define the function to export data to a file
def export_data(start_date, end_date):
    # Code to export data goes here
    get_report.get_report(start_date, end_date)

# Define the function to insert data into a database
def insert_data_to_button():
    # Code to insert data into a database goes here
    insert_data.insert_new_products()

# Define the function to calculate the total amount of purchases
def calculate_total(start_date, end_date):
    # Code to calculate the total amount of purchases goes here
    total = 0
    return total

# Define the function to handle the "Export" button click event
def export_button_click():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    export_data(start_date, end_date)

# Define the function to handle the "Insert" button click event
def insert_button_click():
    insert_data_to_button()


# Creating the DataBase
create_data_base.create_products_table()
create_data_base.create_shopping_table()

# Create the main window
window = tk.Tk()

# Set the size of the window
window.geometry("400x250")

# Add a title to the window
window.title("Purchase Summary")

# Add a label for the start date entry
start_date_label = tk.Label(window, text="Start Date:")
start_date_label.pack(padx=10, pady=10)

# Add an entry for the start date
start_date_entry = tk.Entry(window)
start_date_entry.pack(padx=10, pady=5)

# Add a label for the end date entry
end_date_label = tk.Label(window, text="End Date:")
end_date_label.pack(padx=10, pady=10)

# Add an entry for the end date
end_date_entry = tk.Entry(window)
end_date_entry.pack(padx=10, pady=5)

# Add a button to export data
export_button = tk.Button(window, text="Export", command=export_button_click)
export_button.pack(padx=10, pady=10)

# Add a button to insert data into a database
insert_button = tk.Button(window, text="Insert", command=insert_button_click)
insert_button.pack(padx=10, pady=10)

# Run the main event loop
window.mainloop()