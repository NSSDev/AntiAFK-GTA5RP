import time
import keyboard
from tkinter import messagebox
messagebox.showinfo(title='AntiAFK-GTA5RP', message='Скрипт AntiAFK-GTA5RP запущен !\n\nРазработчик скрипта: HasimN#7777')
total_seconds = 2700
sleep_seconds = 0
while sleep_seconds < total_seconds:
    sleep_seconds += 10
    time.sleep(10)
    keyboard.press('w')
    time.sleep(10)
    keyboard.release('w')
    time.sleep(10)
    keyboard.press('s')
    time.sleep(10)
    keyboard.release('s')
messagebox.showinfo(title='AntiAFK-GTA5RP', message='Скрипт закончил свою работу !\nДля повторной работы, перезапускайте программу')
