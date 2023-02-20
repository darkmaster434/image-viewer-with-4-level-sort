import tkinter as tk
from tkinter import filedialog
import os
import shutil
from PIL import Image, ImageTk, UnidentifiedImageError
# from win32api import GetSystemMetrics
# screen_width = GetSystemMetrics(0)-200 #get screen width
# screen_height = GetSystemMetrics(1)-200 #get screen height
screen_width = 1366  # get screen width
screen_height = 766  # get screen height
main_window_x = screen_width-200
main_window_y = screen_height-200

image_resize_precentage = 55  # %
img_width = int((image_resize_precentage/100)*main_window_y)
img_height = int((image_resize_precentage/100)*main_window_x)

global img1, img2, c


class MYGUI():
    def __init__(self) -> None:
        global img1, img2, c
        c = 0
        self.root = tk.Tk()
        self.root.title('Sorter')
        self.root.geometry(str(screen_width)+'x'+str(screen_height))
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        self.menu = tk.Menu(self.root)
        self.menu.add_command(label="Set Dirctory", command=self.get_dir)
        self.menu.add_command(label="Status", command=self.get_status)

        self.root.config(menu=self.menu)
        Label = tk.Label(self.root, foreground='RED', font=(
            'Airal', 36), borderwidth=2, relief='solid')
        Label.grid(column=0, columnspan=3, row=0,
                   rowspan=3, sticky=tk.W+tk.E+tk.S+tk.N)
        if os.path.exists('config'):
            conf = open('config', 'r').readlines()
            if len(conf) == 3:
                err = ''
                for i in conf:
                    i = i.replace('\n', '')
                    if not os.path.exists(i):
                        err += f'{i} not exist\n'
                if err != '':
                    Label.config(text=err)
                else:
                    plain_path = conf[0].replace('\n', '')
                    wire_path = conf[1].replace('\n', '')
                    sort_path = conf[2].replace('\n', '')
                    wire_img = os.listdir(wire_path)

                    def LABEL():
                        self.img_label = tk.Label(
                            self.root, text=wire_img[c], font=('Arial', 20))
                        self.img_label.grid(
                            row=0, column=2, sticky=tk.W+tk.E+tk.S+tk.N)

                        self.img_label = tk.Label(
                            self.root, text=f'Total Image Left:{len(wire_img)}', font=('Arial', 20))
                        self.img_label.grid(
                            row=0, column=1, sticky=tk.W+tk.E+tk.S+tk.N)
                    LABEL()

                    def IMAGE1():
                        global img2
                        try:
                            t = Image.open(
                                plain_path+'/'+wire_img[c].replace('png', 'jpg'))
                            t = t.resize(
                                (img_width, img_height), Image.LANCZOS)
                            img2 = ImageTk.PhotoImage(t)
                            self.photo_label2 = tk.Label(self.root, image=img2)
                            self.photo_label2.grid(
                                row=1, column=0, sticky=tk.W+tk.E+tk.S+tk.N)
                        except UnidentifiedImageError:
                            self.photo_label2 = tk.Label(
                                self.root, text="NOT IMAGE")
                            self.photo_label2.grid(
                                row=0, column=0, sticky=tk.W+tk.E+tk.S+tk.N)
                        except FileNotFoundError:
                            self.photo_label2 = tk.Label(
                                self.root, text="IMAGE NOT FOUND",font=('Arial',20))
                            self.photo_label2.grid(
                                row=1, column=0, sticky=tk.W+tk.E+tk.S+tk.N)

                    def IMAGE2():
                        global img1
                        try:
                            t = Image.open(wire_path+'/'+wire_img[c])
                            t = t.resize(
                                (img_width, img_height), Image.LANCZOS)
                            img1 = ImageTk.PhotoImage(t)
                            self.photo_label1 = tk.Label(self.root, image=img1)
                            self.photo_label1.grid(
                                row=1, column=2, sticky=tk.W+tk.E+tk.S+tk.N)
                        except UnidentifiedImageError:
                            print('NOT IMGS')
                            self.photo_label1 = tk.Label(
                                self.root, text="NOT IMAGE")
                            self.photo_label1.grid(
                                row=0, column=2, sticky=tk.W+tk.E+tk.S+tk.N)
                        except FileNotFoundError:
                            print('NOT IMGS')
                            self.photo_label1 = tk.Label(
                                self.root, text="IMAGE NOT FOUND",font=('Arial',20))
                            self.photo_label1.grid(
                                row=0, column=2, sticky=tk.W+tk.E+tk.S+tk.N)

                    IMAGE1()
                    btn_fram = tk.Frame(
                        self.root, relief='solid', borderwidth=2)

                    def NEXXT():
                        global c
                        c += 1
                        IMAGE1()
                        IMAGE2()
                        LABEL()

                    def BACKK():
                        global c
                        c -= 1
                        IMAGE1()
                        IMAGE2()
                        LABEL()

                    def DENSE1():
                        folder_path = os.path.join(sort_path, 'Dense1')
                        if not os.path.exists(folder_path):
                            os.mkdir(folder_path)
                        file_path = os.path.join(folder_path, wire_img[c])
                        if not os.path.exists(file_path):
                            shutil.move(wire_path+'/'+wire_img[c], file_path)
                            wire_img.pop(c)
                        NEXXT()

                    def DENSE2():
                        folder_path = os.path.join(sort_path, 'Dense2')
                        if not os.path.exists(folder_path):
                            os.mkdir(folder_path)
                        file_path = os.path.join(folder_path, wire_img[c])
                        if not os.path.exists(file_path):
                            shutil.move(wire_path+'/'+wire_img[c], file_path)
                            wire_img.pop(c)
                        NEXXT()

                    def DENSE3():
                        folder_path = os.path.join(sort_path, 'Dense3')
                        if not os.path.exists(folder_path):
                            os.mkdir(folder_path)
                        file_path = os.path.join(folder_path, wire_img[c])
                        if not os.path.exists(file_path):
                            shutil.move(wire_path+'/'+wire_img[c], file_path)
                            wire_img.pop(c)
                        NEXXT()

                    def DENSE4():
                        folder_path = os.path.join(sort_path, 'Dense4')
                        if not os.path.exists(folder_path):
                            os.mkdir(folder_path)
                        file_path = os.path.join(folder_path, wire_img[c])
                        if not os.path.exists(file_path):
                            shutil.move(wire_path+'/'+wire_img[c], file_path)
                            wire_img.pop(c)
                        NEXXT()

                    def DELETE():
                        if os.path.exists(wire_path+'/'+wire_img[c]):
                            os.remove(wire_path+'/'+wire_img[c])
                            wire_img.pop(c)
                            NEXXT()
                    button1 = tk.Button(btn_fram, text="NEXT", font=(
                        'Arial', 20), command=NEXXT)
                    button1.pack(expand=1, fill='both')
                    button2 = tk.Button(btn_fram, text="DENSE 1", font=(
                        'Arial', 20), command=DENSE1)
                    button2.pack(expand=1, fill='both')
                    button3 = tk.Button(btn_fram, text="DENSE 2", font=(
                        'Arial', 20), command=DENSE2)
                    button3.pack(expand=1, fill='both')
                    button4 = tk.Button(btn_fram, text="DENSE 3", font=(
                        'Arial', 20), command=DENSE3)
                    button4.pack(expand=1, fill='both')
                    button5 = tk.Button(btn_fram, text="DENSE 4", font=(
                        'Arial', 20), command=DENSE4)
                    button5.pack(expand=1, fill='both')
                    button6 = tk.Button(btn_fram, text="BACK", font=(
                        'Arial', 20), command=BACKK)
                    button6.pack(expand=1, fill='both')
                    button7 = tk.Button(btn_fram, text="Delete", font=(
                        'Arial', 20), background='Red', command=DELETE)
                    button7.pack(expand=1, fill='both')

                    btn_fram.grid(row=1, column=1, sticky=tk.W+tk.E+tk.S+tk.N)
                    IMAGE2()

            else:
                Label.config(text='Config File Contain More/Less Then 3 Path')
        else:
            Label.config(text='Config Not Found')

        self.root.mainloop()

    def get_dir(self):
        self.root.withdraw()
        newWindow = tk.Toplevel(self.root, padx=10, pady=10)
        newWindow.title("Directory")
        newWindow.geometry(str(main_window_x)+'x'+str(main_window_y))
        newWindow.columnconfigure(0)
        newWindow.columnconfigure(1, weight=1)
        newWindow.columnconfigure(2)
        dir_name1 = tk.Label(newWindow, text='Plain Directory', font=(
            'Arial', 20)).grid(column=0, row=0, padx=10, pady=10)
        dir_path1 = tk.Label(newWindow, relief=tk.SUNKEN, font=('Arial', 20))
        dir_path1.grid(row=0, column=1, sticky=tk.W +
                       tk.E+tk.S+tk.N, padx=10, pady=10)

        dir_btn1 = tk.Button(newWindow, text="Browse", command=lambda: self.set_dir(dir_path1), font=(
            'Arial', 20)).grid(row=0, column=2, sticky=tk.W+tk.E+tk.S+tk.N, padx=10, pady=10)

        dir_name2 = tk.Label(newWindow, text='Semantics', font=('Arial', 20)).grid(
            column=0, row=1, sticky=tk.W+tk.E+tk.S+tk.N, padx=10, pady=10)
        dir_path2 = tk.Label(newWindow, relief=tk.SUNKEN, font=('Arial', 20))
        dir_path2.grid(row=1, column=1, padx=10, pady=10,
                       sticky=tk.W+tk.E+tk.S+tk.N)
        dir_btn2 = tk.Button(newWindow, text="Browse", command=lambda: self.set_dir(dir_path2), font=(
            'Arial', 20)).grid(row=1, column=2, sticky=tk.W+tk.E+tk.S+tk.N, padx=10, pady=10)

        dir_name3 = tk.Label(newWindow, text='Sort folder', font=('Arial', 20)).grid(
            column=0, row=2, sticky=tk.W+tk.E+tk.S+tk.N, padx=10, pady=10)
        dir_path3 = tk.Label(newWindow, relief=tk.SUNKEN, font=('Arial', 20))
        dir_path3.grid(row=2, column=1, padx=10, pady=10,
                       sticky=tk.W+tk.E+tk.S+tk.N)
        dir_btn3 = tk.Button(newWindow, text="Browse", command=lambda: self.set_dir(dir_path3), font=(
            'Arial', 20)).grid(row=2, column=2, sticky=tk.W+tk.E+tk.S+tk.N, padx=10, pady=10)

        if os.path.exists('config'):
            conf = open('config', 'r').readlines()
            if len(conf) > 0:
                dir_path1.config(text=conf[0].replace('\n', ''))
                dir_path2.config(text=conf[1].replace('\n', ''))
                dir_path3.config(text=conf[2].replace('\n', ''))

        def confirm():
            ff = open('config', 'w')
            s1 = dir_path1.cget('text')
            if s1=='':
                s1=os.path.expanduser("~\Desktop")
            ff.writelines(s1+'\n')
            s2 = dir_path2.cget('text')
            if len(s2) != 0:
                ff.writelines(s2+'\n')
            s3 = dir_path3.cget('text')
            if len(s3) != 0:
                ff.writelines(s3+'\n')
            ff.close()
            self.root.deiconify()
            newWindow.destroy()
            self.root.destroy()
            MYGUI()
        newWindow.protocol('WM_DELETE_WINDOW', confirm)
        button = tk.Button(newWindow, text="OK", command=confirm, background='pink',width=100,font=('Arial',20))
        button.grid(column=0, columnspan=3, sticky=tk.S+tk.N, padx=10, pady=10)

    def set_dir(self, m):
        path = filedialog.askdirectory(initialdir='/')
        m.config(text=path)

    def get_status(self):
        nw = tk.Toplevel(self.root, padx=10, pady=10)
        nw.title("Status")
        l = tk.Label(nw,font=('Arial',20))
        s=''
        if os.path.exists('config'):
            conf = open('config', 'r').readlines()
            if len(conf) == 3:
                err = ''
                for i in conf:
                    i = i.replace('\n', '')
                    if not os.path.exists(i):
                        err += f'{i} not exist\n'
                if err != '':
                    l.config(text=err,foreground="Red")
                else:
                    sort_path = conf[2].replace('\n', '')
                    t_sort=0
                    t=False
                    for i in os.walk(sort_path):
                        if t:
                            t_sort+=len(i[2])
                            f=i[0].split('\\')[-1]
                            s+=f'{f}:{len(i[2])}\n'
                        t=True
                    s+=f'Total Sorte:{t_sort}'
                

            else:
                l.config(text='Config File Contain More/Less Then 3 Path',foreground="Red")

        else:
            l.config(text='Config not exist',foreground="Red")
        l.config(text=s,foreground='salmon')   
        l.pack()


MYGUI()
