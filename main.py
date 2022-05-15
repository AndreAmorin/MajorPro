from ctypes.wintypes import WPARAM
import tkinter as tk
import time
import threading
import random

#Major Project by Andre Amorin
#Aurora Collage and Macintyre High School

class SpeedTypeGameGUI:

    def __init__(self):
        #Graphical User Interface
        self.root = tk.Tk()
        self.root.title("Major Project - Typing Speed - Andre Amorin")
        self.root.geometry("800x600")

        self.texts = open("sentence.txt", "r").read().split("\n")

        self.frame = tk.Frame(self.root)

        self.first_label = tk.Label(self.frame, text=random.choice(self.texts) ,font=("Helevetica", 18))
        self.first_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Helevetica", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start) #Change to KeyRelease from KeyPress

        self.speed_label = tk.Label(self.frame, text="Speed: \n0.00 CPS\n0.00 CMP\n0.00 WPS\n0.00 WPS",font=("Helevetica", 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, font=("Helevetica", 20))
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    #Definitions

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]: #Google!
                self.running = True
                t = threading.Thread(target=self.time_thread) 
                t.start()
        if not self.first_label.cget("text").startswith(self.input_entry.get()):
            self.input_entry.config(fg="red") #when input is wrong
        else:
            self.input_entry.config(fg="black") #when input is typing
        if self.input_entry.get() == self.first_label.cget("text")[:-1]:
            self.running = False
            self.input_entry.config(fg="green") #when input is right

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            CPS = len(self.input_entry.get()) / self.counter
            CPM = CPS * 60
            WPS = len(self.input_entry.get().split(" ")) / self.counter
            WPM = WPS * 60
            self.speed_label.config(text=f"Speed: \n{CPS:.2f} CPS\n{CPM:.2f} CPM\n{WPS:.2f} WPS\n{WPM:.2f} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed \n0.00 CPS\n0.00 CMP\n 0.00 WPS\n0.00 WPS")
        self.first_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, tk.END)

SpeedTypeGameGUI()
