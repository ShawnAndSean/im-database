import random
import sqlite3
import string
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import simpledialog
from tkcalendar import Calendar
import customtkinter


class user:
    def __init__(self, root, shop_id):
        self.item_entries_name = None
        self.item_entries_values_list = None
        self.normalRating = None
        self.shop_id = shop_id
        self.entItemNormal = None
        self.entItemBad = None
        self.entItemGood = None
        self.entItemAve = None
        self.entItemStockAdded = None
        self.entItemSold = None
        self.entItemStockLeft = None
        self.entItemPrice = None
        self.entItemName = None
        self.entItemID = None
        self.asc = None
        self.desc = None
        self.search_box = None
        self.selected_delete = None
        self.selected_column = None
        self.selected_treeview = None
        self.item_records = None
        self.checkbox = None
        self.combobox_choice = None
        self.item_entries = []
        self.entItemID = None
        self.lblItemID = None
        self.root = root
        self.root.title("Retail Paradise User")
        self.root.geometry("1370x930")
        self.root.resizable(width=False, height=False)
        self.MainFrame = customtkinter.CTkFrame(self.root)
        self.MainFrame.grid(pady=30, padx=30)
        # Welcome Frame
        self.WelcomeFrame = customtkinter.CTkFrame(self.MainFrame, width=900, height=30)
        self.WelcomeFrame.grid(row=0, column=0, pady=10, padx=15, columnspan=2)
        # Item Form Frame
        self.FormFrame = customtkinter.CTkFrame(self.MainFrame, width=970, height=800)
        self.FormFrame.grid(row=1, column=0, pady=10, padx=15, sticky="w")
        self.assign_labels()
        self.call_item(0)
        # Treeview Form
        self.TreeviewFrame = customtkinter.CTkFrame(self.MainFrame, width=970, height=800)
        self.TreeviewFrame.grid(row=1, column=1, pady=10, padx=15, sticky="w")
        # Treeview Inner
        self.TreeviewInner = customtkinter.CTkFrame(self.TreeviewFrame)
        self.TreeviewInner.grid(row=1, column=1, pady=10, padx=15, sticky="w")
        self.treeview()
        # Sorterf
        self.SorterFrame = customtkinter.CTkFrame(self.TreeviewFrame, width=580, height=120)
        self.SorterFrame.grid(row=2, column=0, pady=10, padx=5, columnspan=2)
        self.sort()
        # Side Button Frames
        self.SideButtonFrame = customtkinter.CTkFrame(self.root, width=180, height=900)
        self.SideButtonFrame.grid(row=0, column=1, pady=10, columnspan=2)
        self.call_button_assignment()

    def assign_labels(self):
        item_label_text = ['Item Information', 'ID Number *', 'Name *', 'Price *',
                           'Stock Left *', 'Item Sold *', 'Stock Added *', 'Good Rating *',
                           'Bad Rating *', 'Normal Rating *']
        for item_index, item_text in enumerate(item_label_text, start=0):
            if item_index == 0:
                label = customtkinter.CTkLabel(self.FormFrame, text=item_text, width=160,
                                               height=50,
                                               fg_color=("lightblue", "#BB6464"),
                                               corner_radius=8, text_font=20)
                label.grid(row=0, column=0, sticky='nesw', padx=15, pady=20, columnspan=2)
            else:
                label = customtkinter.CTkLabel(self.FormFrame, text=item_text, width=160, height=40,
                                               fg_color=("white", "#205375"),
                                               corner_radius=8)
                label.grid(row=item_index, column=0, sticky=W, padx=15, pady=15)

    def call_item(self, value):
        self.entItemID = ''.join(random.choices(string.digits, k=4))
        self.lblItemID = customtkinter.CTkLabel(self.FormFrame, text=self.entItemID, width=250,
                                                height=40,
                                                fg_color=("lightblue", "#125B50"),
                                                corner_radius=8)
        self.lblItemID.grid(row=1, column=1, sticky=W, padx=15, pady=10)

        if value == 0:
            self.entItemID = ''.join(random.choices(string.digits, k=4))
        if value == 1:
            self.entItemID = self.shop_id

        self.item_entries = []
        self.item_entries_name = [
            self.entItemName,
            self.entItemPrice,
            self.entItemStockLeft,
            self.entItemSold,
            self.entItemStockAdded,
            self.entItemGood,
            self.entItemBad,
            self.normalRating
        ]
        for index in range(2, 10):
            item_entry = customtkinter.CTkEntry(self.FormFrame, width=250, height=40, justify='left')
            item_entry.grid(row=index, column=1, sticky=W, padx=15, pady=5)
            self.item_entries.append(item_entry)

        button = customtkinter.CTkButton(self.FormFrame, text="Add Item", width=250, fg_color='#CC704B', height=50, border_width=0, corner_radius=8,
                                         text_font=20, command=self.add_item_to_database)
        button.grid(row=10, column=0, padx=15, sticky='nesw', pady=20, columnspan=2)

    def call_button_assignment(self):
        button_text = ["Add Item", "Edit Profile", "Update", "Delete", "Refresh", "Exit"]
        button_function = [self.add_item_to_database, self.update_info, self.get_update, self.delete, self.refresh, self.exit]

        for index, (button_text, button_function) in enumerate(zip(button_text, button_function), start=0):
            button = customtkinter.CTkButton(self.SideButtonFrame, text=button_text, width=130, fg_color='#CC704B',
                                             height=70,
                                             border_width=2,
                                             corner_radius=8,
                                             command=button_function, text_font=30)
            button.grid(row=index, column=0, padx=15, sticky='nesw', pady=5)

    def add_item_to_database(self):
        self.item_entries_values_list = []
        for index, (entries, entries_name) in enumerate(zip(self.item_entries, self.item_entries_name)):
            entries_name = entries.get()
            self.item_entries_values_list.append(entries_name)
        for index in range(len(self.item_entries_values_list)):
            if len(self.item_entries_values_list[index]) == 0:
                tkinter.messagebox.showerror("Retailer's Paradise",
                                             "Please fill all forms for Items.")
                return
        for index, values in enumerate(self.item_entries_values_list):
            if index > 0 and not values.isdigit():
                tkinter.messagebox.showerror("Retailer's Paradise",
                                             "Please fill integers from price to normal rating.")
                return
            else:
                con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
                add_info_cursor = con.cursor()
                good = int(self.item_entries[5].get())
                bad = int(self.item_entries[6].get())
                normal = int(self.item_entries[7].get())

                good_weight = float(good) * 4.5
                bad_weight = float(bad) * 1.5
                normal_weight = float(normal) * 3

                max_weighted_score = (good + bad + normal) * 5
                total_weighted_score = (good_weight + bad_weight + normal_weight)

                average = str(round(total_weighted_score / max_weighted_score * 100, 2))
                add_info_cursor.execute(
                    "INSERT INTO item VALUES(:shop_id_number,:item_id_number,:item_name ,:item_price ,:item_stock ,:item_sold,:item_stock_added ,:ave_rating,:good_rating,:bad_rating ,:normal_rating   )",
                    {
                        'shop_id_number': self.shop_id,
                        'item_id_number': self.entItemID,
                        'item_name': self.item_entries_values_list[0],
                        'item_price': self.item_entries_values_list[1],
                        'item_stock': str(int(self.item_entries[2].get()) + int(self.item_entries[4].get())),
                        'item_sold': self.item_entries_values_list[3],
                        'item_stock_added': self.item_entries_values_list[4],
                        'ave_rating': average,
                        'good_rating': good,
                        'bad_rating': bad,
                        'normal_rating': normal,
                    }
                ),
                add_info_cursor.execute(
                    "INSERT INTO root VALUES(:shop_id_number,:item_id_number ,:ave_rating  ,:good_rating  ,:bad_rating ,:normal_rating)",
                    {
                        'shop_id_number': self.shop_id,
                        'item_id_number': self.entItemID,
                        'ave_rating': average,
                        'good_rating': good,
                        'bad_rating': bad,
                        'normal_rating': normal,
                    }
                )
                con.commit()
                con.close()
                tkinter.messagebox.showinfo("Retailer's Paradise",
                                            "Information Added.")
                self.refresh()
                return

    def update_item_to_database(self):
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        add_info_cursor = con.cursor()
        good = int(self.item_entries[5].get())
        bad = int(self.item_entries[6].get())
        normal = int(self.item_entries[7].get())

        good_weight = float(good) * 4.5
        bad_weight = float(bad) * 1.5
        normal_weight = float(normal) * 3

        max_weighted_score = (good + bad + normal) * 5
        total_weighted_score = (good_weight + bad_weight + normal_weight)

        average = str(round(total_weighted_score / max_weighted_score * 100, 2))
        add_info_cursor.execute("""
                                  UPDATE item SET
                                      item_id_number =:item_id_number,
                                      item_name =:item_name,
                                      item_price =:item_price,
                                      item_stock =:item_stock,
                                      item_sold =:item_sold,
                                      item_stock_added =:item_stock_added,
                                      ave_rating =:ave_rating,
                                      good_rating =:good_rating,
                                      bad_rating =:bad_rating,
                                      normal_rating =:normal_rating
                                      WHERE item_id_number =:item_id_number
                                  """, {
            'item_id_number': self.entItemID,
            'item_name': self.item_entries[0].get(),
            'item_price': self.item_entries[1].get(),
            'item_stock': str(int(self.item_entries[2].get()) + int(self.item_entries[4].get())),
            'item_sold': self.item_entries[3].get(),
            'item_stock_added': str(int(self.item_entries[4].get())),
            'ave_rating': average,
            'good_rating': good,
            'bad_rating': bad,
            'normal_rating': normal,
        }),
        add_info_cursor.execute("""
                                  UPDATE root SET
                                      ave_rating =:ave_rating,
                                      good_rating =:ave_rating,
                                      bad_rating =:bad_rating,
                                      normal_rating =:normal_rating
                                      WHERE item_id_number =:item_id_number
                                  """, {
            'item_id_number':  self.entItemID,
            'ave_rating': average,
            'good_rating': good,
            'bad_rating': bad,
            'normal_rating': normal,
        })
        con.commit()
        con.close()
        tkinter.messagebox.showinfo("Retailer's Paradise",
                                    "Information Updated.")

    def treeview(self):

        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        item_cursor = con.cursor()
        item_cursor.execute("SELECT * FROM item "
                            "WHERE shop_id_number="+str(self.shop_id)+
                            f" ORDER BY item_id_number DESC" )

        root_column = ['shopID', 'itemID', 'itemName', 'itemPrice', 'stockLeft', 'itemSold', 'stockAdded',
                       'aveRating',
                       'goodRating', 'badRating', 'normalRating']
        root_name = ['Shop ID', 'Item ID', ' Name', ' Price', 'Stock Left', 'Item Sold',
                     'Stock Added',
                     'Average Rating', 'Good Rating', 'Bad Rating', 'Normal Rating']

        self.scroll_y = Scrollbar(self.TreeviewInner, orient=VERTICAL)
        self.root_column = root_column
        self.root_names = root_name
        self.records = ttk.Treeview(self.TreeviewInner, height=31, columns=self.root_column,
                                    yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.records['show'] = 'headings'

        for (root_id, text) in zip(self.root_column, self.root_names):
            self.records.column(root_id, width=50, anchor=CENTER)
            self.records.heading(root_id, text=text)

        self.records.pack(fill=BOTH, expand=1, anchor=CENTER)

        root_records = item_cursor.fetchall()
        if len(root_records) != 0:
            # for all rows in root records, insert all the values of the databased towards its end
            for row in root_records:
                self.records.insert('', END, values=row)

        self.lblItemID = customtkinter.CTkLabel(self.FormFrame, text=self.entItemID, width=250,
                                                height=40,
                                                fg_color=("lightblue", "#125B50"),
                                                corner_radius=8)
        self.lblItemID.grid(row=1, column=1, sticky=W, padx=15, pady=10)

    def sort(self):
        item_label_text = ['ID Number ', 'Name', 'Price',
                           'Stock Left ', 'Item Sold', 'Stock Added', 'Good Rating',
                           'Bad Rating ', 'Normal Rating']
        label = customtkinter.CTkLabel(self.SorterFrame, text="Sort By Price:", width=120,
                                       height=30,
                                       fg_color=("lightblue", "#BB6464"),
                                       corner_radius=8, text_font=20)
        label.grid(row=0, column=0, sticky='nesw', padx=8, pady=8)

        self.combobox_choice = None

        checkbox_asc = customtkinter.CTkCheckBox(self.SorterFrame, text="ASC", variable=self.asc, command=self.sort_function_combobox_asc, width=50)
        checkbox_asc.grid(row=0, column=1, sticky='e', padx=8, pady=8)
        checkbox_desc = customtkinter.CTkCheckBox(self.SorterFrame, text="DESC", variable=self.desc, command=self.sort_function_combobox_desc,
                                                  width=50)
        checkbox_desc.grid(row=0, column=1, sticky='w', padx=8, pady=8)

        label = customtkinter.CTkLabel(self.SorterFrame, text="Search:", width=120,
                                       height=30,
                                       fg_color=("lightblue", "#BB6464"),
                                       corner_radius=8, text_font=20)
        label.grid(row=1, column=0, sticky='nesw', padx=8, pady=8)

        self.search_box = customtkinter.CTkEntry(self.SorterFrame, width=330, height=30, justify='left')
        self.search_box.grid(row=1, column=1, sticky=W, padx=8, pady=5, columnspan=2)

        button = customtkinter.CTkButton(self.SorterFrame, text="Apply", width=100, fg_color='#CC704B',
                                         height=30,
                                         border_width=2,
                                         corner_radius=8,
                                         command=self.search, text_font=30)
        button.grid(row=1, column=3, padx=5, sticky='w', pady=5)

    def search(self):
        for widget in self.TreeviewInner.winfo_children():
            widget.destroy()
        search = self.search_box.get()
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        search_cursor = con.cursor()
        search_cursor.execute(
            "SELECT * FROM item WHERE item_name LIKE ? AND shop_id_number="+str(self.shop_id), (f'%{search}%',)
        )
        root_column = ['shopID', 'itemID', 'itemName', 'itemPrice', 'stockLeft', 'itemSold', 'stockAdded',
                       'aveRating',
                       'goodRating', 'badRating', 'normalRating']
        root_name = ['Shop ID', 'Item ID', ' Name', ' Price', 'Stock Left', 'Item Sold',
                     'Stock Added',
                     'Average Rating', 'Good Rating', 'Bad Rating', 'Normal Rating']

        self.scroll_y = Scrollbar(self.TreeviewInner, orient=VERTICAL)
        self.root_column = root_column
        self.root_names = root_name
        self.records = ttk.Treeview(self.TreeviewInner, height=31, columns=self.root_column,
                                    yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.records['show'] = 'headings'

        for (root_id, text) in zip(self.root_column, self.root_names):
            self.records.column(root_id, width=50, anchor=CENTER)
            self.records.heading(root_id, text=text)

        self.records.pack(fill=BOTH, expand=1, anchor=CENTER)

        root_records = search_cursor.fetchall()
        if len(root_records) != 0:
            # for all rows in root records, insert all the values of the databased towards its end
            for row in root_records:
                self.records.insert('', END, values=row)

        self.lblItemID = customtkinter.CTkLabel(self.FormFrame, text=self.entItemID, width=250,
                                                height=40,
                                                fg_color=("lightblue", "#125B50"),
                                                corner_radius=8)
        self.lblItemID.grid(row=1, column=1, sticky=W, padx=15, pady=10)
        search_items = search_cursor.fetchall()
        print(search_items)

    def get_update(self):
        self.selected_treeview = self.records.focus()
        self.selected_column = self.records.item(self.selected_treeview, 'values')
        self.entItemID = self.selected_column[1]
        self.lblItemID = customtkinter.CTkLabel(self.FormFrame, text=self.entItemID, width=250,
                                                height=40,
                                                fg_color=("lightblue", "#125B50"),
                                                corner_radius=8)
        self.lblItemID.grid(row=1, column=1, sticky=W, padx=15, pady=10)
        self.item_entries[0].insert(0, self.selected_column[2])
        self.item_entries[1].insert(0, self.selected_column[3])
        self.item_entries[2].insert(0, self.selected_column[4])
        self.item_entries[3].insert(0, self.selected_column[5])
        self.item_entries[4].insert(0, self.selected_column[6])
        self.item_entries[5].insert(0, self.selected_column[8])
        self.item_entries[6].insert(0, self.selected_column[9])
        self.item_entries[7].insert(0, self.selected_column[10])

        button = customtkinter.CTkButton(self.FormFrame, text="Update Item", width=250, fg_color='#CC704B', height=50, border_width=0,
                                         corner_radius=8,
                                         text_font=20, command=self.update_item_to_database)
        button.grid(row=10, column=0, padx=15, sticky='nesw', pady=20, columnspan=2)

    def delete(self):
        self.selected_treeview = self.records.focus()
        self.selected_column = self.records.item(self.selected_treeview, 'values')
        self.item_entries[0].insert(0, self.selected_column[2])
        self.item_entries[1].insert(0, self.selected_column[3])
        self.item_entries[2].insert(0, self.selected_column[4])
        self.item_entries[3].insert(0, self.selected_column[5])
        self.item_entries[4].insert(0, self.selected_column[6])
        self.item_entries[5].insert(0, self.selected_column[8])
        self.item_entries[6].insert(0, self.selected_column[9])
        self.item_entries[7].insert(0, self.selected_column[10])

        self.entItemID = self.selected_column[1]
        self.lblItemID = customtkinter.CTkLabel(self.FormFrame, text=self.entItemID, width=250,
                                                height=40,
                                                fg_color=("lightblue", "#125B50"),
                                                corner_radius=8)
        self.lblItemID.grid(row=1, column=1, sticky=W, padx=15, pady=10)

        button = customtkinter.CTkButton(self.FormFrame, text="Delete Item", width=250, fg_color='#CC704B', height=50, border_width=0,
                                         corner_radius=8,
                                         text_font=20, command=self.delete_from_database)
        button.grid(row=10, column=0, padx=15, sticky='nesw', pady=20, columnspan=2)

    def delete_from_database(self):
        self.selected_delete = self.records.selection()[0]
        self.records.delete(self.selected_delete)
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        delete_cursor = con.cursor()
        delete_cursor.execute("DELETE from item WHERE item_id_number= " + str(self.selected_column[1]))
        tkinter.messagebox.showinfo("Deleted Membership", "Item Deleted.")
        con.commit()
        con.close()

    def refresh(self):
        self.entItemID = ''.join(random.choices(string.digits, k=4))
        self.lblItemID = customtkinter.CTkLabel(self.FormFrame, text=self.entItemID, width=250,
                                                height=40,
                                                fg_color=("lightblue", "#125B50"),
                                                corner_radius=8)
        self.lblItemID.grid(row=1, column=1, sticky=W, padx=15, pady=10)
        button = customtkinter.CTkButton(self.FormFrame, text="Add Item", width=250, fg_color='#CC704B', height=50, border_width=0, corner_radius=8,
                                         text_font=20, command=self.add_item_to_database)
        button.grid(row=10, column=0, padx=15, sticky='nesw', pady=20, columnspan=2)

        for entries in self.item_entries:
            entries.delete(0, END)

        self.sort_function_combobox_desc()

    def sort_function_combobox_asc(self):
        for widget in self.TreeviewInner.winfo_children():
            widget.destroy()
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        item_cursor = con.cursor()
        item_cursor.execute("SELECT * FROM item WHERE shop_id_number="+str(self.shop_id)+" ORDER BY item_price ASC")

        root_column = ['shopID', 'itemID', 'itemName', 'itemPrice', 'stockLeft', 'itemSold', 'stockAdded',
                       'aveRating',
                       'goodRating', 'badRating', 'normalRating']
        root_name = ['Shop ID', 'Item ID', ' Name', ' Price', 'Stock Left', 'Item Sold',
                     'Stock Added',
                     'Average Rating', 'Good Rating', 'Bad Rating', 'Normal Rating']

        self.scroll_y = Scrollbar(self.TreeviewInner, orient=VERTICAL)
        self.root_column = root_column
        self.root_names = root_name
        self.records = ttk.Treeview(self.TreeviewInner, height=31, columns=self.root_column,
                                    yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.records['show'] = 'headings'

        for (root_id, text) in zip(self.root_column, self.root_names):
            self.records.column(root_id, width=50, anchor=CENTER)
            self.records.heading(root_id, text=text)

        self.records.pack(fill=BOTH, expand=1, anchor=CENTER)

        root_records = item_cursor.fetchall()
        if len(root_records) != 0:
            # for all rows in root records, insert all the values of the databased towards its end
            for row in root_records:
                self.records.insert('', END, values=row)

        self.lblItemID = customtkinter.CTkLabel(self.FormFrame, text=self.entItemID, width=250,
                                                height=40,
                                                fg_color=("lightblue", "#125B50"),
                                                corner_radius=8)
        self.lblItemID.grid(row=1, column=1, sticky=W, padx=15, pady=10)
        con.commit()
        con.close()

    def sort_function_combobox_desc(self):
        for widget in self.TreeviewInner.winfo_children():
            widget.destroy()
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        item_cursor = con.cursor()
        item_cursor.execute("SELECT * FROM item "
                            "WHERE shop_id_number="+str(self.shop_id)+
                            " ORDER BY item_price DESC ")

        root_column = ['shopID', 'itemID', 'itemName', 'itemPrice', 'stockLeft', 'itemSold', 'stockAdded',
                       'aveRating',
                       'goodRating', 'badRating', 'normalRating']
        root_name = ['Shop ID', 'Item ID', ' Name', ' Price', 'Stock Left', 'Item Sold',
                     'Stock Added',
                     'Average Rating', 'Good Rating', 'Bad Rating', 'Normal Rating']

        self.scroll_y = Scrollbar(self.TreeviewInner, orient=VERTICAL)
        self.root_column = root_column
        self.root_names = root_name
        self.records = ttk.Treeview(self.TreeviewInner, height=31, columns=self.root_column,
                                    yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.records['show'] = 'headings'

        for (root_id, text) in zip(self.root_column, self.root_names):
            self.records.column(root_id, width=50, anchor=CENTER)
            self.records.heading(root_id, text=text)

        self.records.pack(fill=BOTH, expand=1, anchor=CENTER)

        root_records = item_cursor.fetchall()
        if len(root_records) != 0:
            # for all rows in root records, insert all the values of the databased towards its end
            for row in root_records:
                self.records.insert('', END, values=row)

        self.lblItemID = customtkinter.CTkLabel(self.FormFrame, text=self.entItemID, width=250,
                                                height=40,
                                                fg_color=("lightblue", "#125B50"),
                                                corner_radius=8)
        self.lblItemID.grid(row=1, column=1, sticky=W, padx=15, pady=10)
        con.commit()
        con.close()
    def update_info(self):
        from login import login
        root = customtkinter.CTk()
        self.admin = login(root, self.shop_id)
        root.mainloop()

    def exit(self):
        ask_exit = tkinter.messagebox.askyesno("Retailer's Paradise",
                                               "Are you sure you want to close the program?")
        if ask_exit == 1:
            self.root.destroy()
            return


if __name__ == '__main__':
    root = customtkinter.CTk()
    application = user(root)
    root.mainloop()
