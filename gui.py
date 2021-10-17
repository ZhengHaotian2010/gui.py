import easygui as g
import tkinter
import tkinter.messagebox 
import tkinter.ttk
import windnd
import tkinter.filedialog as tf
import time
def open_path():
    path = tf.askopenfilename()
    return path
def open_io():
    io = tf.askopenfile()
    return path
def msgbox(msg):
    title = g.msgbox(msg=str(msg))
    return title
def enterbox(enter):
    a = g.enterbox(msg=enter,)
    return a
def save():
    save = tf.asksaveasfilename()
    return save
    
#作答区域 正在研制
# def S_open_path():
#     msg = '\n'.join((item.decode("utf-8") for item in files))
#     return msg
# def lgfirst():    
#     tk = tkinter.Tk()
# def lglast():
#     tk.mainloop
# def windnd():
#     windnd.hook_dropfiles(tk,func=S_open_path)
def jdt(speed,butten):
    def show():
        for i in range(100):
            # 每次更新加1
            progressbarOne['value'] = i + 1
            # 更新画面
            root.update()
            time.sleep(speed/100)
        root.destroy()
    root = tkinter.Tk()
    root.geometry('150x120')
    
    progressbarOne = tkinter.ttk.Progressbar(root)
    progressbarOne.pack(pady=20)
    # 进度值最大值
    progressbarOne['maximum'] = 100
    # 进度值初始值
    progressbarOne['value'] = 0
    
    button = tkinter.Button(root, text=butten, command=show)
    button.pack(pady=5)
    
    root.mainloop()
def tktan(txt,buttontxt): 
    window = tkinter.Tk()
    window.title('My Window')
    window.geometry('500x300')
    l = tkinter.Label(window, text=txt, bg='white', font=('Arial', 12), width=30, height=2)
    l.pack()
    b = tkinter.Button(window, text=buttontxt,command=exit).pack()
    window.mainloop()