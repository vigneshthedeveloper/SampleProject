import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta, timezone

def create_form():
    root = tk.Tk()
    root.title("Dr. Priya's Eye Hospital")
    root.geometry("800x600")

    style = ttk.Style()
    style.theme_use('clam')  # Use a themed style for better appearance
    style.configure('TLabel', background='lightblue', font=('Arial', 12, 'bold'))
    style.configure('TEntry', font=('Arial', 12))
    style.configure('TCheckbutton', background='lightblue', font=('Arial', 12))
    style.configure('TFrame', background='lightblue')
    style.configure('TButton', font=('Arial', 12, 'bold'))

    # Create a canvas and a scrollbar
    canvas = tk.Canvas(root, bg="lightblue")
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    hospital_info = ttk.Label(scrollable_frame, text="Dr. PRIYA'S EYE HOSPITAL\nNo.1/2, Kambar Street, PRS Nagar, Palavakkam, Chennai - 600 041.\nTimings: 10.00 A.M - 8.00 P.M", justify=tk.CENTER)
    hospital_info.grid(row=0, columnspan=2, pady=10)

    def update_clock():
        india_offset = timedelta(hours=5, minutes=30)
        india_tz = timezone(india_offset)
        current_india_time = datetime.now(india_tz)
        formatted_india_time = current_india_time.strftime('%H:%M:%S')
        time_entry.delete(0, tk.END)
        time_entry.insert(0, formatted_india_time)
        root.after(1000, update_clock)

    time_label = ttk.Label(scrollable_frame, text="Time:")
    time_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    time_entry = ttk.Entry(scrollable_frame)
    time_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    update_clock()

    def update_date():
        india_offset = timedelta(hours=5, minutes=30)
        india_tz = timezone(india_offset)
        current_india_date = datetime.now(india_tz)
        formatted_india_date = current_india_date.strftime('%d-%m-%Y')
        date_entry.delete(0, tk.END)
        date_entry.insert(0, formatted_india_date)
        root.after(60000, update_date)

    date_label = ttk.Label(scrollable_frame, text="Date:")
    date_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)
    date_entry = ttk.Entry(scrollable_frame)
    date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    update_date()

    def regno():
        label = ttk.Label(scrollable_frame, text="Reg No:")
        label.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    regno()

    def patient_name():
        label = ttk.Label(scrollable_frame, text="Patient Name:")
        label.grid(row=4, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    patient_name()

    def Father_Spouse():
        label = ttk.Label(scrollable_frame, text="Father/Spouse:")
        label.grid(row=5, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    Father_Spouse()

    def get_dob():
        birthdate_str = dob_entry.get()
        return datetime.strptime(birthdate_str, "%d-%m-%Y")

    def calculate_age(dob):
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def update_age(*args):
        try:
            dob = get_dob()
            age = calculate_age(dob)
            age_var.set(age)
        except ValueError:
            age_var.set("Invalid date")

    dob_label = ttk.Label(scrollable_frame, text="DOB:")
    dob_label.grid(row=6, column=0, sticky="e", padx=5, pady=5)
    dob_var = tk.StringVar()
    dob_var.trace_add("write", update_age)
    dob_entry = ttk.Entry(scrollable_frame, textvariable=dob_var)
    dob_entry.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    age_label = ttk.Label(scrollable_frame, text="Age:")
    age_label.grid(row=7, column=0, sticky="e", padx=5, pady=5)
    age_var = tk.StringVar()
    age_entry = ttk.Entry(scrollable_frame, textvariable=age_var, state='normal')
    age_entry.grid(row=7, column=1, padx=5, pady=5, sticky="w")

    def Gender():
        label = ttk.Label(scrollable_frame, text="Sex:")
        label.grid(row=8, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=8, column=1, padx=5, pady=5, sticky="w")

    Gender()

    def Allergies():
        label = ttk.Label(scrollable_frame, text="Allergies:")
        label.grid(row=9, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=9, column=1, padx=5, pady=5, sticky="w")

    Allergies()

    def Address():
        label = ttk.Label(scrollable_frame, text="Address:")
        label.grid(row=10, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=10, column=1, padx=5, pady=5, sticky="w")

    Address()

    def Telephone():
        label = ttk.Label(scrollable_frame, text="Telephone:")
        label.grid(row=11, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=11, column=1, padx=5, pady=5, sticky="w")

    Telephone()

    def Occupation():
        label = ttk.Label(scrollable_frame, text="Occupation:")
        label.grid(row=12, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=12, column=1, padx=5, pady=5, sticky="w")

    Occupation()

    def Emailid():
        label = ttk.Label(scrollable_frame, text="Email ID:")
        label.grid(row=13, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=13, column=1, padx=5, pady=5, sticky="w")

    Emailid()

    def hospital():
        label = ttk.Label(scrollable_frame, text="HOW DID YOU KNOW OUR HOSPITAL?")
        label.grid(row=14, columnspan=2, pady=10)
        checkbox1 = ttk.Checkbutton(scrollable_frame, text="Friends")
        checkbox2 = ttk.Checkbutton(scrollable_frame, text="Relatives")
        checkbox3 = ttk.Checkbutton(scrollable_frame, text="Ads")
        checkbox4 = ttk.Checkbutton(scrollable_frame, text="Others")

        checkbox1.grid(row=15, column=0, sticky="w", padx=5, pady=5)
        checkbox2.grid(row=15, column=1, sticky="w", padx=5, pady=5)
        checkbox3.grid(row=16, column=0, sticky="w", padx=5, pady=5)
        checkbox4.grid(row=16, column=1, sticky="w", padx=5, pady=5)

    hospital()

    def problem():
        label = ttk.Label(scrollable_frame, text="FOR WHAT PROBLEM YOU HAVE COME TO THE HOSPITAL?")
        label.grid(row=17, columnspan=2, pady=10)
        checkbox1 = ttk.Checkbutton(scrollable_frame, text="PAIN")
        checkbox2 = ttk.Checkbutton(scrollable_frame, text="REDNESS")
        checkbox3 = ttk.Checkbutton(scrollable_frame, text="WATERING")
        checkbox4 = ttk.Checkbutton(scrollable_frame, text="ITCHING")
        checkbox5 = ttk.Checkbutton(scrollable_frame, text="DECREASED VISION")
        checkbox6 = ttk.Checkbutton(scrollable_frame, text="SWELLING")
        checkbox7 = ttk.Checkbutton(scrollable_frame, text="FB")
        checkbox8 = ttk.Checkbutton(scrollable_frame, text="DISCHARGE")
        checkbox9 = ttk.Checkbutton(scrollable_frame, text="HEADACHE")
        checkbox10 = ttk.Checkbutton(scrollable_frame, text="ROUTINE CHECKUP")

        checkbox1.grid(row=18, column=0, sticky="w", padx=5, pady=5)
        checkbox2.grid(row=18, column=1, sticky="w", padx=5, pady=5)
        checkbox3.grid(row=19, column=0, sticky="w", padx=5, pady=5)
        checkbox4.grid(row=19, column=1, sticky="w", padx=5, pady=5)
        checkbox5.grid(row=20, column=0, sticky="w", padx=5, pady=5)
        checkbox6.grid(row=20, column=1, sticky="w", padx=5, pady=5)
        checkbox7.grid(row=21, column=0, sticky="w", padx=5, pady=5)
        checkbox8.grid(row=21, column=1, sticky="w", padx=5, pady=5)
        checkbox9.grid(row=22, column=0, sticky="w", padx=5, pady=5)
        checkbox10.grid(row=22, column=1, sticky="w", padx=5, pady=5)

    problem()

    def Complaints():
        label = ttk.Label(scrollable_frame, text="Chief Complaints:")
        label.grid(row=23, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=23, column=1, padx=5, pady=5, sticky="w")

    Complaints()

    def history():
        label = ttk.Label(scrollable_frame, text="Past History:")
        label.grid(row=24, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=24, column=1, padx=5, pady=5, sticky="w")

    history()

    def condition():
        label = ttk.Label(scrollable_frame, text="General Condition:")
        label.grid(row=25, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=25, column=1, padx=5, pady=5, sticky="w")

    condition()

    def PG_Power():
        label = ttk.Label(scrollable_frame, text="PG POWER")
        label.grid(row=26, columnspan=2, pady=10)

    PG_Power()

    def OD():
        label = ttk.Label(scrollable_frame, text="OD:")
        label.grid(row=27, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=27, column=1, padx=5, pady=5, sticky="w")

    OD()

    def OS():
        label = ttk.Label(scrollable_frame, text="OS:")
        label.grid(row=28, column=0, sticky="e", padx=5, pady=5)
        entry = ttk.Entry(scrollable_frame)
        entry.grid(row=28, column=1, padx=5, pady=5, sticky="w")

    OS()

    def confirm():
        print("Form confirmed")
        # Add functionality to process form data here

    def cancel():
        root.destroy()

    confirm_button = ttk.Button(scrollable_frame, text="Confirm", command=confirm)
    cancel_button = ttk.Button(scrollable_frame, text="Cancel", command=cancel)

    confirm_button.grid(row=29, column=0, padx=5, pady=20, sticky="e")
    cancel_button.grid(row=29, column=1, padx=5, pady=20, sticky="w")

    root.mainloop()

create_form()
