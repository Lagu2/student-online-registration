import tkinter as tk
from tkinter import messagebox
import sqlite3

class StudentRegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration")
        self.root.geometry("500x600")

        # Connect to SQLite database
        self.conn = sqlite3.connect("student_registration.db")
        self.c = self.conn.cursor()

        # Create table if not exists
        self.c.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY,
                            school_name TEXT,
                            date_of_application TEXT,
                            first_name TEXT,
                            last_name TEXT,
                            dob TEXT,
                            gender TEXT,
                            email TEXT,
                            address TEXT,
                            parent_name TEXT,
                            course_name TEXT)''')

        # Header
        self.header_frame1 = tk.Frame(self.root, bg="lightblue", pady=10)
        self.header_frame1.pack(fill=tk.X)
        self.header_frame2 = tk.Frame(self.root, bg="GRAY", pady=10)
        self.header_frame2.pack(fill=tk.X)
        self.school_label = tk.Label(self.header_frame1, text="FULLA SENIOR SECONDARY SCHOOL", font=("CASTELLAR", 25))
        self.school_label.pack()
        self.school_label = tk.Label(self.header_frame2, text="STUDENT ONLINE REGISTRATION FORM", font=("ALGERIAN", 19))
        self.school_label.pack()

        # Form
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=20)

        fields = ["Date of Application", "First Name", "Last Name", "Date of Birth", "Gender",
                  "Email Address", "Address", "Parent's Name", "Course Name"]
        self.entries = {}
        for i, field in enumerate(fields):
            label = tk.Label(self.form_frame, text=field, font=("Times New Roman", 15))
            label.grid(row=i, column=0, sticky="e", padx=10, pady=5)
            entry = tk.Entry(self.form_frame, font=("Arial", 12), width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[field] = entry


        # Footer
        self.footer_frame1 = tk.Frame(self.root, bg="lightgreen", pady=10)
        self.footer_frame1.pack(fill=tk.X, side=tk.BOTTOM)
        self.footer_frame2 = tk.Frame(self.root, bg="lightyellow", pady=10)
        self.footer_frame2.pack(fill=tk.X, side=tk.BOTTOM)
        self.motto_label = tk.Label(self.footer_frame1, text="MOTTO:EDUCATION FOR SERVICE AND DEVELOPMENT", font=("Times New Roman", 18))
        self.motto_label.pack()
        self.address_label = tk.Label(self.footer_frame2, text="ADDRESS:NIMULE ,EASTERN EQUATORIA STATE ,SOUTHERN SUDAN", font=("Times New Roman", 18))
        self.address_label.pack()

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_form, font=("Arial,bold", 14), bg="lightgrey")
        self.submit_button.pack(pady=20)

    def submit_form(self):
        data = {
            "school_name": self.school_label.cget("text"),
            "date_of_application": self.entries["Date of Application"].get(),
            "first_name": self.entries["First Name"].get(),
            "last_name": self.entries["Last Name"].get(),
            "dob": self.entries["Date of Birth"].get(),
            "gender": self.entries["Gender"].get(),
            "email": self.entries["Email Address"].get(),
            "address": self.entries["Address"].get(),
            "parent_name": self.entries["Parent's Name"].get(),
            "course_name": self.entries["Course Name"].get(),
            "photo_path": self.photo_entry.get()
        }

        # Insert data into SQLite database
        self.c.execute('''INSERT INTO students (school_name, date_of_application, first_name, last_name,
                                                dob, gender, email, address, parent_name, course_name)
                                                VALUES (:school_name, :date_of_application, :first_name, 
                                                        :last_name, :dob, :gender, :email, :address, 
                                                        :parent_name, :course_name)''', data)
        self.conn.commit()
        messagebox.showinfo("Success", "Form submitted successfully!")

        # Clear form fields
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.photo_entry.delete(0, tk.END)

root = tk.Tk()
app = StudentRegistrationApp(root)
root.mainloop()
