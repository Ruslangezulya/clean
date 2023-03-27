from tkinter import *
from tkinter import messagebox
 
def calculate():
   temp = int(xtwo.get())
   time = int(xone.get())
   ud = 1.5541+0.2122*int(time)+0.024*int(temp)
   izm = 2.2903-0.0430*time-0.005*temp  
   messagebox.showinfo('Рассчёт', f'Удельная энергоёмкость мойки составит {ud} кВт/ч Изменение массы деталей после удаления загрязнений составит {izm}% ')
   
 
window = Tk()
window.title('Clean')
window.geometry('700x500')
 
 
frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)
 
 
xone = Label(
   frame,
   text="Введите продолжительность мойки (в минутах)"
)
xone.grid(row=3, column=1)
 
xtwo = Label(
   frame,
   text="Введите температуру ёмкости в процессе мойки (в градусах)",
)
xtwo.grid(row=4, column=1)
 
xone = Entry(
   frame,
)
xone.grid(row=3, column=2, pady=5)
 
xtwo = Entry(
   frame,
)
xtwo.grid(row=4, column=2, pady=5)
 
cal_btn = Button(
   frame,
   text='Рассчитать',
   command = calculate
)
cal_btn.grid(row=5, column=2)
 
window.mainloop()