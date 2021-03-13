import tkinter as tk
import cam
import register
import pic_to_numpy
window = tk.Tk()
window.title('Face detect App')
window.geometry('320x240')
window.configure(background='white')

def go_to_register():
    name=register_entry.get()
    if(name==""):
        result_label.configure(text="名稱必填!")
        return
    register.main(name)
    pic_to_numpy.main()

header_label = tk.Label(window, text='1092人臉辨識')
header_label.pack()

register_frame = tk.Frame(window)
register_frame.pack(side=tk.TOP)
register_label = tk.Label(register_frame, text='還沒註冊?輸入名稱(英文名)')
register_label.pack(side=tk.LEFT)
register_entry = tk.Entry(register_frame)
register_entry.pack(side=tk.LEFT)

register_btn = tk.Button(window, text='註冊',command=go_to_register)
register_btn.pack()

activate_cam_btn = tk.Button(window, text='啟動人臉辨識',command=cam.camLoop)
activate_cam_btn.pack()

exit_btn = tk.Button(window, text='離開',command=window.destroy)
exit_btn.pack()
result_label = tk.Label(window)
result_label.pack()

window.mainloop()