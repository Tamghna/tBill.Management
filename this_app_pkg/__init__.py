import ttkbootstrap as tk
import sqlite3
class bill_manager():
    def create_bill_window():
        print("EXECUTED")

        win1 = tk.Toplevel()
        win1.geometry("1200x600")
        win1.title("CREATE A NEW BILL _ WINDOW")
        
        
        
        
        
        win1.mainloop()
        

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
        
        
        Checkbutton1 = tk.IntVar()   

  
        Button1 = tk.Checkbutton(win2, text = "Preset Price?",  
                            variable = Checkbutton1, 
                            onvalue = 1, 
                            offvalue = 0, )
        
        Button1.pack()
                
        
        
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
        