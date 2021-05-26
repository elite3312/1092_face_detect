#!/usr/bin/env python
# coding: utf-8

# In[7]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import os
import pathlib
import time
import tkinter as tk
import tkinter.messagebox
import register_main_frame
import tsv_query
import tsv_create
import datetime
import cam
class basedesk():
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry('200x200')        
        Login_screen(self.root)
class Login_screen():
    def __init__(self,master):
        
        self.master = master
        self.master.config(bg='white')
        #基準介面initface
        self.Login_screen = tk.Frame(self.master,)
        self.Login_screen.pack()
        label=tk.Label(self.Login_screen,text="員工打卡系統",fg='black',font = ('Arial',14))
        label.pack()
        self.entry=tk.Entry(self.Login_screen,width=20)
        self.entry.pack()
        button = tk.Button(self.Login_screen, text = "Login",bg = 'orange',fg = 'black', command = self.login)
        button.pack()
        
    def get_time(self,):
        seconds = time.time()
        result = time.localtime(seconds)
        tm = str(result.tm_year)+'/'+str(result.tm_mon)+'/'+str(result.tm_mday)
        return tm
    def login(self,):
        path = pathlib.Path().absolute()
        #print(path)
        os.chdir(path)
        f=open(r'ID_list.tsv','r')  
        words=f.readlines()
        #path = os.path.join("Test")
        #file_list = os.listdir(path)
        #flag=0;
        for name in words:
            if(name[len(name)-1]=='\n'):
                words[words.index(name)]=name[0:len(name)-1]
                name = name[0:len(name)-1]#delete the '\n'.
            if(self.entry.get()!=name):
                flag=1
            else:
                tkinter.messagebox.showinfo(title='Welcome!',message='Welcome,{}.'.format(self.entry.get()))
                flag=0
                login_info = dict()
                login_info[name] = self.get_time()
                print(login_info)
                self.Login_screen.destroy()
                user_screen(self.master) 
                guard_id=name
                year=datetime.datetime.now().strftime('%Y')
                month=datetime.datetime.now().strftime('%m')
                day=datetime.datetime.now().strftime('%d')
                
                tsv_create.create_tsv(guard_id,year,month,day)
                return login_info
                break
        if(flag==1):
            tkinter.messagebox.showinfo(title='Login Failed! ',message='Not Found, please try again.')
class user_screen():
    def __init__(self,master):
        
        self.master = master
        self.master.config(bg='white')
        self.user_screen = tk.Frame(self.master,)
        self.user_screen.pack()
        register_btn = tk.Button(self.user_screen, text='註冊',command=self.register)
        register_btn.pack()
        btn = tk.Button(self.user_screen,text='Logout',bg = 'orange',fg = 'black',command=self.logout)
        btn.pack()
        btn = tk.Button(self.user_screen,text='查詢',bg = 'orange',fg = 'black',command=self.query)
        btn.pack()
        activate_cam_btn = tk.Button(self.user_screen,text='啟動人臉辨識',command=cam.camLoop)
        activate_cam_btn.pack()
        self.register_base=register_main_frame.basedesk(master)
        self.tsv_query_base=tsv_query.basedesk(master)

        self.register_base.Register_screen.register_frame.pack_forget()
        self.tsv_query_base.Query_screen.query_frame.pack_forget()
        self.tsv_query_base.Query_screen.show_frame.pack_forget()
    def register(self,):
        self.register_base.Register_screen.register_frame.pack()
        
    def query(self,):
        
        self.tsv_query_base.Query_screen.query_frame.pack()
        self.tsv_query_base.Query_screen.show_frame.pack()
    def logout(self,):       
        self.user_screen.destroy()
        self.register_base.Register_screen.good_bye()
        self.tsv_query_base.Query_screen.good_bye()
        Login_screen(self.master)
if __name__ == '__main__':    
    root = tk.Tk()
    basedesk(root)
    root.mainloop()


# In[7]:


# In[ ]:




