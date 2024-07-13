import tkinter as tk
from tkinter import ttk

def Check_tot():
    Price = float(item_price_text.get())
    quantity = float(item_quantity_text.get())
    total = Price*quantity
    item_total_text.delete(0, tk.END)
    item_total_text.insert(0,total)

def add():
    grand_tot = 0
    item = item_name_text.get()
    price = item_price_text.get()
    quantity = item_quantity_text.get()
    total = item_total_text.get()

    table.insert('', tk.END, values=(item,price,quantity,total))

    item_name_text.delete(0,tk.END)
    item_price_text.delete(0,tk.END)
    item_quantity_text.delete(0,tk.END)
    item_total_text.delete(0,tk.END)

    for items in table.get_children():
        value = table.item(items, 'values')
        ind_tot = float(value[3])
        print(ind_tot)
        grand_tot += ind_tot
        g_total.configure(text=f'Total: {grand_tot}')



root = tk.Tk()
root.title('Billing System')
main_title = tk.Label(root, text='Billing System', font=('Arial',40),fg='white',bg='black')
main_title.pack(pady=10)
root.geometry('810x500')
root.resizable(False,False)

frm = tk.Frame(root)
frm.pack()

for col in range(4):
    frm.columnconfigure(col, minsize=200)

#Labels

item_name = tk.Label(frm, text='Item Name', font=('Arial bold',15))
item_name.grid(row=0,column=0)

item_price = tk.Label(frm, text='Price', font=('Arial bold',15))
item_price.grid(row=0, column=1)

item_quantity = tk.Label(frm, text='Quantity', font=('Arial bold',15))
item_quantity.grid(row=0, column=2)

item_total = tk.Label(frm, text='Total', font=('Arial bold',15))
item_total.grid(row=0, column=3)

#Entry

item_name_text = tk.Entry(frm, width=15, font=('Arial',15))
item_name_text.grid(row=1,column=0)

item_price_text = tk.Entry(frm, width=15, font=('Arial',15), justify='right')
item_price_text.grid(row=1,column=1)

item_quantity_text = tk.Entry(frm, width=15, font=('Arial',15), justify='right')
item_quantity_text.grid(row=1,column=2)

item_total_text = tk.Entry(frm, width=15, font=('Arial',15), justify='right')
item_total_text.grid(row=1,column=3)

#Button

bt_total = tk.Button(frm, text="Check Total" ,width=10, font=('Arial bold',15),bg='#33ccff', command=Check_tot)
bt_total.grid(row=2,column=2,pady=10)

bt_add = tk.Button(frm, text="Add" ,width=10, font=('Arial bold',15),bg='#00ff00', command=add)
bt_add.grid(row=2,column=3,pady=10)

#table

table = ttk.Treeview(frm, columns=('item','price','qt','tot'), show='headings')
table.grid(row=3, column=0, columnspan=4)

table.heading('#1', text='Item')
table.heading('#2', text='Price')
table.heading('#3', text='Quantity')
table.heading('#4', text='Total')

g_total = tk.Label(root, text='Grand Total: ', fg='#00ff00', width=10, font=('Arial bold', 20))
g_total.pack(pady=11)
root.mainloop()