from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyautogui
import subprocess
import time
import sqlite3 as sq


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

def fun1():
    
    time.sleep(slider.get())
    conn=sq.connect("location.db")
    cur=conn.cursor()
    sql1="CREATE TABLE IF NOT EXISTS location(id INTEGER PRIMARY KEY, x REAL, y REAL)"
    cur.execute(sql1)
    x,y=pyautogui.position()
    sql2="INSERT INTO location(x, y) VALUES(?, ?)"
    cur.execute(sql2,(int(x),int(y)))
    print(pyautogui.position())
   
    messagebox.showinfo("info","Location Recorded")
    conn.commit()
    conn.close()

def fun2():
    try:
        conn=sq.connect("location.db")
    except:
        messagebox.showerror("error","No locations recorded")
        
    cur=conn.cursor()
    cur.execute("SELECT * FROM location")
    l=cur.fetchall()
    for i in l:
        x=i[1]
        y=i[2]
        print(x,y)
       
        time.sleep(slider.get())
        pyautogui.moveTo(x,y, duration = 1)
        pyautogui.click()
    messagebox.showinfo("info","Work Complete.")
       
    
    conn.close()
def fun3():
    try:
        conn=sq.connect("location.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM location")
        conn.commit()
        conn.close()
        messagebox.showinfo("info","Locations Deleted")
    except:
        messagebox.showerror ("error","sorry can't perform this opeation")     

def fun4():
    time.sleep(slider.get())
    if e1.get()!="":
        pyautogui.write(e1.get())
        pyautogui.press('enter')
    else:
        messagebox.showerror("error","Please enter text to type")     
def refresh_data(dataview):
    for item in dataview.get_children():
        dataview.delete(item)
    conn=sq.connect("location.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM location")
    data=cur.fetchall()
    for row in data:
        dataview.insert("", "end", values=row)
    
    fig=Figure(figsize=(2, 2), dpi=80)
    plot1=fig.add_subplot(111)
    plot1.set_title("Mouse Click Locations")
    plot1.set_xlabel("X Coordinate")
    plot1.set_ylabel("Y Coordinate")
    plot1.plot([row[1] for row in data], [row[2] for row in data], 'ro')
    
    

    
    canvas=FigureCanvasTkAgg(fig, master=f2)
    canvas.draw()

    canvas.get_tk_widget().place(x=650,y=70,width=800,height=600)

try:
    root = Tk()
    root.geometry("1600x900+0+0")
    root.title("Agentic AI")
    root.iconbitmap("logo.ico")
    root.config(bg="white")

   

    conn=sq.connect("users.db")
    cur=conn.cursor()
    sql1="select name from users where id=1"
    cur.execute(sql1)
    name=cur.fetchone()[0]


    f1=Frame(root,bg="black")
    f1.place(x=1500,y=0,width=500,height=1000)
    l1=Label(f1,text="Control Panel",bg="black",fg="white",font=("Arial",20,"bold"))
    l1.place(x=110,y=10,width=250,height=50)

    Button1=Button(f1,text="Record",bg="blue",fg="white",font=("Arial",20),command=fun1)
    Button1.place(x=110,y=100,width=250,height=50)
    Button2=Button(f1,text="Repeat",bg="green",fg="white",font=("Arial",20),command=fun2)
    Button2.place(x=110,y=200,width=250,height=50)
    Button3=Button(f1,text="Delete",bg="red",fg="white",font=("Arial",20),command=fun3)
    Button3.place(x=110,y=300,width=250,height=50)

    e1=Entry(f1,font=("Arial",20))
    e1.place(x=110,y=400,width=250,height=50)
    Button4=Button(f1,text="Type Text",bg="purple",fg="white",font=("Arial",20),command=fun4)
    Button4.place(x=110,y=500,width=250,height=50)
    slider = Scale(
    f1,
    from_=5,          # Minimum value
    to=20,           # Maximum value
    orient="horizontal",  # Horizontal orientation
    length=20,       # Length of the slider in pixels
    tickinterval=5,  # Show tick marks every 20 units
   # Step size (0.5 means half steps)
    # Function to call on change
  
    )
    slider.place(x=110,y=600,width=250,height=70)
    slider.set(5)
    l2=Label(f1,text="Delay (seconds)",bg="grey",fg="white",font=("Arial",12))
    l2.place(x=110,y=670,width=250,height=30)




    f2=Frame(root,bg="grey")

    f2.place(x=0,y=0,width=1500,height=1000)
   
    
    l2=Label(f2,text=f"Welcome {name}",bg="grey",fg="white",font=("Arial",30))
    l2.place(x=500,y=10,height=50)

    b1=Button(f2,text="Open Browser",bg="black",fg="lightgreen",font=("Arial",20),command=lambda: subprocess.run('start microsoft-edge:', shell=True))
    b1.place(x=50,y=100,width=250,height=50)

    b2=Button(f2,text="Open Notepad",bg="black",fg="lightgreen",font=("Arial",20),command=lambda: pyautogui.hotkey('win', 'r') or time.sleep(1) or pyautogui.write('notepad') or pyautogui.press('enter'))
    b2.place(x=350,y=100,width=250,height=50)

    b3=Button(f2,text="Open Calculator",bg="black",fg="lightgreen",font=("Arial",20),command=lambda: pyautogui.hotkey('win', 'r') or time.sleep(1) or pyautogui.write('calc') or pyautogui.press('enter'))
    b3.place(x=350,y=300,width=250,height=50)
    
    b4=Button(f2,text="Open CMD",bg="black",fg="lightgreen",font=("Arial",20),command=lambda: pyautogui.hotkey('win', 'r') or time.sleep(1) or pyautogui.write('cmd') or pyautogui.press('enter'))
    b4.place(x=50,y=300,width=250,height=50)
    b6=Button(f2,text="File Explorer",bg="black",fg="lightgreen",font=("Arial",20),command=lambda: pyautogui.hotkey('win', 'r') or time.sleep(1) or pyautogui.write('explorer') or pyautogui.press('enter'))
    b6.place(x=50,y=200,width=250,height=50)
    b7=Button(f2,text="Open Camera",bg="black",fg="lightgreen",font=("Arial",20),command=lambda: subprocess.run('start microsoft.windows.camera:', shell=True))
    b7.place(x=350,y=200,width=250,height=50)

    dataview=ttk.Treeview(f2, columns=("ID", "X", "Y"), show="headings")
    dataview.heading("ID", text="Serial No")
    dataview.heading("X", text="X Coordinate")
    dataview.heading("Y", text="Y Coordinate")
    dataview.place(x=50,y=700,width=1400,height=250)
    conn=sq.connect("location.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM location")
    data=cur.fetchall()
    for row in data:
        dataview.insert("", "end", values=row)
    conn.close()

    
    fig=Figure(figsize=(2, 2), dpi=80)
    plot1=fig.add_subplot(111)
    plot1.set_title("Mouse Click Locations")
    plot1.set_xlabel("X Coordinate")
    plot1.set_ylabel("Y Coordinate")
    plot1.plot([row[1] for row in data], [row[2] for row in data], 'ro')



    canvas=FigureCanvasTkAgg(fig, master=f2)
    canvas.draw()

    canvas.get_tk_widget().place(x=650,y=70,width=800,height=600)
    
    refresh_button = Button(f1, text="Refresh Data", bg="orange", fg="white", font=("Arial", 12), command=lambda: refresh_data(dataview))
    refresh_button.place(x=110, y=750, width=250, height=50)



    




    root.mainloop()


except:
    messagebox.showerror("error","sorry can't perform this opeation")

# Optional: Add window icon and styling





