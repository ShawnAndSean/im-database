import random
import sqlite3
import string
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import simpledialog
from tkcalendar import Calendar
import customtkinter


class login:
    def __init__(self, root, shop_id):
        self.admin = None
        self.is_user = None
        self.search_shop_id = shop_id
        self.date_editor_id_record = None
        self.owner_editor_id = None
        self.owner_records = None
        self.shop_records = None
        self.updateID = None
        self.owner_entries_values_list = None
        self.shop_entries_values_list = None
        self.lblOwnerID = None
        self.lblShopIDMirror = None
        self.shopId = None
        self.entShopID = None
        self.entShopAverageResponseRate = None
        self.entShopFollowerCount = None
        self.entShopLocation = None
        self.entShopName = None
        self.shop_entries = None
        self.shop_entries_name = None
        self.OwnerID = None
        self.cal = None
        self.owner_entries = None
        self.owner_entries_name = None
        self.entOwnerID = None
        self.entOwnerNameLast = None
        self.entOwnerNameFirst = None
        self.entOwnerNameMiddle = None
        self.entOwnerPhone = None
        self.entOwnerEmail = None
        self.root = root
        self.root.title("Retail Paradise User")
        self.root.geometry("1370x800")
        self.root.resizable(width=False, height=False)
        self.MainFrame = customtkinter.CTkFrame(self.root)
        self.MainFrame.grid(pady=30, padx=30)
        # Item Form Frame
        self.ShopFrame = customtkinter.CTkFrame(self.MainFrame, width=970, height=800)
        self.ShopFrame.grid(row=1, column=0, pady=10, padx=15)

        self.OwnerFrame = customtkinter.CTkFrame(self.MainFrame, width=970, height=800)
        self.OwnerFrame.grid(row=1, column=1, pady=10, padx=15, sticky="w")

        self.ButtonFrame = customtkinter.CTkFrame(self.MainFrame, width=970, height=200)
        self.ButtonFrame.grid(row=1, column=0, pady=50, padx=15, sticky="s")

        self.call_owner(0)
        self.call_shop(0)
        if not shop_id:
            self.call_button_assignment()
        if shop_id:
            self.call_update_button_assignment()

    def call_owner(self, value):
        if value == 0:
            self.entOwnerID = ''.join(random.choices(string.digits, k=4))
            self.cal = Calendar(self.OwnerFrame, selectmode='day', year=2020, month=5, day=22)
            self.cal.grid(row=13, column=1, sticky=W, padx=5, pady=40)
        if value == 1:
            self.cal.destroy()

        label_text = ['Owner Information', 'Owner ID *', 'First Name *', 'Middle Name',
                      'Last Name *', 'Phone Number *', 'Email', 'Date Joined']

        self.OwnerID = customtkinter.CTkLabel(self.OwnerFrame, text=self.entOwnerID, width=400,
                                              height=40,
                                              fg_color=("lightblue", "#125B50"),
                                              corner_radius=8)
        self.OwnerID.grid(row=7, column=1, sticky=W, padx=15, pady=5)
        for owner_index, owner_text in enumerate(label_text, start=0):
            if owner_index == 0:
                label = customtkinter.CTkLabel(self.OwnerFrame, text=owner_text, width=160,
                                               height=40,
                                               fg_color=("lightblue", "#BB6464"),
                                               corner_radius=8)
                label.grid(row=owner_index + 6, column=0, sticky=W, padx=15, pady=10)
            else:
                label = customtkinter.CTkLabel(self.OwnerFrame, text=owner_text, width=160, height=40,
                                               fg_color=("white", "#205375"),
                                               corner_radius=8)
                label.grid(row=owner_index + 6, column=0, sticky=W, padx=15, pady=5)

        self.owner_entries = []
        self.owner_entries_name = [
            self.entOwnerNameFirst,
            self.entOwnerNameMiddle,
            self.entOwnerNameLast,
            self.entOwnerPhone,
            self.entOwnerEmail,
        ]

        for index in range(8, 13):
            owner_entry = customtkinter.CTkEntry(self.OwnerFrame, width=400, justify='left', height=40)
            owner_entry.grid(row=index, column=1, sticky=W, padx=15, pady=10)
            self.owner_entries.append(owner_entry)

    def call_shop(self, value):
        if value == 0:
            self.entShopID = ''.join(random.choices(string.digits, k=4))
        if value == 1:
            self.entShopID = self.updateID
        self.shopId = customtkinter.CTkLabel(self.ShopFrame, text=self.entShopID, width=400,
                                             height=40,
                                             fg_color=("lightblue", "#125B50"),
                                             corner_radius=8)
        self.shopId.grid(row=1, column=1, sticky=W, padx=15, pady=10)

        label_text = ['Shop Information', 'Shop ID *', 'Shop Name *', 'Location *', 'Follower Count',
                      'Average Response Rate']

        for index, text in enumerate(label_text, start=0):
            if index == 0:
                label = customtkinter.CTkLabel(self.ShopFrame, text=text, width=160,
                                               height=40,
                                               fg_color=("lightblue", "#BB6464"),
                                               corner_radius=8)
                label.grid(row=0, column=0, sticky=W, padx=15, pady=10)
            else:
                label = customtkinter.CTkLabel(self.ShopFrame, text=text, width=160, height=40,
                                               fg_color=("white", "#205375"),
                                               corner_radius=8)
                label.grid(row=index, column=0, sticky=W, padx=15, pady=10)
        self.shop_entries = []
        self.shop_entries_name = [
            self.entShopID,
            self.entShopName,
            self.entShopLocation,
            self.entShopFollowerCount,
            self.entShopAverageResponseRate,
        ]
        for index in range(2, 6):
            shop_entry = customtkinter.CTkEntry(self.ShopFrame, width=400, justify='left', height=40)
            shop_entry.grid(row=index, column=1, sticky=W, padx=15, pady=10)
            self.shop_entries.append(shop_entry)

    def call_button_assignment(self):
        button_text = ["Login", "Register", 'Refresh', "Exit"]
        button_function = [self.login_user, self.add_data, self.refresh, self.exit]

        for index, (button_text, button_function) in enumerate(zip(button_text, button_function), start=0):
            button = customtkinter.CTkButton(self.ButtonFrame, text=button_text, width=110, fg_color='#CC704B',
                                             height=40,
                                             border_width=3,
                                             corner_radius=8,
                                             command=button_function, text_font=30)
            button.grid(row=0, column=index, padx=15, sticky='nesw', pady=5)

    def login_user(self):
        from user import user
        self.is_user = tkinter.simpledialog.askinteger("Confirm Membership",
                                                       "ENTER SHOP ID: \t\t\t\t\t")
        con = sqlite3.connect('Shoppe Seller Information Management System.db', timeout=2)
        shop_cursor = con.cursor()
        shop_cursor.execute("SELECT shop_id_number FROM shop")
        shop_records = shop_cursor.fetchall()
        for shop in shop_records:
            if self.is_user == shop[0]:
                root = customtkinter.CTk()
                self.admin = user(root, self.is_user)
                root.mainloop()

    def call_update_button_assignment(self):
        self.update()
        button_text = ["Update", 'Refresh', "Exit"]
        button_function = [self.updateFinal, self.refresh, self.exit]

        for index, (button_text, button_function) in enumerate(zip(button_text, button_function), start=0):
            button = customtkinter.CTkButton(self.ButtonFrame, text=button_text, width=110, fg_color='#CC704B',
                                             height=40,
                                             border_width=3,
                                             corner_radius=8,
                                             command=button_function, text_font=30)
            button.grid(row=0, column=index, padx=15, sticky='nesw', pady=5)

    def add_data(self):
        self.shop_entries_values_list = []
        for index, (entries, entries_name) in enumerate(zip(self.shop_entries, self.shop_entries_name)):
            entries_name = entries.get()
            self.shop_entries_values_list.append(entries_name)

        self.owner_entries_values_list = []
        for index, (entries, entries_name) in enumerate(zip(self.owner_entries, self.owner_entries_name)):
            entries_name = entries.get()
            self.owner_entries_values_list.append(entries_name)

        for index in range(len(self.shop_entries_values_list)):
            if len(self.shop_entries_values_list[index]) == 0:
                tkinter.messagebox.showerror("Retailer's Paradise Inventory Seller's Information",
                                             "Please fill all forms for Shops.")
                return
            elif self.shop_entries_values_list[2].isdigit() is False or self.shop_entries_values_list[3].isdigit() is False:
                tkinter.messagebox.showerror("Retailer's Paradise Inventory Seller's Information",
                                             "Please fill only integers for Response Rate and Follower Count.")
                return
        for index in range(len(self.owner_entries_values_list)):
            if len(self.owner_entries_values_list[index]) == 0:
                tkinter.messagebox.showerror("Retailer's Paradise Inventory Seller's Information",
                                             "Please fill all forms for Owners.")
                return
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
        con.commit()
        con.close()
        tkinter.messagebox.showinfo("Retailer's Paradise Inventory Seller's Information",
                                    "Information Added.")
        self.refresh()

    def update(self):
        self.updateID = self.search_shop_id
        if self.updateID is not None:
            con_query = sqlite3.connect('Shoppe Seller Information Management System.db')
            editor_cursor = con_query.cursor()
            record_id = str(self.updateID)
            editor_cursor.execute("SELECT * FROM shop WHERE shop_id_number=" + record_id)
            self.shop_records = editor_cursor.fetchall()
            editor_cursor.execute("SELECT * FROM owner WHERE shop_id_number=" + record_id)
            self.owner_records = editor_cursor.fetchall()

            if len(self.shop_records) != 0:
                self.call_shop(1)
                for records in self.shop_records:
                    self.shop_entries[0].insert(0, records[1])
                    self.shop_entries[1].insert(0, records[2])
                    self.shop_entries[2].insert(0, records[3])
                    self.shop_entries[3].insert(0, records[4])
                    self.entOwnerID = records[5]
            if len(self.owner_records) != 0:
                self.call_owner(1)
                for records in self.owner_records:
                    self.owner_entries[0].insert(0, records[2])
                    self.owner_entries[1].insert(0, records[3])
                    self.owner_entries[2].insert(0, records[4])
                    self.owner_entries[3].insert(0, records[5])
                    self.owner_entries[4].insert(0, records[6])
                    date = records[7]
                    split_date = date.split('/')
                    self.cal = Calendar(self.OwnerFrame, selectmode='day', year=int(split_date[2]), month=int(split_date[0]), day=int(split_date[1]))
                    self.cal.grid(row=13, column=1, sticky=W, padx=5, pady=40)

    def updateFinal(self):
        print(self.entOwnerID)
        print(self.entShopID)
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
        }),
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
        tkinter.messagebox.showinfo("Retailer's Paradise Inventory Seller's Information",
                                    "Information Updated.")

    def refresh(self):
        # SHOP
        self.entShopID = ''.join(random.choices(string.digits, k=4))
        self.lblShopIDMirror = customtkinter.CTkLabel(self.ShopFrame, text=self.entShopID, width=400,
                                                      height=40,
                                                      fg_color=("lightblue", "#125B50"),
                                                      corner_radius=8)
        self.lblShopIDMirror.grid(row=1, column=1, sticky=W, padx=15)
        # OWNER
        self.entOwnerID = ''.join(random.choices(string.digits, k=4))
        self.lblOwnerID = customtkinter.CTkLabel(self.OwnerFrame, text=self.entOwnerID, pady=1, width=400,
                                                 height=40,
                                                 fg_color=("lightblue", "#125B50"),
                                                 corner_radius=8)
        self.lblOwnerID.grid(row=7, column=1, sticky=W, padx=15)

        for index, (shop_entries, owner_entries) in enumerate(zip(self.shop_entries, self.owner_entries)):
            shop_entries.delete(0, END)
            owner_entries.delete(0, END)

    def exit(self):
        ask_exit = tkinter.messagebox.askyesno("Retailer's Paradise Inventory Seller's Information",
                                               "Are you sure you want to close the program?")
        if ask_exit == 1:
            self.root.destroy()
            return
