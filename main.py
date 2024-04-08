import sqlite3
import ttkbootstrap as tk 
import tkinter as otk 
import datetime
import time
import os
import tsoft_basic_pkg
import this_app_pkg
from tkinter import ttk 
from tkinter import messagebox




ft_val = open("ft_value.val" , 'r').read()

if ft_val == "FIRST_OPEN":
    from tkinter import messagebox
    from tkinter.simpledialog import askstring
    
    messagebox.showinfo("" , "WELCOME , LETS SETUP!")
    
    
    com_name = askstring('////\\\\', 'Enter Your Company name:')
    os.chdir("settings")
    with open("com_name.set" , 'w')as f:
        f.write(com_name)
        f.close()
    os.chdir("..")
    
    with open("ft_value.val" , 'w')as w:
        w.write("SUCESS_SETUP[CODE:0]")
    

        
        



















#Start a new database connection:
conn = sqlite3.connect("bill_data.db")
cur = conn.cursor()

#Create Table:
cur.execute("""CREATE TABLE IF NOT EXISTS bill_data_cust(
    
    name text,
    phone text,
    ammount text,
    date text    
     
    
    )""")


cur.execute("""CREATE TABLE IF NOT EXISTS bill_data(
    
    name text,
    items text,
    ammount text
     
    
    )""")





conn2 = sqlite3.connect("items.db")
cur2 = conn2.cursor()

#Create Table:
cur2.execute("""CREATE TABLE IF NOT EXISTS item(
    
    item_name,
    item_price,
    item_gst
    
    )""")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#MAIN root INSILIZATION:
root = tk.Window()
root.config(background="#b3c6ff")
root.attributes('-fullscreen', True)
root.title("tBillMangagement")
root.geometry("1300x500")

def get_time():
    date_time_label.config(text=tsoft_basic_pkg.time.timenow())
    date_time_label.after(1000, get_time)
 
os.chdir("settings")   
com_name_get = open("com_name.set" , 'r').read()
os.chdir("..")

welcome_text = tk.Label(root  , text="WELCOME , " + com_name_get , font=("London-Tube" , 25))
welcome_text.pack()



date_time_label = tk.Label(root , text="DATA_NOT_FOUND" , font=("London-Tube" , 20))
date_time_label.pack()

exit_button = tk.Button(root , text="EXIT" , command=exit , bootstyle="outlined")
exit_button.pack(side="right" , padx=10)




tabControl = ttk.Notebook(root) 

  
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

  
tabControl.add(tab1, text ='Home') 
tabControl.add(tab2, text ='Billing') 
tabControl.add(tab3, text ='Items/Services Management') 
tabControl.add(tab4, text ="USER") 
tabControl.add(tab5, text ='Settings') 

tabControl.pack(expand = 1, fill ="both" , padx=10 , pady= 10) 


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#











#home:
todays_sale_label = tk.Label(tab1 , text="Todays Sales:" , font=("Impact" , 15))
todays_sale_label.pack()






#Billing:

treev = ttk.Treeview(tab2, selectmode ='browse')
 
# Calling pack method w.r.to treeview
treev.pack()
 
# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(root, 
                           orient ="vertical", 
                           command = treev.yview)
 
# Calling pack method w.r.to vertical 
# scrollbar
verscrlbar.pack(side="right",fill ='x')
 
# Configuring treeview
treev.configure(xscrollcommand = verscrlbar.set)
 
# Defining number of columns
treev["columns"] = ("1", "2", "3" , "4")
 
# Defining heading
treev['show'] = 'headings'
 
# Assigning the width and anchor to  the
# respective columns
treev.column("1", width = 150, anchor ='c')
treev.column("2", width = 150, anchor ='c')
treev.column("3", width = 150, anchor ='c')
treev.column("4", width = 150, anchor ='c')
 
# Assigning the heading names to the 
# respective columns
treev.heading("1", text ="Name")
treev.heading("2", text ="Address")
treev.heading("3", text ="AMMOUNT")
treev.heading("4", text ="Date")
 
# Inserting the items and their features to the 
# columns built
cur.execute("SELECT * FROM bill_data_cust")

data = cur.fetchall()

for single in data:
    one = single[0]
    two = single[1]
    three= single[2]
    four = single[3]


    treev.insert("", 'end', text ="L1", 
            values = (one,two,three,four))






create_bill_launcher_button = tk.Button(tab2, text="Create Bill" ,bootstyle="outlined",command=this_app_pkg.bill_manager.create_bill_window)
create_bill_launcher_button.pack()


edit_bill_launcher_button = tk.Button(tab2, text="Edit Selected Bill 🧑‍💻" ,bootstyle="outlined", command=this_app_pkg.bill_manager.create_bill_window)
edit_bill_launcher_button.pack()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#











#item Management:

add_an_item_to_database_button = tk.Button(tab3 , text="Add an item/service to database" , command=this_app_pkg.item_manager.add_an_item_to_database_window)
add_an_item_to_database_button.pack(pady=10)

view_all_item_from_data_base_button = tk.Button(tab3 , text="View all items in database" , command=this_app_pkg.item_manager.view_item_window)
view_all_item_from_data_base_button.pack(pady=10)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#





#SETTINGS:


from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
def change_logo_settings():

    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    os.chdir("settings")

    with open("logo_path.set" , 'w')as f:
        f.write(str(filename))
        f.close()



    os.chdir("..")

    from tkinter import messagebox
    messagebox.showinfo("LOGO SAVED")


def change_invoice_title():
    from tkinter import messagebox
    from tkinter.simpledialog import askstring
    

    
    
    title_name_cache = askstring('////\\\\', 'Enter Invoice TITLE:-')

    os.chdir("settings")

    with open("invoice_title.set" , 'w')as f:
        f.write(str(title_name_cache))
        f.close()

    os.chdir("..")



def set_hospital_ipd_mode():
    print("RAN")

    if messagebox.askyesnocancel("" , "Do you want to HOSPITAL IPD MODE to BE ON?           CLICK [YES] to turn {ON} and CLICK [NO] to turn {OFF}") == True:

        
        os.chdir("settings")
        with open("hospital_ipd_mode.set" , 'w')as f:
            f.write("1")
            f.close()

        os.chdir("..")
        messagebox.showinfo("" , "SET SUCESSFULLY")

    else:
        os.chdir("settings")
        with open("hospital_ipd_mode.set" , 'w')as f:
            f.write("0")
            f.close()

        os.chdir("..")
        messagebox.showinfo("" , "SET SUCESSFULLY")






change_company_name_button_tab5 = tk.Button(tab5 , text="CHANGE COMPANY NAME" , bootstyle="outlined")
change_company_name_button_tab5.place(x=10 , y=20)


change_invoice_title_button_tab5 = tk.Button(tab5 , text="CHANGE INVOICE TITLE" , bootstyle="outlined" , command=change_invoice_title)
change_invoice_title_button_tab5.place(x=10 , y=50)



change_invoice_logo_button_tab5 = tk.Button(tab5 , text="CHANGE INVOICE LOGO" , bootstyle="outlined" , command=change_logo_settings)
change_invoice_logo_button_tab5.place(x=10 , y=80)


change_hospital_ipd_mode_button_tab5 = tk.Button(tab5 , text="SET HOSPITAL IPD MODE ON OR OFF" , bootstyle="outlined" , command=set_hospital_ipd_mode)
change_hospital_ipd_mode_button_tab5.place(x=10 , y=110)


















#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#































#LOOP rootS:
get_time()
root.mainloop()






