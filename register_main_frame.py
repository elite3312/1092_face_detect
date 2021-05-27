import tkinter as tk
import tkinter.messagebox
import cam
import register
import pic_to_numpy
import csv

class basedesk():
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry('800x800')        
        self.Register_screen=Register_screen(self.root)
class Register_screen():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='white')

        self.register_frame = tk.Frame(master)
        self.register_frame.pack(side=tk.TOP)
        header_label = tk.Label( self.register_frame, text='1092人臉辨識註冊介面')
        header_label.pack(side=tk.TOP)
        register_label = tk.Label( self.register_frame, text='輸入ID')
        register_label.pack(side=tk.LEFT)
        self.register_entry = tk.Entry( self.register_frame)
        self.register_entry.pack(side=tk.LEFT)

        self.register_btn = tk.Button( self.register_frame, text='註冊',command=self.go_to_register)
        self.register_btn.pack()

        #activate_cam_btn = tk.Button(master, text='啟動人臉辨識',command=cam.camLoop)
        #activate_cam_btn.pack()

        exit_btn = tk.Button( self.register_frame, text='離開',command=self.good_bye)
        exit_btn.pack()
        self.result_label = tk.Label( self.register_frame)
        self.result_label.pack()

    def good_bye(self,):
        self.register_frame.pack_forget()
        
    def go_to_register(self,):
        name=self.register_entry.get()
        if(name==""):
            self.result_label.configure(text="ID必填!")
            return
        #check dup id
        f = open("ID_list.tsv", "r",encoding="utf-8")            
        read_tsv_id=csv. reader(f, delimiter="\t")
        rows_label = list(read_tsv_id)
        for row in rows_label:
            if(name==row[0]):
                tkinter.messagebox.showinfo(title='DUPLICATE ID!',message=name+'ID已有人使用!')
                print('id already exists')
                return
        f.close()
        file = open("ID_list.tsv", 'a',encoding="utf-8")

        tsv_writer = csv.writer(file,delimiter='\t', lineterminator='\n' )
        tsv_writer.writerow([name])
        file.close()
        tkinter.messagebox.showinfo(title='looks good!',message='請看鏡頭!按下c拍照!按下q退出!')
                
        register.main(name)
        tkinter.messagebox.showinfo(title='looks good!',message='正在產生向量!')
        pic_to_numpy.main()
        tkinter.messagebox.showinfo(title='looks good!',message='員工'+name+'註冊成功!')
        self.good_bye()
if __name__ == '__main__':    
    root = tk.Tk()
    basedesk(root)
    root.mainloop()
