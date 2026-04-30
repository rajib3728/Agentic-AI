import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3 as sq
from tkinter import messagebox

class AuthScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Login & Register")
        self.root.geometry("900x600+200+100")
        #self.root.resizable(False, False)
        
        # Set color scheme
        self.bg_color = "#1e1e2e"
        self.primary_color = "#6366f1"
        self.secondary_color = "#f97316"
        self.text_color = "#ffffff"
        
        self.root.configure(bg=self.bg_color)
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel (branding)
        self.left_panel = tk.Frame(self.main_frame, bg=self.primary_color)
        self.left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(self.left_panel, text="Welcome", font=("Arial", 40, "bold"), 
                               bg=self.primary_color, fg=self.text_color)
        title_label.pack(pady=30)
        subtitle = tk.Label(self.left_panel, text="to", font=("Arial", 34),
                                bg=self.primary_color, fg=self.text_color)
        subtitle.pack()
        
        subtitle = tk.Label(self.left_panel, text="Agentic AI", 
                           font=("Arial", 34), bg=self.primary_color, fg=self.text_color)
        subtitle.pack()
        
        # Right panel (form)
        self.right_panel = tk.Frame(self.main_frame, bg=self.bg_color)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Form container
        self.form_frame = tk.Frame(self.right_panel, bg=self.bg_color)
        self.form_frame.pack(pady=60, padx=40)
        
        # Buttons to switch views
        button_frame = tk.Frame(self.form_frame, bg=self.bg_color)
        button_frame.pack(pady=10)
        
        self.login_btn = tk.Button(button_frame, text="LOGIN", font=("Arial", 12, "bold"),
                                   bg=self.primary_color, fg=self.text_color, 
                                   width=12, command=self.show_login)
        self.login_btn.pack(side=tk.LEFT, padx=10)
        
        self.register_btn = tk.Button(button_frame, text="REGISTER", font=("Arial", 12, "bold"),
                                      bg=self.secondary_color, fg=self.text_color, 
                                      width=12, command=self.show_register)
        self.register_btn.pack(side=tk.LEFT, padx=10)
        
        # Content frame
        self.content_frame = tk.Frame(self.form_frame, bg=self.bg_color)
        self.content_frame.pack(pady=20)
        
        self.show_login()
    
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_login(self):
        self.clear_content()
        self.login_btn.config(bg=self.primary_color)
        self.register_btn.config(bg="#555555")
        
        # Email
        tk.Label(self.content_frame, text="Email:", font=("Arial", 11), 
                bg=self.bg_color, fg=self.text_color).pack(anchor=tk.W, pady=5)
        email_entry = tk.Entry(self.content_frame, font=("Arial", 10), width=30)
        email_entry.pack(pady=5)
        
        # Password
        tk.Label(self.content_frame, text="Password:", font=("Arial", 11), 
                bg=self.bg_color, fg=self.text_color).pack(anchor=tk.W, pady=5)
        password_entry = tk.Entry(self.content_frame, font=("Arial", 10), width=30, show="*")
        password_entry.pack(pady=5)
        
        # Login button
        tk.Button(self.content_frame, text="LOGIN", font=("Arial", 11, "bold"),
                 bg=self.primary_color, fg=self.text_color, width=20,
                 command=lambda: self.login(email_entry.get(), password_entry.get())).pack(pady=20)
        
        tk.Label(self.content_frame, text="Forgot password?", font=("Arial", 9), 
                bg=self.bg_color, fg=self.primary_color, cursor="hand2").pack()
    
    def show_register(self):
        self.clear_content()
        self.register_btn.config(bg=self.secondary_color)
        self.login_btn.config(bg="#555555")
        
        # Name
        tk.Label(self.content_frame, text="Full Name:", font=("Arial", 11), 
                bg=self.bg_color, fg=self.text_color).pack(anchor=tk.W, pady=5)
        name_entry = tk.Entry(self.content_frame, font=("Arial", 10), width=30)
        name_entry.pack(pady=5)
        
        # Email
        tk.Label(self.content_frame, text="Email:", font=("Arial", 11), 
                bg=self.bg_color, fg=self.text_color).pack(anchor=tk.W, pady=5)
        email_entry = tk.Entry(self.content_frame, font=("Arial", 10), width=30)
        email_entry.pack(pady=5)
        
        # Password
        tk.Label(self.content_frame, text="Password:", font=("Arial", 11), 
                bg=self.bg_color, fg=self.text_color).pack(anchor=tk.W, pady=5)
        password_entry = tk.Entry(self.content_frame, font=("Arial", 10), width=30, show="*")
        password_entry.pack(pady=5)
        
        # Register button
        tk.Button(self.content_frame, text="REGISTER", font=("Arial", 11, "bold"),
                 bg=self.secondary_color, fg=self.text_color, width=20,
                 command=lambda: self.register(name_entry.get(), email_entry.get(), password_entry.get())).pack(pady=20)
    
    def login(self, email, password):
        
        print(f"Logging in: {email}")
        conn=sq.connect("users.db")
        cur=conn.cursor()
       
        sql2="SELECT * FROM users WHERE email=? and password=?"
        cur.execute(sql2,(email,password))
        user=cur.fetchone()
        if user:
            tk.messagebox.showinfo("Login Successful", f"Welcome back, {user[1]}!")
            root.destroy()  # Close the auth screen
            import root1  # Import the main application
        else:
            tk.messagebox.showerror("Login Failed", "No account found with that email.")

    
    def register(self, name, email, password):

        conn=sq.connect("users.db")
        cur=conn.cursor()
        sql1="CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, email TEXT,password TEXT)"
        cur.execute(sql1)
        sql2="INSERT INTO users(name, email, password) VALUES(?, ?, ?)"
        cur.execute(sql2,(name,email,password))
        conn.commit()
        tk.messagebox.showinfo("Registration Successful", f"Welcome, {name}!")
        conn.close()


        print(f"Registering: {name}, {email}")

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap("logo.ico")
    app = AuthScreen(root)
    root.mainloop()