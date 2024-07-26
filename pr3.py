from tkinter import *
from tkinter import ttk, messagebox
import string, random

# Setting up the main application window
root = Tk()
root.title("Password Generator")
root.geometry("640x480")
root.configure(bg="#f0f0f0")  # Light grey background for the window

class PasswordGenerator:
    def __init__(self, root):
        self.root = root 
        title = Label(self.root, text="Password Generator", font=("Times New Roman", 26, "bold"), bg="#4CAF50", fg="white", relief=GROOVE)
        title.place(x=0, y=0, relwidth=1, height=60)
        self.password_frame = Frame(self.root, bg="#ffffff", bd=2, relief=SUNKEN)
        self.password_frame.place(x=120, y=120, width=400, height=250)
        self.length_label = Label(self.password_frame, text="Enter Length:", font=("Arial", 18, "bold"), fg="#333333", bg="#ffffff")
        self.length_label.grid(row=0, column=0, pady=20, padx=(10, 0), sticky=E)
        self.length_entry = Entry(self.password_frame, font=("Arial", 18), width=10, bd=2, relief=SOLID)
        self.length_entry.grid(row=0, column=1, padx=(0, 10), pady=20, sticky=W)
        self.generate_button = Button(self.password_frame, text="Generate Password", font=("Arial", 16, "bold"), command=self.generate_password, bg="#4CAF50", fg="white", bd=2, relief=RAISED)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=20, ipadx=10, ipady=5, padx=10)
        self.password_label = Label(self.password_frame, text="Generated Password:", font=("Arial", 14, "bold"), fg="#333333", bg="#ffffff")
        self.password_label.grid(row=2, column=0, pady=20, padx=(10, 0), sticky=E)
        self.password_display = Entry(self.password_frame, font=("Arial", 16), state="readonly", width=20, bd=2, relief=SOLID)
        self.password_display.grid(row=2, column=1, padx=(0, 10), pady=20, sticky=W)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be positive.")

            password = self.create_password(length)
            self.password_display.configure(state="normal") 
            self.password_display.delete(0, END)  
            self.password_display.insert(0, password) 
            self.password_display.configure(state="readonly")  
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number for password length.")
            self.clear_password_display()
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            self.clear_password_display()

    def create_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def clear_password_display(self):
        self.password_display.configure(state="normal")
        self.password_display.delete(0, END)
        self.password_display.configure(state="readonly")

password_generator = PasswordGenerator(root)

root.mainloop()
