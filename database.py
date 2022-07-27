import random
import sqlite3
import string
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import simpledialog
from tkcalendar import Calendar
import customtkinter


class app:
    def __init__(self, root):
        self.owner_entries_values_list = None
        self.item_entries_values_list = None
        self.shop_entries_values_list = None
        self.owners_entries_values_list = None
        self.proceed = None
        self.shop_update_list = None
        self.owner_entries_name = None
        self.lblOwnerID = None
        self.lblShopIDMirror = None
        self.OwnerID = None
        self.lblDate = None
        self.lblItemID = None
        self.btnAddNewItem = None
        self.search_item_root_names = None
        self.search_item_root_column = None
        self.search_owner_root_names = None
        self.search_shop_root_names = None
        self.search_shop_root_column = None
        self.search_owner_root_column = None
        database = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        c = database.cursor()
        c.execute("""
                        CREATE TABLE IF NOT EXISTS shop(
                            shop_id_number INT NOT NULL,
                            shop_name VARCHAR(30) NOT NULL,
                            shop_location VARCHAR(50) NOT NULL,
                            shop_followers INT(5) DEFAULT 0,
                            ave_response DECIMAL(3) DEFAULT 0,
                            ownerID DECIMAL(20) NOT NULL,
                            PRIMARY KEY(shop_id_number)
                        )""")
        c.execute("""
                        CREATE TABLE IF NOT EXISTS item(
                            shop_id_number INT NOT NULL,
                            item_id_number INT NOT NULL,
                            item_name VARCHAR(30) NOT NULL,
                            item_price VARCHAR(5) DEFAULT 0,
                            item_stock INT(5) DEFAULT 0,
                            item_sold DECIMAL(3) DEFAULT 0,
                            item_stock_added DECIMAL(5) NOT NULL,
                            ave_rating INT NOT NULL,
                            good_rating INT NOT NULL,
                            bad_rating INT NOT NULL,
                            normal_rating INT NOT NULL,
                            PRIMARY KEY(shop_id_number,item_id_number)
                        )"""),
        c.execute("""
                        CREATE TABLE IF NOT EXISTS owner(
                            shop_id_number INT NOT NULL,
                            owner_id_number INT NOT NULL,
                            owner_first_name VARCHAR(30) NOT NULL,
                            owner_middle_name VARCHAR(30) NOT NULL,
                            owner_surname VARCHAR(30) NOT NULL,
                            owner_phone_number INT NOT NULL,
                            owner_email VARCHAR(50) ,
                            owner_date_joined VARCHAR(10),
                            PRIMARY KEY(shop_id_number,owner_id_number)
                )"""),
        c.execute("""
                        CREATE TABLE IF NOT EXISTS root(
                            shop_id_number INT NOT NULL,
                            item_id_number INT NOT NULL,
                            ave_rating INT NOT NULL,
                            good_rating INT NOT NULL,
                            bad_rating INT NOT NULL,
                            normal_rating INT NOT NULL,
                            PRIMARY KEY(shop_id_number, item_id_number)
                )""")
        database.commit()
        database.close()
        self.search_width = None
        self.button_function = None
        self.button_text = None
        self.date_editor_id_record = None
        self.owner_editor_id = None
        self.item_records = None
        self.owner_records = None
        self.choose_search_record = None
        self.search_item_records = None
        self.search_owner_records = None
        self.search_shop_records = None
        self.deleteID = None
        self.shopId = None
        self.entOwnerID = None
        self.entOwnerNameLast = None
        self.entOwnerNameFirst = None
        self.entOwnerNameMiddle = None
        self.entOwnerPhone = None
        self.entOwnerEmail = None
        self.shop_records = None
        self.updateID = None
        self.searchID = None
        self.entShopID = None
        self.entShopAverageResponseRate = None
        self.entShopFollowerCount = None
        self.entShopLocation = None
        self.entShopName = None
        self.entShopIDMirror = None
        self.isShopId = None
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
        self.normalRating = IntVar()
        self.addItem = None
        self.root = root
        self.root.title("Retail Paradise Admin")
        self.root.geometry("1800x950")
        self.root.resizable(width=False, height=False)
        self.MainFrame = customtkinter.CTkFrame(self.root, width=1330, height=600)
        self.MainFrame.grid(pady=30, padx=30)

        self.TableLabel = customtkinter.CTkLabel(self.MainFrame, text='Form', width=160,
                                                 height=25,
                                                 fg_color=("lightblue", "#4D4C7D"),
                                                 corner_radius=8)
        self.TableLabel.grid(row=0, column=0, sticky='nesw', padx=5, pady=2)

        self.TableLabel = customtkinter.CTkLabel(self.MainFrame, text='Database', width=160,
                                                 height=25,
                                                 fg_color=("lightblue", "#4D4C7D"),
                                                 corner_radius=8)
        self.TableLabel.grid(row=0, column=1, sticky='nesw', padx=5, pady=2)

        self.FormFrame = customtkinter.CTkFrame(self.MainFrame, width=900, height=800,
                                                )
        self.FormFrame.grid(row=1, column=0, pady=20, padx=15)

        self.TreeviewFrame = customtkinter.CTkFrame(self.MainFrame, width=450, height=800,
                                                    )
        self.TreeviewFrame.grid(row=1, column=1, pady=20, padx=20)

        self.TableLabel = customtkinter.CTkLabel(self.MainFrame, text='Buttons', width=160,
                                                 height=25,
                                                 fg_color=("lightblue", "#4D4C7D"),
                                                 corner_radius=8)
        self.TableLabel.grid(row=2, column=0, sticky='nesw', padx=5, pady=2, columnspan=2)

        self.ButtonFrame = customtkinter.CTkFrame(self.MainFrame, width=1320, height=800)
        self.ButtonFrame.grid(row=3, column=0, columnspan=2, pady=10, padx=15)

        self.ShopName = StringVar()
        self.ShopLocation = StringVar()
        self.ShopFollowerCount = IntVar()
        self.ShopAveResponseRate = IntVar()

        self.OwnerFirstName = StringVar()
        self.OwnerLastName = StringVar()
        self.OwnerMiddleName = StringVar()
        self.OwnerPhoneNumber = StringVar()
        self.OwnerEmail = StringVar()

        self.ItemName = StringVar()
        self.ItemPrice = IntVar()
        self.ItemStock = IntVar()
        self.ItemSold = IntVar()
        self.ItemStockAdded = IntVar()

        self.aveRating = IntVar()
        self.goodRating = IntVar()
        self.badRating = IntVar()
        self.normalRating = IntVar()

        self.root_column = ['shopID', 'itemID', 'aveRating', 'goodRating', 'badRating', 'normalRating']
        self.root_names = ['Shop ID', 'Item ID', 'Average Rating', 'Good Rating', 'Bad Rating', 'Normal Rating']

        self.scroll_y = Scrollbar(self.TreeviewFrame, orient=VERTICAL)
        self.records = ttk.Treeview(self.TreeviewFrame, height=31, columns=self.root_column,
                                    yscrollcommand=self.scroll_y.set)

        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.records['show'] = 'headings'

        for (root_id, text) in zip(self.root_column, self.root_names):
            self.records.column(root_id, width=135)
            self.records.heading(root_id, text=text)

        self.records.pack(fill=BOTH, expand=1, anchor=CENTER)

        self.call_item(self.FormFrame, 2, 3, 0)
        self.call_shop(self.FormFrame, 1, 0)
        self.call_owner(self.FormFrame, 0, 0)
        self.call_button_assignment()
        self.show_summary()

    def call_treeview_summary(self, root_column, root_name, width):
        self.records.pack_forget()
        self.scroll_y.pack_forget()
        self.scroll_y = Scrollbar(self.TreeviewFrame, orient=VERTICAL)
        self.root_column = root_column
        self.root_names = root_name
        self.records = ttk.Treeview(self.TreeviewFrame, height=31, columns=self.root_column,
                                    yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.records['show'] = 'headings'

        for (root_id, text) in zip(self.root_column, self.root_names):
            self.records.column(root_id, width=width, anchor=CENTER)
            self.records.heading(root_id, text=text)

        self.records.pack(fill=BOTH, expand=1, anchor=CENTER)

    def call_shop(self, frame, label_column, edit):
        if edit == 0:
            self.entShopID = ''.join(random.choices(string.digits, k=4))
        if edit == 1:
            self.entShopID = self.updateID
        self.shopId = customtkinter.CTkLabel(frame, text=self.entShopID, width=160,
                                             height=25,
                                             fg_color=("lightblue", "#125B50"),
                                             corner_radius=8)
        self.shopId.grid(row=1, column=label_column, sticky=W, padx=5, pady=10)

        label_text = ['Shop Information', 'Shop ID *', 'Shop Name *', 'Location *', 'Follower Count',
                      'Average Response Rate']

        for index, text in enumerate(label_text, start=0):
            if index == 0:
                label = customtkinter.CTkLabel(frame, text=text, width=160,
                                               height=25,
                                               fg_color=("lightblue", "#BB6464"),
                                               corner_radius=8)
                label.grid(row=index, column=0, sticky=W, padx=5, pady=10)
            else:
                label = customtkinter.CTkLabel(frame, text=text, width=160, height=25,
                                               fg_color=("white", "#205375"),
                                               corner_radius=8)
                label.grid(row=index, column=0, sticky=W, padx=5, pady=5)
        self.shop_entries = []
        self.shop_entries_name = [
            self.entShopID,
            self.entShopName,
            self.entShopLocation,
            self.entShopFollowerCount,
            self.entShopAverageResponseRate,
        ]
        for index in range(2, 6):
            shop_entry = customtkinter.CTkEntry(frame, width=250, justify='left')
            shop_entry.grid(row=index, column=1, sticky=W, padx=5, pady=5)
            self.shop_entries.append(shop_entry)

    def call_item(self, frame, label_column, entry_column, edit):
        if edit == 0:
            self.entItemID = ''.join(random.choices(string.digits, k=4))
        if edit == 1:
            self.entItemID = self.updateID

        self.lblItemID = customtkinter.CTkLabel(frame, text=self.entItemID, width=160,
                                                height=25,
                                                fg_color=("lightblue", "#125B50"),
                                                corner_radius=8)
        self.lblItemID.grid(row=1, column=entry_column, sticky=W, padx=5, pady=10)

        item_label_text = ['Item Information', 'ID Number *', 'Name *', 'Price *',
                           'Stock Left *', 'Item Sold *', 'Stock Added *', 'Good Rating *',
                           'Bad Rating *', 'Normal Rating *']
        for item_index, item_text in enumerate(item_label_text, start=0):
            if item_index == 0:
                label = customtkinter.CTkLabel(frame, text=item_text, width=160, height=25, fg_color=("lightblue", "#BB6464"), corner_radius=8)
                label.grid(row=item_index, column=label_column, sticky=W, padx=5, pady=10)
            else:
                label = customtkinter.CTkLabel(frame, text=item_text, width=160, height=25, fg_color=("white", "#205375"), corner_radius=8)
                label.grid(row=item_index, column=label_column, sticky=W, padx=5, pady=5)

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
            item_entry = customtkinter.CTkEntry(frame, width=250, justify='left')
            item_entry.grid(row=index, column=entry_column, sticky=W, padx=5, pady=5)
            self.item_entries.append(item_entry)

    def call_owner(self, frame, label_column, edit):
        if edit == 0:
            self.entOwnerID = ''.join(random.choices(string.digits, k=4))
            self.cal = Calendar(frame, selectmode='day', year=2020, month=5, day=22)
            self.cal.grid(row=13, column=1, sticky=W, padx=5, pady=20)
        if edit == 1:
            self.entOwnerID = self.updateID

        label_text = ['Owner Information', 'Owner ID *', 'First Name *', 'Middle Name',
                      'Last Name *', 'Phone Number *', 'Email', 'Date Joined']

        self.OwnerID = customtkinter.CTkLabel(frame, text=self.entOwnerID, width=160,
                                              height=25,
                                              fg_color=("lightblue", "#125B50"),
                                              corner_radius=8)
        self.OwnerID.grid(row=7, column=1, sticky=W, padx=5, pady=5)
        for owner_index, owner_text in enumerate(label_text, start=0):
            if owner_index == 0:
                label = customtkinter.CTkLabel(frame, text=owner_text, width=160,
                                               height=25,
                                               fg_color=("lightblue", "#BB6464"),
                                               corner_radius=8)
                label.grid(row=owner_index + 6, column=label_column, sticky=W, padx=5, pady=10)
            else:
                label = customtkinter.CTkLabel(frame, text=owner_text, width=160, height=25,
                                               fg_color=("white", "#205375"),
                                               corner_radius=8)
                label.grid(row=owner_index + 6, column=label_column, sticky=W, padx=5, pady=5)

        self.owner_entries = []
        self.owner_entries_name = [
            self.entOwnerNameFirst,
            self.entOwnerNameMiddle,
            self.entOwnerNameLast,
            self.entOwnerPhone,
            self.entOwnerEmail,
        ]

        for index in range(8, 13):
            owner_entry = customtkinter.CTkEntry(frame, width=250, justify='left')
            owner_entry.grid(row=index, column=1, sticky=W, padx=5, pady=5)
            self.owner_entries.append(owner_entry)

    def search(self):
        self.searchID = tkinter.simpledialog.askinteger("Search Membership",
                                                        "ENTER SHOP ID:\t\t\t\t\t")
        print(self.searchID)
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        select_cursor = con.cursor()
        select_cursor.execute("SELECT * from shop where shop_id_number=" + str(self.searchID))
        self.search_shop_records = select_cursor.fetchall()
        print(self.search_shop_records)
        select_cursor.execute("SELECT * from owner where shop_id_number=" + str(self.searchID))
        self.search_owner_records = select_cursor.fetchall()
        select_cursor.execute("SELECT * from item where shop_id_number=" + str(self.searchID) + " ORDER BY item_price DESC")
        self.search_item_records = select_cursor.fetchall()
        if self.searchID is not None:
            if len(self.search_shop_records) != 0:
                self.search_shop_root_column = ['shopID', 'shopName', 'shopLocation', 'shopFollower',
                                                'shopAverageResponse',
                                                'OwnerID']
                self.search_shop_root_names = ['Shop ID', ' Name', ' Location', 'Followers', 'Average Response Rate',
                                               'Owner ID']
            if len(self.search_owner_records) != 0:
                self.search_owner_root_column = ['shopID', 'ownerID', 'ownerFirst', 'ownerMiddle', 'ownerSurname', 'ownerPhone', 'ownerEmail',
                                                 'dateJoined']
                self.search_owner_root_names = ['Shop ID', 'Owner ID', 'First Name', 'Middle Name', 'Last Name', 'Phone Number', ' Email',
                                                'Date Joined']
            if len(self.search_item_records) != 0:
                self.search_item_root_column = ['shopID', 'itemID', 'itemName', 'itemPrice', 'stockLeft', 'itemSold',
                                                'stockAdded',
                                                'aveRating',
                                                'goodRating', 'badRating', 'normalRating']
                self.search_item_root_names = ['Shop ID', 'Item ID', ' Name', ' Price', 'Stock Left', 'Item Sold',
                                               'Stock Added',
                                               'Average Rating', 'Good Rating', 'Bad Rating', 'Normal Rating']
            else:
                tkinter.messagebox.showinfo("Retail Paradise",
                                            "Non-existing ID.")
                return
            self.records.pack_forget()
            self.scroll_y.pack_forget()

            label = ['Shop', 'Owner', 'Items']
            treeview_height = [1, 1, 22]

            search_records_list = [self.search_shop_records, self.search_owner_records, self.search_item_records]
            root_column_list = [self.search_shop_root_column, self.search_owner_root_column,
                                self.search_item_root_column]
            root_names_list = [self.search_shop_root_names, self.search_owner_root_names, self.search_item_root_names]
            width_list = [125, 80, 65]

            for index, (column, names, width, records, labels, height) in enumerate(
                    zip(root_column_list, root_names_list, width_list, search_records_list, label, treeview_height)):
                search_label = customtkinter.CTkLabel(self.TreeviewFrame, text=labels, width=50, height=25,
                                                      fg_color=("white", "#205375"),
                                                      corner_radius=8)
                search_label.grid(row=index, column=0, padx=10)

                if labels == 'Items':
                    scroll_y = Scrollbar(self.TreeviewFrame, orient=VERTICAL)
                    scroll_y.grid(row=index, column=2, sticky='nse', pady=15)
                    tree = ttk.Treeview(self.TreeviewFrame, height=height, columns=column,
                                        yscrollcommand=scroll_y.set)
                else:
                    tree = ttk.Treeview(self.TreeviewFrame, height=height, columns=column)
                tree.grid(row=index, column=1, sticky="nsew", pady=15)
                tree['show'] = 'headings'

                for (search_id, search_text) in zip(column, names):
                    print(search_id, search_text)
                    tree.column(search_id, width=width)
                    tree.heading(search_id, text=search_text)

                root_records = records
                if len(root_records) != 0:
                    for row in root_records:
                        tree.insert('', END, values=row)
            con.commit()
            con.close()

    def delete(self):
        self.deleteID = tkinter.simpledialog.askinteger("Delete Membership",
                                                        "ENTER SHOP ID OR ITEM ID to DELETE:\t\t\t\t\t")
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        delete_cursor = con.cursor()
        if self.deleteID is not None:
            delete_cursor.execute("DELETE from shop WHERE shop_id_number= " + str(self.deleteID))
            delete_cursor.execute("DELETE from root WHERE shop_id_number= " + str(self.deleteID))
            delete_cursor.execute("DELETE from item WHERE shop_id_number= " + str(self.deleteID))
            delete_cursor.execute("DELETE from owner WHERE shop_id_number= " + str(self.deleteID))
            delete_cursor.execute("DELETE from item WHERE item_id_number= " + str(self.deleteID))
            tkinter.messagebox.showinfo("Deleted Membership", "Please Refresh List to see changes.")

        con.commit()
        con.close()

    def update(self):
        self.updateID = tkinter.simpledialog.askinteger("Confirm Membership",
                                                        "ENTER SHOP ID, OWNER ID, OR ITEM ID: \t\t\t\t\t")
        if self.updateID is not None:
            editor = Tk()
            editor.title('Update a Record')
            editor.geometry("440x480")
            editor.configure(bg="#525456")
            con_query = sqlite3.connect('Shoppe Seller Information Management System.db')
            editor_cursor = con_query.cursor()
            record_id = str(self.updateID)
            editor_cursor.execute("SELECT * FROM shop WHERE shop_id_number=" + record_id)
            self.shop_records = editor_cursor.fetchall()
            editor_cursor.execute("SELECT * FROM item WHERE item_id_number=" + record_id)
            self.item_records = editor_cursor.fetchall()
            editor_cursor.execute("SELECT * FROM owner WHERE owner_id_number=" + record_id)
            self.owner_records = editor_cursor.fetchall()
            if len(self.shop_records) != 0:
                self.call_shop(editor, 1, 1)
                self.deployUpdateButton(editor, 7, 1)
                for records in self.shop_records:
                    print(records)
                    self.shop_entries[0].insert(0, records[1])
                    self.shop_entries[1].insert(0, records[2])
                    self.shop_entries[2].insert(0, records[3])
                    self.shop_entries[3].insert(0, records[4])

                    self.owner_editor_id = customtkinter.CTkLabel(editor, text='Owner ID', width=160, height=25,
                                                                  fg_color=("white", "#205375"),
                                                                  corner_radius=8)
                    self.owner_editor_id.grid(sticky=W, row=6, column=0, padx=5, pady=5)
                    self.owner_editor_id = customtkinter.CTkLabel(editor, text=records[5], width=160, height=25,
                                                                  fg_color=("white", "#205375"),
                                                                  corner_radius=8)
                    self.owner_editor_id.grid(sticky=W, row=6, column=1, pady=5, padx=5)

            elif len(self.item_records) != 0:
                self.call_item(editor, 0, 1, 1)
                self.deployUpdateButton(editor, 14, 3)
                for records in self.item_records:
                    self.item_entries[0].insert(0, records[2])
                    self.item_entries[1].insert(0, records[3])
                    self.item_entries[2].insert(0, records[4])
                    self.item_entries[3].insert(0, records[5])
                    self.item_entries[4].insert(0, records[7])
                    self.item_entries[5].insert(0, records[8])
                    self.item_entries[6].insert(0, records[9])
                    self.item_entries[7].insert(0, records[10])

            elif len(self.owner_records) != 0:
                self.call_owner(editor, 0, 1)
                self.deployUpdateButton(editor, 14, 2)
                for records in self.owner_records:
                    split_name = records[2].split(None, 2)
                    self.owner_entries[0].insert(0, records[2])
                    self.owner_entries[1].insert(0, records[3])
                    self.owner_entries[2].insert(0, records[4])
                    self.owner_entries[3].insert(0, records[5])
                    self.owner_entries[4].insert(0, records[6])
                    self.date_editor_id_record = customtkinter.CTkLabel(editor, text=records[7])
                    self.date_editor_id_record.grid(sticky=W, row=13, column=1)
            else:
                editor.destroy()
                return

    def refresh(self):
        # SHOP
        self.entShopID = ''.join(random.choices(string.digits, k=4))
        self.lblShopIDMirror = customtkinter.CTkLabel(self.FormFrame, text=self.entShopID, width=160,
                                                      height=25,
                                                      fg_color=("lightblue", "#125B50"),
                                                      corner_radius=8)
        self.lblShopIDMirror.grid(row=1, column=1, sticky=W, padx=5)
        # OWNER
        self.entOwnerID = ''.join(random.choices(string.digits, k=4))
        self.lblOwnerID = customtkinter.CTkLabel(self.FormFrame, text=self.entOwnerID, pady=1, width=160,
                                                 height=25,
                                                 fg_color=("lightblue", "#125B50"),
                                                 corner_radius=8)
        self.lblOwnerID.grid(row=7, column=1, sticky=W, padx=5)
        # ITEM
        self.entItemID = ''.join(random.choices(string.digits, k=4))
        self.lblItemID = customtkinter.CTkLabel(self.FormFrame, text=self.entItemID, pady=1, width=160,
                                                height=25,
                                                fg_color=("lightblue", "#125B50"),
                                                corner_radius=8)
        self.lblItemID.grid(row=1, column=3, sticky=W, padx=5)

        for index, (shop_entries, owner_entries) in enumerate(zip(self.shop_entries, self.owner_entries)):
            print(owner_entries.get())
            shop_entries.delete(0, END)
            owner_entries.delete(0, END)
        for item_entries in self.item_entries:
            item_entries.delete(0, END)

    def add_info(self):
        self.shop_entries_values_list = []
        for index, (entries, entries_name) in enumerate(zip(self.shop_entries, self.shop_entries_name)):
            entries_name = entries.get()
            self.shop_entries_values_list.append(entries_name)

        self.owner_entries_values_list = []
        for index, (entries, entries_name) in enumerate(zip(self.owner_entries, self.owner_entries_name)):
            entries_name = entries.get()
            self.owner_entries_values_list.append(entries_name)

        self.item_entries_values_list = []
        for index, (entries, entries_name) in enumerate(zip(self.item_entries, self.item_entries_name)):
            entries_name = entries.get()
            self.item_entries_values_list.append(entries_name)

        for index in range(len(self.shop_entries_values_list)):
            if len(self.shop_entries_values_list[index]) == 0:
                tkinter.messagebox.showerror("Retail Paradise Inventory Seller's Information",
                                             "Please fill all forms for Shops.")
                return
            elif self.shop_entries_values_list[2].isdigit() is False or self.shop_entries_values_list[
                3].isdigit() is False:
                tkinter.messagebox.showerror("Retail Paradise Inventory Seller's Information",
                                             "Please fill only integers for Response Rate and Follower Count.")
                return
            print(self.shop_entries_values_list[3])
            if int(self.shop_entries_values_list[3]) >= 100:
                tkinter.messagebox.showerror("Retail Paradise Inventory Seller's Information",
                                             "Please fill only Response Rates in terms of percentages.")
                return
        for index in range(len(self.owner_entries_values_list)):
            if len(self.owner_entries_values_list[index]) == 0:
                tkinter.messagebox.showerror("Retail Paradise Inventory Seller's Information",
                                             "Please fill all forms for Owners.")
                return
        for index in range(len(self.item_entries_values_list)):
            if len(self.item_entries_values_list[index]) == 0:
                tkinter.messagebox.showerror("Retail Paradise Inventory Seller's Information",
                                             "Please fill all forms for Items.")
                return
        for index, values in enumerate(self.item_entries_values_list):
            if index > 0 and not values.isdigit():
                tkinter.messagebox.showerror("Retail Paradise Inventory Seller's Information",
                                             "Please fill integers from price to normal rating.")
                return
            elif index >= 6 and values > 100:
                tkinter.messagebox.showerror("Retail Paradise Inventory Seller's Information",
                                             "Please fill only Ratings in terms of percentages.")
            else:
                self.addItemDatabase()
                return

    def addItemDatabase(self):
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        add_info_cursor = con.cursor()
        # =============================DATABASE INSERT DECLARATION====================================================#
        add_info_cursor.execute(
            "INSERT INTO shop VALUES(:shop_id_number,:shop_name,:shop_location,:shop_followers,:ave_response,:owner_id_number)",
            {
                'shop_id_number': self.entShopID,
                'shop_name': self.shop_entries_values_list[0],
                'shop_location': self.shop_entries_values_list[1],
                'shop_followers': self.shop_entries_values_list[2],
                'ave_response': self.shop_entries_values_list[3],
                'owner_id_number': self.entOwnerID,
            }
        )
        add_info_cursor.execute(
            "INSERT INTO owner VALUES(:shop_id_number,:owner_id_number,:owner_first_name,:owner_middle_name,:owner_surname,:owner_phone_number,:owner_email,:owner_date_joined)",
            {
                'shop_id_number': self.entShopID,
                'owner_id_number': self.entOwnerID,
                'owner_first_name': self.owner_entries_values_list[0],
                'owner_middle_name': self.owner_entries_values_list[1],
                'owner_surname': self.owner_entries_values_list[2],
                'owner_phone_number': self.owner_entries_values_list[3],
                'owner_email': self.owner_entries_values_list[4],
                'owner_date_joined': self.cal.get_date()
            }
        ),
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
                'shop_id_number': self.entShopID,
                'item_id_number': self.entItemID,
                'item_name': self.item_entries[0].get(),
                'item_price': self.item_entries[1].get(),
                'item_stock': int(self.item_entries[2].get()) + int(self.item_entries[4].get()),
                'item_sold': self.item_entries[3].get(),
                'item_stock_added': self.item_entries[4].get(),
                'ave_rating': average,
                'good_rating': good,
                'bad_rating': bad,
                'normal_rating': normal,
            }
        ),
        add_info_cursor.execute(
            "INSERT INTO root VALUES(:shop_id_number,:item_id_number ,:ave_rating  ,:good_rating  ,:bad_rating ,:normal_rating)",
            {
                'shop_id_number': self.entShopID,
                'item_id_number': self.entItemID,
                'ave_rating': average,
                'good_rating': good,
                'bad_rating': bad,
                'normal_rating': normal,
            }
        )
        con.commit()
        con.close()
        tkinter.messagebox.showinfo("Retail Paradise",
                                    "Information Added.")
        self.refresh()

    def add_item(self):
        self.isShopId = tkinter.simpledialog.askinteger("Confirm Membership",
                                                        "ENTER SHOP ID: \t\t\t\t\t")
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        shop_cursor = con.cursor()
        shop_cursor.execute("SELECT shop_id_number FROM shop")
        shop_records = shop_cursor.fetchall()
        for shop in shop_records:
            if self.isShopId == shop[0]:
                self.addItem = Tk()
                self.addItem.configure(bg="#525456")
                self.addItem.title(f"Add an Item for Shop # {self.isShopId}")
                self.addItem.geometry("500x500+200+0")
                self.addItem.resizable(width=False, height=False)
                # ADD ITEM POSITION
                self.call_item(self.addItem, 0, 1, 0)
                self.btnAddNewItem = customtkinter.CTkButton(self.addItem, text="Add Item", pady=1, fg_color='#CC704B',
                                                             height=32,
                                                             border_width=0,
                                                             corner_radius=8,
                                                             padx=20, width=5, command=self.addItemDone)
                self.btnAddNewItem.grid(row=11, column=0, pady=10)
                break

    def addItemDone(self):
        no_error = False
        for index, (values, entries) in enumerate(zip(self.item_entries, self.item_entries_name)):
            if len(values.get()) == 0:
                warning_label = customtkinter.CTkLabel(self.addItemr, text='Please fill in all information.')
                warning_label.grid(row=11, column=1, pady=10, padx=5)
            else:
                self.item_entries_name[index] = values.get()
                no_error = True
        if no_error:
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
                "INSERT INTO item VALUES(:shop_id_number,:item_id_number,:item_name ,:item_price ,:item_stock ,:item_sold,:item_stock_added ,:ave_rating,:good_rating,:bad_rating ,:normal_rating)",
                {
                    'shop_id_number': self.isShopId,
                    'item_id_number': self.entItemID,
                    'item_name': self.item_entries[0].get(),
                    'item_price': self.item_entries[1].get(),
                    'item_sold': self.item_entries[3].get(),
                    'item_stock_added': self.item_entries[4].get(),
                    'item_stock': int(self.item_entries[2].get()) + int(self.item_entries[4].get()),
                    'ave_rating': average,
                    'good_rating': good,
                    'bad_rating': bad,
                    'normal_rating': normal,
                }
            ),
            add_info_cursor.execute(
                "INSERT INTO root VALUES(:shop_id_number,:item_id_number ,:ave_rating  ,:good_rating  ,:bad_rating ,:normal_rating)",
                {
                    'shop_id_number': self.entShopID,
                    'item_id_number': self.entItemID,
                    'ave_rating': average,
                    'good_rating': good,
                    'bad_rating': bad,
                    'normal_rating': normal,
                }
            )
            con.commit()
            con.close()
            self.refresh()
            tkinter.messagebox.showinfo("Retail Paradise Inventory Seller's Information",
                                        "Item Added.")

    def exit_app(self):
        ask_exit = tkinter.messagebox.askyesno("Retail Paradise",
                                               "Are you sure you want to close the program?")
        if ask_exit == 1:
            self.root.destroy()
            return

    def show_item(self):
        for widget in self.TreeviewFrame.winfo_children():
            widget.destroy()
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        item_cursor = con.cursor()
        item_cursor.execute("SELECT * FROM item ORDER BY shop_id_number ASC")
        self.root_column = ['shopID', 'itemID', 'itemName', 'itemPrice', 'stockLeft', 'itemSold', 'stockAdded',
                            'aveRating',
                            'goodRating', 'badRating', 'normalRating']
        self.root_names = ['Shop ID', 'Item ID', ' Name', ' Price', 'Stock Left', 'Item Sold',
                           'Stock Added',
                           'Average Rating', 'Good Rating', 'Bad Rating', 'Normal Rating']
        self.call_treeview_summary(self.root_column, self.root_names, 74)

        root_records = item_cursor.fetchall()
        if len(root_records) != 0:
            # for all rows in root records, insert all the values of the databased towards its end
            for row in root_records:
                self.records.insert('', END, values=row)

        con.commit()
        con.close()

    def show_owner(self):
        for widget in self.TreeviewFrame.winfo_children():
            widget.destroy()
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        item_cursor = con.cursor()
        item_cursor.execute("SELECT * FROM owner ORDER BY owner_id_number")
        self.root_column = ['shopID', 'ownerID', 'ownerFirst', 'ownerMiddle', 'ownerSurname', 'ownerPhone', 'ownerEmail', 'dateJoined']
        self.root_names = ['Shop ID', 'Owner ID', ' First Name', 'Middle Name', 'Surname', 'Phone Number', ' Email', 'Date Joined']
        self.call_treeview_summary(self.root_column, self.root_names, 100)
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        root_cursor = con.cursor()
        root_cursor.execute("SELECT * FROM owner")

        # for root only in main display
        root_records = root_cursor.fetchall()
        if len(root_records) != 0:
            # for all rows in root records, insert all the values of the databased towards its end
            for row in root_records:
                self.records.insert('', END, values=row)
        con.commit()
        con.close()

    def show_shop(self):
        for widget in self.TreeviewFrame.winfo_children():
            widget.destroy()
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        self.root_column = ['shopID', 'shopName', 'shopLocation', 'shopFollower', 'shopAverageResponse', 'OwnerID']
        self.root_names = ['Shop ID', ' Name', ' Location', 'Followers', 'Average Response Rate', 'Owner ID']
        self.call_treeview_summary(self.root_column, self.root_names, 135)

        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        root_cursor = con.cursor()
        root_cursor.execute("SELECT * FROM shop ORDER BY shop_id_number")

        # for root only in main display
        root_records = root_cursor.fetchall()
        if len(root_records) != 0:
            # for all rows in root records, insert all the values of the databased towards its end
            for row in root_records:
                self.records.insert('', END, values=row)
        con.commit()
        con.close()

    def show_summary(self):
        for widget in self.TreeviewFrame.winfo_children():
            widget.destroy()
        self.root_column = ['shopID', 'itemID', 'aveRating', 'goodRating', 'badRating', 'normalRating']
        self.root_names = ['Shop ID', 'Item ID', 'Average Rating', 'Good Rating', 'Bad Rating', 'Normal Rating']
        self.call_treeview_summary(self.root_column, self.root_names, 135)
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        root_cursor = con.cursor()
        root_cursor.execute("SELECT * FROM root ORDER BY shop_id_number")

        # for root only in main display
        root_records = root_cursor.fetchall()
        if len(root_records) != 0:
            # for all rows in root records, insert all the values of the databased towards its end
            for row in root_records:
                self.records.insert('', END, values=row)
        con.commit()
        con.close()

    def update_shop(self):
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        add_info_cursor = con.cursor()
        add_info_cursor.execute("""
                          UPDATE shop SET
                               shop_id_number =:shop_id_number,
                               shop_name =:shop_name,
                               shop_location =:shop_location,
                               shop_followers=:shop_followers,
                               ave_response=:ave_response
                               WHERE shop_id_number = :shop_id_number
                          """, {
            'shop_id_number': self.entShopID,
            'shop_name': self.shop_entries[0].get(),
            'shop_location': self.shop_entries[1].get(),
            'shop_followers': self.shop_entries[2].get(),
            'ave_response': self.shop_entries[3].get(),
            'owner_id_number': self.entOwnerID,
        })
        con.commit()
        con.close()
        tkinter.messagebox.showinfo("Retail Paradise Inventory Seller's Information",
                                    "Information Updated.")

    def update_owner(self):
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        add_info_cursor = con.cursor()
        add_info_cursor.execute("""
                          UPDATE owner SET
                              owner_id_number = :owner_id_number,
                              owner_first_name = :owner_first_name,
                              owner_middle_name = :owner_middle_name,
                              owner_surname = :owner_surname,
                              owner_phone_number = :owner_phone_number,
                              owner_email = :owner_email
                              WHERE owner_id_number = :owner_id_number
                          """, {
            'owner_id_number': self.entOwnerID,
            'owner_first_name': self.owner_entries[0].get(),
            'owner_middle_name': self.owner_entries[1].get(),
            'owner_surname': self.owner_entries[2].get(),
            'owner_phone_number': self.owner_entries[3].get(),
            'owner_email': self.owner_entries[4].get(),
            'owner_date_joined': self.cal.get_date()
        })
        con.commit()
        con.close()
        tkinter.messagebox.showinfo("Retail Paradise Inventory Seller's Information",
                                    "Information Updated.")

    def update_item(self):
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        add_info_cursor = con.cursor()
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
            'item_stock': int(self.item_entries[2].get()) + int(self.item_entries[4].get()),
            'item_sold': self.item_entries[3].get(),
            'item_stock_added': self.item_entries[4].get(),
            'ave_rating': (int(self.item_entries[5].get()) + int(self.item_entries[6].get()) + int(self.item_entries[7].get())) / 3,
            'good_rating': self.item_entries[5].get(),
            'bad_rating': self.item_entries[6].get(),
            'normal_rating': self.item_entries[7].get(),
        })
        add_info_cursor.execute("""
                          UPDATE root SET
                              ave_rating =:ave_rating,
                              good_rating =:ave_rating,
                              bad_rating =:bad_rating,
                              normal_rating =:normal_rating
                              WHERE item_id_number =:item_id_number
                          """, {
            'item_id_number': self.updateID,
            'ave_rating': (int(self.item_entries[5].get()) + int(self.item_entries[6].get()) + int(self.item_entries[7].get())) / 3,
            'good_rating': self.item_entries[5].get(),
            'bad_rating': self.item_entries[6].get(),
            'normal_rating': self.item_entries[7].get(),
        })
        con.commit()
        con.close()
        tkinter.messagebox.showinfo("Retail Paradise Inventory Seller's Information",
                                    "Information Updated.")

    def deployUpdateButton(self, frame, row, command):
        if command == 1:
            button = customtkinter.CTkButton(frame, text='Done', width=120, fg_color='#CC704B',
                                             height=32,
                                             border_width=0,
                                             corner_radius=8,
                                             command=self.update_shop)
            button.grid(row=row, column=0, padx=15, sticky=W, pady=5)
        if command == 2:
            button = customtkinter.CTkButton(frame, text='Done', width=120, fg_color='#CC704B',
                                             height=32,
                                             border_width=0,
                                             corner_radius=8,
                                             command=self.update_owner)
            button.grid(row=row, column=0, padx=15, sticky=W, pady=5)
        if command == 3:
            button = customtkinter.CTkButton(frame, text='Done', width=120, fg_color='#CC704B',
                                             height=32,
                                             border_width=0,
                                             corner_radius=8,
                                             command=self.update_item)
            button.grid(row=row, column=0, padx=15, sticky=W, pady=5)

    def call_button_assignment(self):

        self.button_text = ["Add Data", "Summary List", "Shops List", "Owner List", "Items List", "Add Item", "Update",
                            "Search", "Delete", "Refresh", "Exit"]
        self.button_function = [self.add_info, self.show_summary, self.show_shop, self.show_owner, self.show_item,
                                self.add_item,
                                self.update, self.search, self.delete, self.refresh, self.exit_app]

        for index, (button_text, button_function) in enumerate(zip(self.button_text, self.button_function), start=0):
            button = customtkinter.CTkButton(self.ButtonFrame, text=button_text, width=100, fg_color='#CC704B',
                                             height=38,
                                             border_width=0,
                                             corner_radius=8,
                                             command=button_function)
            button.grid(row=0, column=index, padx=15, sticky=W, pady=5)
