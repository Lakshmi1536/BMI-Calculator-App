import csv
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
def savefile():
    print('Saved!')
    username = usernametxt.get()
    userage = useragetxt.get()
    userheight = userheighttxt.get()
    userweight = userweighttxt.get()
    userbmi =bmi_label.cget("text")
    usercategory = category_label.cget("text")
    with open('bmiusers.csv','a')as filewriter:
        filewritercsv=csv.writer(filewriter)
        filewritercsv.writerow([username,userage,userheight,userweight,userbmi,usercategory])
# Calculate BMI based on weight (kg) and height (m)

def calculate_bmi():
    try:
        weight_kg = float(userweighttxt.get())
        height_cm = float(userheighttxt.get())
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        bmi = round(bmi, 1)
        display_bmi(bmi)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid weight and height.")
# Display BMI and corresponding category
def display_bmi(bmi):
    bmi_label.config(text=f"Your BMI Value : {bmi:.1f}")
    bmi_category = get_bmi_category(bmi)
    category_label.config(text=f"You Fall in the category of : {bmi_category}")

# Determine BMI category
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def show_bmi_barchart():
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    bmi_values = [18.5, 24.9, 29.9, 100]
    plt.bar(categories, bmi_values, color=["blue", "green", "orange", "red"])
    plt.xlabel("BMI Category")
    plt.ylabel("BMI Value")
    plt.title("BMI Categories")
    plt.show()
def show_bmi_pichart():
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    bmi_values = np.array([18.5, 24.9, 29.9, 100])
    plt.pie(bmi_values, labels=categories)
    plt.legend(title="Four Categories:")
    plt.show()


window = tk.Tk()
window.title("BMI Calculator")

frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

userinputframe=tk.LabelFrame(frame,text='User Input')
userinputframe.grid(row=0,column=0,sticky='news')

userinputname=tk.Label(userinputframe,text='Name:')
userinputname.grid(row=0,column=0,padx=10,pady=10)
usernametxt=tk.Entry(userinputframe)
usernametxt.grid(row=0,column=1,padx=10,pady=10)

userinputage = tk.Label(userinputframe, text="Age:")
userinputage.grid(row=0, column=2,padx=10,pady=10)
useragetxt=tk.Entry(userinputframe)
useragetxt.grid(row=0,column=3,padx=10,pady=10)

gender=(('Male'),
        ('Female'))
# Gender Label
lcstmsex = tk.Label(userinputframe, font=("helvetica", 10), text="Gender:")
lcstmsex.grid(row=1, column=0)

# Radio Button
v = tk.IntVar()
v.set(0)  # Default value (0 corresponds to no selection)
r1 = tk.Radiobutton(userinputframe, text="Female", value=1, variable=v)
r1.grid(row=1, column=1)

r2 = tk.Radiobutton(userinputframe, text="Male", value=2, variable=v)
r2.grid(row=1, column=2)

r3 = tk.Radiobutton(userinputframe, text="Other", value=3, variable=v)
r3.grid(row=1, column=3)

userinputheight = tk.Label(userinputframe, text="Height (cm):")
userinputheight.grid(row=2, column=0,padx=10,pady=10)
userheighttxt=tk.Entry(userinputframe)
userheighttxt.grid(row=2,column=1,padx=10,pady=10)

userinputweight = tk.Label(userinputframe, text="Weight (kg):")
userinputweight.grid(row=2, column=2,padx=10,pady=10)
userweighttxt=tk.Entry(userinputframe)
userweighttxt.grid(row=2,column=3,padx=10,pady=10)

calculate_button = tk.Button(userinputframe, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, column=0,padx=10,pady=10)

resultframe=tk.LabelFrame(frame,text='Result')
resultframe.grid(row=1,column=0,sticky='news')

bmi_label = tk.Label(resultframe, text="")
bmi_label.grid(row=0, columnspan=2)

category_label = tk.Label(resultframe, text="")
category_label.grid(row=1, columnspan=2)

chart_button = tk.Button(userinputframe, text="Show BMI Chart", command=show_bmi_barchart)
chart_button.grid(row=3, column=1,padx=10,pady=10)

chart_button = tk.Button(userinputframe, text="Show PI Chart", command=show_bmi_pichart)
chart_button.grid(row=3, column=2,padx=10,pady=10)

save_button=tk.Button(userinputframe,text='Save',command=savefile)
save_button.grid(row=3,column=3,padx=10,pady=10)

window.mainloop()
