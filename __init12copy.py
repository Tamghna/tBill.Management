import ttkbootstrap as tk
import sqlite3
import sqlite3
import ttkbootstrap as tk 
import tkinter as otk 
import datetime
import time
import os
import tsoft_basic_pkg
import this_app_pkg
from tkinter import ttk 


class bill_manager():
    def create_bill_window():

        cached_list_items_win1 = []
        global total_price_count
        total_price_count = 0




        def addItem():
            global treev_win1
            #getting
            item_name = manual_itemname_entry_entry_win1.get()

            if item_name == "":
                item_name = clicked1.get()

            item_price = manual_itemprice_entry_entry_win1.get()

            item_quantity = itemquantity_entry_entry_win1.get()

            item_gst = "12%"
            global total_price_count
            total_price_count += int(item_price)


            

            cached_list_items_win1.append([item_name , item_price , item_quantity , item_gst])
            
            
            treev_win1.insert("", 'end', text ="L1", 
                    values = (item_name , item_price , item_gst , item_quantity))
            
            print(cached_list_items_win1)
            print(total_price_count)







        def remove_from_item_list_view_win1():
            global treev_win1

            slecteditem_win1_item_list_view = treev_win1.focus()


            details = treev_win1.item(slecteditem_win1_item_list_view)


            global total_price_count

            total_price_count -= int(details.get("values")[1])


            cached_list_items_win1.remove([str(details.get("values")[0])   , str(details.get("values")[1]) , str( details.get("values")[3])    ,   str(details.get("values")[2] ) ])


            treev_win1.delete(slecteditem_win1_item_list_view)


            



            print(cached_list_items_win1)
            print(total_price_count)















        con1 = sqlite3.connect("items.db")
        cur1 = con1.cursor()


        win1 = tk.Toplevel()
        win1.geometry("1300x800")
        win1.title("CREATE A NEW BILL _ WINDOW")
        win1.config(background="#b3c6ff")
        
        
        heading_win1 = tk.Label(win1,text="Create New Bill/Invoice :-" , font=("London-Tube" , 19))
        heading_win1.pack(pady=10)
        
        
        manual_itemname_entry_text_win1 = tk.Label(win1 , text="ENTER ITEM NAME MANUALLY:-")
        manual_itemname_entry_text_win1.pack(anchor="n" , side="left" , padx=2 , pady=10)
        
        manual_itemname_entry_entry_win1 = tk.Entry(win1)
        manual_itemname_entry_entry_win1.pack(anchor="n" , side="left" , pady=10)
        
        
        
        
        
        
        
        
        manual_itemprice_entry_text_win1 = tk.Label(win1 , text="ENTER ITEM PRICE MANUALLY:-")
        manual_itemprice_entry_text_win1.pack(anchor="n" , side="left" , padx=10 , pady=10)
        
        manual_itemprice_entry_entry_win1 = tk.Entry(win1)
        manual_itemprice_entry_entry_win1.pack(anchor="n" , side="left" , pady=10)
        
        
        
        
        
        itemquantity_entry_text_win1 = tk.Label(win1 , text="ENTER Quantity:-")
        itemquantity_entry_text_win1.pack(anchor="n" , side="left" , padx=10 , pady=10)
        
        itemquantity_entry_entry_win1 = tk.Entry(win1)
        itemquantity_entry_entry_win1.pack(anchor="n" , side="left" , pady=10)


        #DROP DOWN


        cur1.execute("SELECT * FROM item")

        get_data_for_drop_down_menu = cur1.fetchall()

        options = []
        
        for sorted_get_data_drop in get_data_for_drop_down_menu:
            options.append(sorted_get_data_drop[0])


  
# datatype of menu text 
        clicked1 = tk.StringVar() 
        
        # initial menu text 

        
        # Create Dropdown menu 
        drop1_win1 = tk.OptionMenu( win1 , clicked1 , *options ) 

        or_other_optin_label_win1 = tk.Label(win1 , text="OR select from list of added items:-")
        or_other_optin_label_win1.place(x=1 , y=93)

        drop1_win1.place(x=200 , y=93)
                
            
        
        global treev_win1
        
        treev_win1 = ttk.Treeview(win1, selectmode ='browse')

        
 
        # Calling pack method w.r.to treeview
        treev_win1.place(x=20 , y=150)
        
        # Constructing vertical scrollbar
        # with treeview
        verscrlbar = ttk.Scrollbar(win1, 
                                orient ="vertical", 
                                command = treev_win1.yview)
        
        # Calling pack method w.r.to vertical 
        # scrollbar
        verscrlbar.pack()
        
        # Configuring treeview
        treev_win1.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev_win1["columns"] = ("1", "2", "3" , "4")
        
        # Defining heading
        treev_win1['show'] = 'headings'
        
        # Assigning the width and anchor to  the
        # respective columns
        treev_win1.column("1", width = 270, anchor ='c')
        treev_win1.column("2", width = 150, anchor ='c')
        treev_win1.column("3", width = 150, anchor ='c')
        treev_win1.column("4", width = 150, anchor ='c')
        
        # Assigning the heading names to the 
        # respective columns
        treev_win1.heading("1", text ="ITEM NAME")
        treev_win1.heading("2", text ="PRICE")
        treev_win1.heading("3", text ="GST")
        treev_win1.heading("4", text ="QUANTITY")
        
        # Inserting the items and their features to the 
        # columns built




                
        
        
        add_item_button_win1 = tk.Button(win1 , text="ADD ITEM ✅" , bootstyle="outlined" , command=addItem)
        add_item_button_win1.place(x=20 , y=390)
        
        remove_selected_item_button_win1 = tk.Button(win1 , text="REMOVE AN SELECTED ITEM ❌" , bootstyle="outlined" , command=remove_from_item_list_view_win1)
        remove_selected_item_button_win1.place(x=170 , y=390)

        save_bill_win1 = tk.Button(win1 , text="SAVE BILL/INVOICE 💾" , bootstyle="outlined")
        save_bill_win1.place(x=970 , y=390)
        
        save_bill_and_print_win1 = tk.Button(win1 , text="SAVE BILL AND PRINT 💾🖨️" , bootstyle="outlined")
        save_bill_and_print_win1.place(x=970 , y=420)
        
        
        
        fill_this_details_text_win1 = tk.Label(win1 , text="Fill the Patient Data before adding items!:-" , font=("London-Tube" , 15 ) , background="red")
        fill_this_details_text_win1.place(x=10 , y=450)
        
        cust_name_text_win1 = tk.Label(win1 , text="Patient Name:")
        cust_name_text_win1.place(x=10 , y=490)
        cust_name_entry_win1 = tk.Entry(win1)
        cust_name_entry_win1.place(x=119 , y=490)
        
        
        cust_age_text_win1 = tk.Label(win1 , text="Patient Age:")
        cust_age_text_win1.place(x=10 , y=515)
        cust_age_entry_win1 = tk.Entry(win1)
        cust_age_entry_win1.place(x=119 , y=515)
        
        
        
        cust_address_text_win1 = tk.Label(win1 , text="Patient Address:")
        cust_address_text_win1.place(x=10 , y=542)
        cust_address_entry_win1 = tk.Entry(win1)
        cust_address_entry_win1.place(x=120  , y=542)

        
        
        


        clicked2 = tk.StringVar()
        options2=["----SELECT GENDER----" , "MALE" , "FEMALE"]
        cust_gender_text_win1 = tk.Label(win1 , text="Patient Gender:")
        cust_gender_text_win1.place(x=10 , y=574)
        clicked2 = tk.StringVar() 
        
        # initial menu text 
        clicked2.set( "----SELECT GENDER----" ) 
        
        # Create Dropdown menu 
        drop2_win1 = tk.OptionMenu( win1 , clicked2 , *options2 ) 


        drop2_win1.place(x=137 , y=574)
        
        
        
        
        
        
        
        
        
        
        win1.mainloop()
        
    
    
    
    
    
    def edit_bill_window():
        win4 = tk.Toplevel()
        win4.geometry("1300x800")
        win4.title("EDIT BILL   |   tBillManager")
        
        
        
        
        
        
        
        win4.geometry()








#************************************************************************************************************************************************************#



class item_manager():
    def add_an_item_to_database_window():
        
        
        def add_exe():
            from tkinter import messagebox
            import os
            print(os.curdir)
            item_name_get = win2_item_name_entry.get()
            item_price_get = win2_item_price_entry.get()
            item_gst_get = win2_item_gst_entry.get()
            
            conn2 = sqlite3.connect("items.db")
            cur2 = conn2.cursor()

            cur2.execute("insert into item values (?, ?, ?)",(item_name_get, item_price_get, item_gst_get))
            
            conn2.commit()
            
            win2.destroy()
            
            messagebox.showinfo("" , "SUCESS!")
            
        
        
        
        
        
        
        
        
        
        win2 = tk.Toplevel()
        win2.geometry("1200x600")
        win2.title("Add item to database")
        
        win2_item_name_text = tk.Label(win2 , text="Item name:-")
        win2_item_name_text.pack()
        
        win2_item_name_entry = tk.Entry(win2)
        win2_item_name_entry.pack()
        
        
        
        win2_item_price_text = tk.Label(win2 , text="Item Price:-")
        win2_item_price_text.pack()
        
        win2_item_price_entry = tk.Entry(win2)
        win2_item_price_entry.pack(padx=5)
        
        
        
        win2_item_gst_text = tk.Label(win2 , text="Item GST%:-")
        win2_item_gst_text.pack()
        
        win2_item_gst_entry = tk.Entry(win2)
        win2_item_gst_entry.pack(padx=5)
        

        
        
        win2_save_button = tk.Button(win2 , text="SAVE" , command=add_exe)
        win2_save_button.pack(anchor="center")
        
        
        
        win2.mainloop()
        
        
        
        
    def view_item_window():
        global lcount
        lcount = 0

        from tkinter import ttk 

        win3 = tk.Window()
        win3.geometry("1000x400")
        
        conn2 = sqlite3.connect("items.db")
        cur2 = conn2.cursor()
        
        
        
        treev = ttk.Treeview(win3, selectmode ='browse')
 
        # Calling pack method w.r.to treeview
        treev.pack()
        
        # Constructing vertical scrollbar
        # with treeview
        verscrlbar = ttk.Scrollbar(win3, 
                                orient ="vertical", 
                                command = treev.yview)
        
        # Calling pack method w.r.to vertical 
        # scrollbar
        verscrlbar.pack(side="right",fill ='x')
        
        # Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = ("1", "2", "3" )
        
        # Defining heading
        treev['show'] = 'headings'
        
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width = 230, anchor ='c')
        treev.column("2", width = 150, anchor ='se')
        treev.column("3", width = 150, anchor ='se')

        
        # Assigning the heading names to the 
        # respective columns
        treev.heading("1", text ="Item Name")
        treev.heading("2", text ="Price in ₹")
        treev.heading("3", text ="GST%")

        # Inserting the items and their features to the 
        # columns built
        cur2.execute("SELECT * FROM item")

        data = cur2.fetchall()

        for single in data:
            one = single[0]
            two = single[1]
            three= single[2]
            
            lcount +=1
            
            
            treev.insert("", 'end', text = "L" + str(lcount), 
                        values = (one,two,three))
                
            

            
            


                
                
                
                
                
        
        
        
        
        
        
        
        
        win3.mainloop()
        