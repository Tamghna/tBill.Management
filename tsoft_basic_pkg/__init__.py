class time():
    def timenow():
        import time
        from time import strftime

        formatted_date = strftime("%d-%m-%Y %H:%M:%S")
        
        return formatted_date
        
import requests
import os

from tkinter import messagebox

def updates(progress_bar):
        progress_bar.update()

        try:
            print("\n UPDATING                                    \n")



            
            import os
                

            os.mkdir("./temp_downloads")
            import win32con, win32api,os

            file='main.exe'


            #to force deletion of a file set it to normal


            os.chdir("./temp_downloads")



            #GETTING INIT PY
            url1 = 'https://raw.githubusercontent.com/Tamghna/tBill.Management/main/this_app_pkg/__init__.py'
            r1 = requests.get(url1, allow_redirects=True)
            open('__init__.py', 'wb').write(r1.content)
            #---------------------------------------------------------------------------------------------------------#

            for i in range(20):
                time.sleep(0.1)
                progress_bar.update()



            #GETTING main.exe
            url1 = 'https://raw.githubusercontent.com/Tamghna/tBill.Management/main/main.exe'
            r1 = requests.get(url1, allow_redirects=True)
            open('main.exe', 'wb').write(r1.content)
            #---------------------------------------------------------------------------------------------------------#

            for i in range(10):
                time.sleep(0.1)

                progress_bar.update()

            
            #GETTING ver.exe
            url1 = 'https://raw.githubusercontent.com/Tamghna/tBill.Management/main/version.ver'
            r1 = requests.get(url1, allow_redirects=True)
            open('version.ver', 'wb').write(r1.content)
            #---------------------------------------------------------------------------------------------------------#

            for i in range(24):

                progress_bar.update()


            import shutil


            os.chdir("..")

            


            from subprocess import Popen
            p2 = Popen("copy.bat")
            stdout, stderr = p2.communicate()
            progress_bar.update()
            for i in range(10):
                time.sleep(0.1)

                progress_bar.update()

            progress_bar.update()
            for i in range(31):
                time.sleep(0.1)

                progress_bar.update()

 



            from subprocess import Popen
            p2 = Popen("remove2.bat")
            stdout, stderr = p2.communicate()
            progress_bar.update()
            for i in range(10):
                time.sleep(0.1)

                progress_bar.update()





        except Exception as e:
            os.chdir("..")
            
            print(os.getcwd())
            from subprocess import Popen
            p = Popen("remove2.bat")
            stdout, stderr = p.communicate()

            from tkinter import messagebox
            messagebox.showerror("" , "FAILED TO GET THE LATEST UPDATES DUE TO INTERNET PROBLEMS.    |                                                                                                                                                           CLICK OK TO RUN PROGRAM WITHOUT UPDATING                                                                                                                                                                                                                                                                                                                            ERROR:  " + str(e))

   
   









import threading
import time
import sys

class ProgressBar:
    def __init__(self, total):
        self.total = total
        self.progress = 0

    def update(self):
        self.progress += 1
        sys.stdout.write("\r[%-20s] %d%%" % ('=' * int(self.progress / self.total * 20), self.progress / self.total * 100))
        sys.stdout.flush()




progress_bar = ProgressBar(100)
thread = threading.Thread(target=updates, args=(progress_bar,))
thread.start()
thread.join()