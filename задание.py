from tkinter import *
from tkinter import messagebox
 
def calculate():
   temp = int(xtwo.get())
   time = int(xone.get())
   ud = 1.5541+0.2122*int(time)+0.024*int(temp)
   izm = 2.2903-0.0430*time-0.005*temp  
   messagebox.showinfo('Рассчёт', f'Удельная энергоёмкость мойки составит {ud} кВт/ч Изменение массы деталей после удаления загрязнений составит {izm}% ')
   file = open('Рассчёты.txt','a+')
   file.write('\n!Новая запись\nВведённое значение температуры - ' + str(temp) + ' с\nВведённое значение времени - ' + str(time) + ' мин\nРасчитанное значение удельной энергоёмкости - ' + str(ud) + ' кВт/ч\n Рассчитанное значение изменения массы деталей - ' + str(izm) + ' % ') 
   file.close()
   file = open('Рассчёты.xls','a+')
   file.write('\n!Новая запись\nВведённое значение температуры - ' + str(temp) + ' с\nВведённое значение времени - ' + str(time) + ' мин\nРасчитанное значение удельной энергоёмкости - ' + str(ud) + ' кВт/ч\n Рассчитанное значение изменения массы деталей - ' + str(izm) + ' % ') 
   file.close()
   
   
   
    
def razrab():     
   messagebox.showinfo('О разработчике', f'Разработчик - Гезуля Руслан Алексеевич, ruslan_gezulya@mail.ru ')
   
window = Tk()
window.title('Clean')
window.geometry('700x500')
window.configure(bg='MediumAquaMarine')
 
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
xone.configure(bg='Salmon')
 
xtwo = Label(
   frame,
   text="Введите температуру ёмкости в процессе мойки (в градусах)",
)
xtwo.grid(row=4, column=1)
xtwo.configure(bg='Salmon')
 
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
cal_btn.configure(bg='PaleGreen')

razrab_btn = Button(
   frame,
   text='О разработчике',
   command = razrab
)
razrab_btn.grid(row=5, column=3)
razrab_btn.configure(bg='Pink')

window.mainloop()