from tkinter import *
from tkinter import ttk
import psutil
from time import sleep
import data_record

# Создание окна программы
root = Tk()

root.title("Уровень загруженности")

root.geometry("600x400")

counter2 = True  # вспомогательная переменная для управления циклом в основной функции


def start1():
    """
    основная функция работы программы с выводом результатов измерений на экран и
    записью результатов измерений в базу данных
    """
    counter = int(value_data_on.get())
    counter1 = 0
    global counter2
    counter2 = True
    sys_start['text'] = 'СТОП'
    sys_start['command'] = stop
    while counter2:
        value_cp['text'] = f'Загрузка ЦП: {centprocessor():.2f} %'
        value_cp.update()
        value_ram['text'] = f'ОЗУ: свободно {ram_free():.6f} Гб, всего {ram():.6f} Гб'
        value_ram.update()
        value_hdd['text'] = f'ПЗУ: свободно {hdd_free():.6f} Гб, всего {hdd():.6f} Гб'
        value_hdd.update()
        m, s = divmod(int(counter1), 60)
        value_timer['text'] = f'Время работы {'{:02d} : {:02d}'.format(m, s)} сек.'
        value_timer.update()
        counter1 += counter
        data_record.recording(centprocessor(), ram_free(), ram(), hdd_free(), hdd())
        sleep(counter)


def stop():
    # функция остановки / перезапуска программы
    global counter2
    counter2 = False
    sys_start['text'] = 'СТАРТ'
    sys_start['command'] = start1


value_cp = ttk.Label(root, text='0')  # строка с процентом загрузки процессора
value_cp.pack(anchor='nw', padx=20, pady=30)
value_ram = ttk.Label(root, text='0')  # строка состояния оперативной памяти
value_ram.pack(anchor='nw', padx=20, pady=20)
value_hdd = ttk.Label(root, text='0')  # строка состояния жесткого диска
value_hdd.pack(anchor='nw', padx=20, pady=20)

value_data = ttk.Label(root, text='Введите интервал измерений:')  # информационная строка
value_data.pack(anchor='s')
value_data_on = ttk.Entry(root, width=12)  # окно ввода интервала измерений
value_data_on.pack(anchor='s')

sys_start = ttk.Button(root, text='СТАРТ', command=start1)  # кнопка запуска / остановки программы
sys_start.pack(anchor='s')

value_timer = ttk.Label(root, text='0')  # окно времени работы программы
value_timer.pack(anchor='s')


def centprocessor():  # процент загруженности процессора
    return psutil.cpu_percent()


def ram():  # определяем размер оперативной памяти
    return psutil.virtual_memory().total / 1024 ** 3


def ram_free():  # определяем свободную часть оперативной памяти
    return psutil.virtual_memory().free / 1024 ** 3


def hdd():  # определяем объем HDD
    return psutil.disk_usage('/').total / 2 ** 30


def hdd_free():  # определяем свободное место на HDD
    return psutil.disk_usage('/').free / 2 ** 30


# Запуск программы
root.mainloop()
