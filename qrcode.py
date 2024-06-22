import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recognition_System")

        # This part is image labels setting start
        # first header image
        img = Image.open(r"C:\Users\bbruc\PycharmProjects\Face Attendance system\Images_GUI\banner.jpg")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # backgorund image
        bg1 = Image.open(r"C:\Users\bbruc\PycharmProjects\Face Attendance system\Images_GUI\bg3.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        title_lb1 = Label(bg_img, text="Attendance Management System Using Facial Recognition", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        std_img_btn = Image.open(r"C:\Users\bbruc\PycharmProjects\Face Attendance system\Images_GUI\std1.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.student_pannels, image=self.std_img1, cursor="hand2")
        std_b1.place(x=250, y=100, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.student_pannels, text="Student Panel", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=250, y=280, width=180, height=45)

        # ... (repeat for other buttons)

        # Additional button for viewing attendance
        view_attendance_btn = Button(bg_img, command=self.view_attendance, text="View Attendance", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        view_attendance_btn.place(x=1170, y=510, width=180, height=45)

    def generate_qr_code(self):
        # Add code to generate QR code
        pass

    def save_attendance(self, student_id):
        # Add code to save attendance to the database
        pass

    def view_attendance(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="face_recognition"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM student_attendance")
            records = mycursor.fetchall()

            view_window = Toplevel(self.root)
            view_window.title("Attendance Records")

            tree = ttk.Treeview(view_window)
            tree["columns"] = ("ID", "Roll No", "Name", "Time", "Date", "Attendance")
            tree.heading("#0", text="ID")
            tree.column("#0", anchor="center", width=50)
            for col in tree["columns"]:
                tree.heading(col, text=col)
                tree.column(col, anchor="center", width=100)

            for record in records:
                tree.insert("", "end", values=record)

            tree.pack(expand=True, fill="both")

        except Exception as e:
            messagebox.showerror("Error", f"Error fetching attendance records: {str(e)}")

    def student_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_rec(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_pannel(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developr(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def helpSupport(self):
        self.new_window = Toplevel(self.root)
        self.app = Helpsupport(self.new_window)

    def Close(self):
        root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
