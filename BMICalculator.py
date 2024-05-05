from tkinter import *

def bmi_calculate():
    height = float(h_entry.get()) # Lay du lieu tu doi tuong lop Entry
    weight = float(w_entry.get())
    bmi = weight/(height**2) # Tinh BMI
    output_label.configure(text='BMI: {:.1f}'.format(bmi)) # Xuat ket qua

# Khoi tao cua so ung dung
root = Tk()
root.title('BMI Calculator')

# Tao cac nhan (label) trong cua so
h_message_label = Label(text='Nhap chieu cao (m)', font=('Verdana', 16))
w_message_label = Label(text='Nhap can nang (kg)', font=('Verdana', 16))
output_label = Label(font=('Verdana', 16))

# Tao textbox nhap lieu
h_entry = Entry(font=('Verdana', 16), width=4)
w_entry = Entry(font=('Verdana', 16), width=4)

# Tao nut lenh (button)
calc_button = Button(text='Tinh', font=('Verdana', 16), command=bmi_calculate)

# Sx vi tri cac doi tuong do hoa
h_message_label.grid(row=0, column=0)
w_message_label.grid(row=1, column=0)
h_entry.grid(row=0, column=1)
w_entry.grid(row=1, column=1)
output_label.grid(row=2, column=1)
calc_button.grid(row=2, column=3, rowspan=2)

# Chay Tkinter voi event loop
mainloop()