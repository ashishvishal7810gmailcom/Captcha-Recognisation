import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import Menu
import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import create_menu
import cam_open
#import predict_img
import cv2
from time import sleep
from PIL import Image, ImageTk
import cv2
import numpy as np
import pickle
from tkinter.filedialog import askopenfile
import show_demo_image as sdi

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        padx=145
        pady=720
        self._geom='200x200+0+0'
        #master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.geometry("{0}x{1}+360+40".format(master.winfo_screenwidth() - pady, master.winfo_screenheight() - padx))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

def run_progressbar():
    progress_bar['maximum']=100
    for i in range(101):
        sleep(0.01)
        progress_bar['value']=i
        progress_bar.update()
    #root.destroy()

root = tk.Tk(className='Captcha Solver')
app=FullScreenApp(root)

image = Image.open("covid19.jpg")
photo = ImageTk.PhotoImage(image)
create_menu.icon_background(root,photo)
'''panel = Label(root, image = photo)
panel.pack(side = "bottom", fill = "both", expand = "yes")'''
canvas = Canvas(root, width = 850, height = 600)
canvas.pack()
#img = PhotoImage(file="ball.ppm")
canvas.create_image(0,0, anchor=NW, image=photo)
Label(root,text='LOADING MODEL....',font='Didot',bg='AntiqueWhite1',fg='RED').pack()
model = pickle.load(open('new_emnist_model.sav', 'rb'))

progress_bar=ttk.Progressbar(root,orient='horizontal',length=500,mode='determinate')
progress_bar.pack(padx=20,pady=10,ipadx=10,ipady=1)
Label(root,text="",font='Didot',bg='AntiqueWhite1',fg='RED',command=run_progressbar())#.pack(padx=20,pady=10,ipadx=10,ipady=10)

for i in range(10):
    sleep(.01)
Label(root,text="WELCOME for Captcha Solver",font='Didot',bg='AntiqueWhite1',fg='green').pack(padx=20,pady=10,ipadx=10,ipady=10)

root.after(2300,lambda: root.destroy())
root.mainloop()

'''
ans=0
while(ans==0):
    ans=msg.showinfo('Important Info','Be Sure That the Background Must Be Black')
'''

main_window=tk.Tk(className='Captcha Solver')
main_window.resizable(False,False)
create_menu.create_menu_bar(main_window)


Label(main_window,text="NOTE: Hey Become Sure That Final Background of Image Must Be Black",font='Didot',bg='AntiqueWhite1',fg='green').grid(row=0,column=0,padx=10,pady=5,ipadx=10,ipady=0)
Label(main_window,text="Change background either 0 or 1 to achieve above",font='Didot',bg='AntiqueWhite1',fg='green').grid(row=1,column=0,padx=20,pady=10,ipadx=10,ipady=0)


def CAMERA_IMAGE():
    image=cam_open.cam_on()
    r=cv2.selectROI('crop_image',image,showCrosshair=True)
    image = image[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    predic_text = sdi.image_show(image)
    '''predic_text=predict_img.predict_image_(image)
    #print("predict_text :",predic_text)'''
    new_wind=tk.Tk(className='Prediced Value')
    create_menu.create_menu_bar(new_wind)
    Label(new_wind, text='Predicted captcha image :', bg='Aqua', fg='RED', font='Didot').grid(row=0, column=0, pady=10,
                                                                                          padx=10)
    Label(new_wind, text=predic_text, bg='Aqua', fg='RED', font='Didot').grid(row=0, column=1, pady=10,
                                                                                          padx=10)


def take_from_gallery():
    file = askopenfile(mode='r', filetypes=[('images', '*.png'),('image','.*jpg')])
    cnt=0
    path=""
    file=str(file)
    print('file :',file)
    for x in range(len(file)):
        if(file[x]=='\''):
            cnt=cnt+1
        if (cnt == 1 and file[x]!='\''):
            if(file[x]=='/'):
                path=path+'/'
            else:
                path = path + file[x]
        if(cnt==2):
            break
    print(file)
    if(file=='None'):
        msg.showerror('ERROR','Please select some image')
    elif file is not None:
        image=cv2.imread(path,1)
        predic_text=sdi.image_show(image)
        new_wind = tk.Tk(className='Prediced Value')
        Label(new_wind, text='Predicted captcha image :', bg='Aqua', fg='RED', font='Didot').grid(row=0, column=0,
                                                                                                  pady=10,
                                                                                                  padx=10)
        Label(new_wind, text=predic_text, bg='Aqua', fg='RED', font='Didot').grid(row=0, column=1, pady=10,
                                                                                  padx=10)


def Plot_Phase_Modulation():
    final_window = tk.Tk(className='Captcha Solver')
    final_window.resizable(False, False)
    create_menu.create_menu_bar(final_window)
    final_window.configure(background='AntiqueWhite1')
    Label(final_window, text="team name", bg='Aqua', fg='RED', font='Didot').grid(row=0, column=0, pady=10,
                                                                              padx=10)
    Label(final_window, text="Expelliarmus", bg='Aqua', fg='RED', font='Didot').grid(row=0, column=1, pady=10,
                                                                                  padx=10)

    '''final_window = tk.Tk(className='Captcha Solver')
    final_window.resizable(False, False)
    create_menu.create_menu_bar(final_window)
    final_window.configure(background='AntiqueWhite1')
    image = Image.open("C:/Users/DELL/Pictures/tname.png")
    photo1 = ImageTk.PhotoImage(image)
    #create_menu.icon_background(root, photo)
    print("image loaded")
    canva = Canvas(final_window, width=850, height=600)
    canva.pack()
    print("image loaded")
    print('canvas packed')
    # img = PhotoImage(file="ball.ppm")
    canva.create_image(0, 0, anchor=NW, image=photo1)
    #Label(final_window, text='LOADING MODEL....', font='Didot', bg='AntiqueWhite1', fg='RED').pack()
    final_window.mainloop()'''


main_window.configure(background='AntiqueWhite1')
plot_detail=tk.LabelFrame(main_window,text='Captcha prediction',font='Didot',width=450,highlightcolor='pink',highlightbackground='pink',bd=30,bg='Aqua')
plot_detail.grid(row=2,column=0,padx=20,pady=10)
Label(plot_detail,text='Take captcha image',bg='Aqua',fg='RED',font='Didot').grid(row=0,column=0,pady=10,padx=10)
#button1=tk.Button(plot_detail,bg='LightSlateGray',command=plot_resistor,font='Courier',activebackground='blue',activeforeground='red',text='resistor',width=20,height=2).grid(row=1,column=0,padx=5,pady=5)
button1=tk.Button(plot_detail,bg='LightSlateGray',command=CAMERA_IMAGE,font='courier',activebackground='blue',activeforeground='red',text='TAKE BY CAMERA',width=30,height=2).grid(row=1,column=0,padx=5,pady=5)
button2=tk.Button(plot_detail,bg='LightSlateGray',command=take_from_gallery,font='courier',activebackground='blue',activeforeground='red',text='TAKE FROM GALLERY',width=30,height=2).grid(row=2,column=0,padx=5,pady=5)
button3=tk.Button(plot_detail,bg='LightSlateGray',command=Plot_Phase_Modulation,font='courier',activebackground='blue',activeforeground='red',text='Here Is Nothing',width=30,height=2).grid(row=3,column=0,padx=5,pady=5)




'''
main_window1=tk.LabelFrame(main_window,text='Solid State Device',font='Didot',width=350,highlightcolor='pink',highlightbackground='pink',bd=10,bg='Aqua')
main_window1.grid(row=0,column=1,padx=20,pady=10)

Label(plot_device,text='Choose Any One to Plot characetristics',bg='Aqua',fg='RED',font='Didot').grid(row=0,column=0,padx=10,pady=10)
button1=tk.Button(plot_device,bg='LightSlateGray',command='',font='Courier',activebackground='blue',activeforeground='red',text='Resistor',width=20,height=2).grid(row=1,column=0,padx=5,pady=5)
button2=tk.Button(plot_device,bg='LightSlateGray',command='',font='Courier',activebackground='blue',activeforeground='red',text='Diode',width=20,height=2).grid(row=2,column=0,padx=5,pady=5)
button3=tk.Button(plot_device,bg='LightSlateGray',command='',font='Courier',activebackground='blue',activeforeground='red',text='Transistor',width=20,height=2).grid(row=3,column=0,padx=5,pady=5)
'''
'''
scale_thresh = IntVar(main_window)
scale_erode = IntVar(main_window)
scale_dialete = IntVar(main_window)
scale_min_h= IntVar(main_window)
scale_min_s = IntVar(main_window)
scale_min_v = IntVar(main_window)
scale_max_h= IntVar(main_window)
scale_max_s = IntVar(main_window)
scale_max_v = IntVar(main_window)
scale_width=IntVar(main_window)
scale_height=IntVar(main_window)

main_window1=tk.LabelFrame(main_window,text='Captcha prediction',font='Didot',width=450,highlightcolor='pink',highlightbackground='pink',bd=10,bg='Aqua')
main_window1.grid(row=0,column=1,padx=20,pady=10)
Label(main_window1,text='Choose Any One to Plot characetristics',bg='Aqua',fg='RED',font='Didot').grid(row=0,column=0,padx=10,pady=10)


ttk.Label(main_window1, text='threshold value: ').grid(row=1, column=0, sticky=tk.E)
ttk.Label(main_window1, text='No. of times of erode: ').grid(row=2, column=0, sticky=tk.E)
ttk.Label(main_window1, text='No. of times of dialete:').grid(row=3, column=0, sticky=tk.E)
ttk.Label(main_window1, text='Minimum H :').grid(row=4, column=0, sticky=tk.E)
ttk.Label(main_window1, text='Minimum S :').grid(row=5, column=0, sticky=tk.E)
ttk.Label(main_window1, text='Minimum V :').grid(row=6, column=0, sticky=tk.E)
ttk.Label(main_window1, text='Maximum H :').grid(row=7, column=0, sticky=tk.E)
ttk.Label(main_window1, text='Maximum S :').grid(row=8, column=0, sticky=tk.E)
ttk.Label(main_window1, text='Maximum V :').grid(row=9, column=0, sticky=tk.E)
ttk.Label(main_window1, text='Width :').grid(row=10, column=0, sticky=tk.E)
ttk.Label(main_window1, text='Height :').grid(row=11, column=0, sticky=tk.E)


scale_thresh.set(50)
scale_erode.set(2)
scale_dialete.set(2)
scale_min_h.set(0)
scale_min_s.set(0)
scale_min_v.set(0)
scale_max_h.set(180)
scale_max_s.set(180)
scale_max_v.set(180)
scale_width.set(800)
scale_height.set(300)




scale_t = Scale(main_window1, variable=scale_thresh, from_=0, to=255, orient=HORIZONTAL).grid(row=1,
                                                                                                    column=1,
                                                                                                    sticky=tk.EW,
                                                                                                    columnspan=3)
scale_e = Scale(main_window1, variable=scale_erode, from_=0, to=10, orient=HORIZONTAL).grid(row=2,
                                                                                                    column=1,
                                                                                                    sticky=tk.EW,
                                                                                                    columnspan=3)
scale_d = Scale(main_window1, variable=scale_dialete, from_=0, to=10, orient=HORIZONTAL).grid(row=3,
                                                                                                    column=1,
                                                                                                    sticky=tk.EW,
                                                                                                    columnspan=3)
scale_minh = Scale(main_window1, variable=scale_min_h, from_=0, to=360, orient=HORIZONTAL).grid(row=4,
                                                                                                    column=1,
                                                                                                    sticky=tk.EW,
                                                                                                    columnspan=3)
scale_mins = Scale(main_window1, variable=scale_min_s, from_=0, to=180, orient=HORIZONTAL).grid(row=5,
                                                                                                    column=1,
                                                                                                    sticky=tk.EW,
                                                                                                    columnspan=3)
scale_minv = Scale(main_window1, variable=scale_min_v, from_=0, to=180, orient=HORIZONTAL).grid(row=6,
                                                                                                    column=1,
                                                                                                    sticky=tk.EW,
                                                                                                    columnspan=3)
scale_maxh = Scale(main_window1, variable=scale_max_h, from_=0, to=360, orient=HORIZONTAL).grid(row=7,
                                                                                                    column=1,
                                                                                                    sticky=tk.EW,
                                                                                                    columnspan=3)
scale_maxs = Scale(main_window1, variable=scale_max_s, from_=0, to=180, orient=HORIZONTAL).grid(row=8,
                                                                                                    column=1,
                                                                                                    sticky=tk.EW,
                                                                                                    columnspan=3)
scale_maxv = Scale(main_window1, variable=scale_max_v, from_=0, to=180, orient=HORIZONTAL).grid(row=9,
                                                                                                    column=1,
                                                                                                    sticky=tk.EW,
                                                                                                    columnspan=3)
scale_maxw = Scale(main_window1, variable=scale_width, from_=0, to=1000, orient=HORIZONTAL).grid(row=10,
                                                                                                    column=1,
                                                                                                    sticky=tk.EW,
                                                                                                    columnspan=3)
scale_maxhe = Scale(main_window1, variable=scale_height, from_=0, to=1000, orient=HORIZONTAL).grid(row=11,
                                                                                                    column=1,
                                                                                                    sticky=tk.EW,
                                                                                                    columnspan=3)



'''
main_window.mainloop()