import csv
import tkinter as tk
import tkinter.messagebox
class basedesk():
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry('800x800')        
        Query_screen(self.root)
class Query_screen():
    def __init__(self,master):
        
        self.master = master
        self.master.config(bg='white')
        self.query_frame = tk.Frame(self.master,)
        self.query_frame.pack(side=tk.TOP)
        
        header_label = tk.Label(self.query_frame, text='attendence query')
        header_label.pack()



        year_label=tk.Label(self.query_frame, text="年(20xx)")
        year_label.pack(side=tk.LEFT)

        self.year_entry = tk.Entry(self.query_frame)
        self.year_entry.insert(-1,"2021")
        self.year_entry.pack(side=tk.LEFT)


        month_label=tk.Label(self.query_frame, text="月")
        month_label.pack(side=tk.LEFT)

        self.month_entry = tk.Entry(self.query_frame)
        self.month_entry.insert(-1,"5")
        self.month_entry.pack(side=tk.LEFT)


        day_label=tk.Label(self.query_frame, text="日")
        day_label.pack(side=tk.LEFT)

        self.day_entry=tk.Entry(self.query_frame)
        self.day_entry.insert(-1,"23")
        self.day_entry.pack(side=tk.LEFT)




        self.exit_btn = tk.Button(self.query_frame, text='離開',command=self.good_bye)
        self.exit_btn.pack()

        self.show_frame=tk.Frame(self.master,width=600,height=600)
        self.show_frame.pack(side=tk.TOP) #.grid(row=0,column=0)

        self.canvas=tk.Canvas(self.show_frame,bg='#FFFFFF',width=600,height=600,scrollregion=(0,0,500,500))
        query_btn = tk.Button(self.query_frame, text='查詢打卡紀錄',command=self.show_records)
        query_btn.pack()
        self.canvas.pack()
    def show_records(self,):
        year=self.year_entry.get()
        month=self.month_entry.get()
        day=self.day_entry.get()
        year_int=int(year, base=10)
        if (2000>year_int or 4000<year_int):
            
            return
        month_int=int(month, base=10)
        if (0>month_int or 12<month_int):
            
            return
        day_int=int(day, base=10)
        if (0>month_int or 31<month_int):
            
            return
        if(len(month)==1):month="0"+month
        if(len(day)==1):day="0"+day
        try:
            f = open("attendence-record/"+year+"/"+month+"/attendance-record-"+year+"-"+month+"-"+day+".tsv", "r",encoding="utf-8")            
            read_tsv_label=csv. reader(f, delimiter="\t")
            rows_label = list(read_tsv_label)
            f.close()
            b = tk.Entry(self.canvas)
            b.insert ( 0, str(rows_label[0][0]))
            b.grid(row=0, column=0,sticky=tk.E+tk.W)
            b = tk.Entry(self.canvas)
            b.insert (0,str(rows_label[0][1]))
            b.grid(row=0, column=1,sticky=tk.E+tk.W)
            height = len(rows_label)
            for i in range(1,height): #Rows
                b = tk.Entry(self.canvas)
                b.insert (0,str(rows_label[i][0]))
                b.grid(row=i, column=0,sticky=tk.E+tk.W)
                b = tk.Entry(self.canvas)
                b.insert (0,str(rows_label[i][1]))
                b.grid(row=i, column=1,sticky=tk.E+tk.W)
                b = tk.Entry(self.canvas)
                #b.insert (0,str(rows_label[i][2]))
                #b.grid(row=i, column=2,sticky=tk.E+tk.W)
        except IOError:
            print("File not accessible")
            tkinter.messagebox.showinfo(title='record not found!',message='查無打卡紀錄')
            
        
        
    def good_bye(self,):
        self.query_frame.destroy()
        self.show_frame.destroy()
if __name__ == '__main__':    
    root = tk.Tk()
    basedesk(root)
    root.mainloop()          
