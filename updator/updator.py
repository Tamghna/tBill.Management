import requests
import os

from tkinter import messagebox
def run():
    import os
    print(os.getcwd())

    def update():

        try:
                

            os.mkdir("./temp_downloads")
            os.chdir("./temp_downloads")



            #GETTING INIT PY
            url1 = 'https://raw.githubusercontent.com/Tamghna/tBill.Management/main/this_app_pkg/__init__.py'
            r1 = requests.get(url1, allow_redirects=True)
            open('__init__.py', 'wb').write(r1.content)
            #---------------------------------------------------------------------------------------------------------#


            #GETTING main.exe
            url1 = 'https://raw.githubusercontent.com/Tamghna/tBill.Management/main/main.exe'
            r1 = requests.get(url1, allow_redirects=True)
            open('main.exe', 'wb').write(r1.content)
            #---------------------------------------------------------------------------------------------------------#

            import shutil

            print(os.getcwd())
            os.chdir("..")

            src_path = r"temp_downloads\__init__.py"
            dst_path = r"this_app_pkg\__init__.py"
            shutil.copy(src_path, dst_path)
            print('Copied')
            src_path2 = r"temp_downloads\main.exe"
            dst_path2 = r"main.exe"
            shutil.copy(src_path2, dst_path2)
            print('Copied')
            print(os.getcwd())
            os.chdir("temp_files")
            rver = open("lver.v" , 'r').read()
            os.chdir("..")
            with open("version.ver" , 'w')as f:
                f.write(str(rver))

            
            from subprocess import Popen
            p = Popen("remove.bat")
            stdout, stderr = p.communicate()

            from subprocess import Popen
            p2 = Popen("remove2.bat")
            stdout, stderr = p2.communicate()

            from tkinter import messagebox
            messagebox.showinfo("" , "UPDATE COMPLETE | NEW VERSION IS:---    " + str(rver))
        except Exception:
            from tkinter import messagebox
            messagebox.showerror("" , "FAILED TO FETCH UPDATE DUE TO INTERNET PROBLEMS")

   
   

    try:


        os.mkdir("./temp_files")
        os.chdir("./temp_files")
        url3 = 'https://raw.githubusercontent.com/Tamghna/tBill.Management/main/version.ver'
        r3 = requests.get(url3, allow_redirects=True)
        open('lver.v', 'wb').write(r3.content)
        lver1 = open("lver.v" , 'r').read()
        os.chdir("..")

        cver = open("version.ver" , 'r').read()

        
        from subprocess import Popen
        p = Popen("remove.bat")
        stdout, stderr = p.communicate()

        int(cver)
        int(lver1)

        if lver1 > cver:

            if messagebox.askyesnocancel('',"UPDATE IS AVALABLE!   DO YOU WANT TO UPDATE THE SOFTWARE?") == True:
                print("begin")
                update()

            else:
                import os
                import time


                time.sleep(3)

    except Exception:
        from tkinter import messagebox
        messagebox.showerror("" , "FAILED TO CHECK FOR UPDATES BECAUSE:                                                         INTERNET CONNECTION IS NOT AVAILABLE                                                                                                                                                                                                                                                                                                                                                 CLICK OK TO CONTINUE WITHOUT CHECKING FOR UPDATES(THE SOFTWARE WILL FUNCTION NORMALLY WITHOUT CHECKING FOR UPDATES)             IF ANY PROBLEM OCCURS , CONTACT:tamghnaiquebal@gmail.com")
        os.chdir("..")
                
        from subprocess import Popen
        p = Popen("remove.bat")
        stdout, stderr = p.communicate()













