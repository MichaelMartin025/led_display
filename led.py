import tkinter as tk
import time

class Display:
    def __init__(self):
        self.led0 = "white"
        self.led1 = "red"
        self.led2 = "red"
        self.led3 = "white"
        self.led4 = "red"
        self.led5 = "red"
        self.led6 = "red"

    def light_leds(self, num):
        print(type(num), num)
        if num == "0":
            self.led0 = "red"
            self.led1 = "red"
            self.led2 = "red"
            self.led3 = "white"
            self.led4 = "red"
            self.led5 = "red"
            self.led6 = "red"
        if num == "1":
            self.led0 = "white"
            self.led1 = "white"
            self.led2 = "red"
            self.led3 = "white"
            self.led4 = "white"
            self.led5 = "red"
            self.led6 = "white"
        if num == "2":
            self.led0 = "red"
            self.led1 = "white"
            self.led2 = "red"
            self.led3 = "red"
            self.led4 = "red"
            self.led5 = "white"
            self.led6 = "red"
        if num == "3":
            self.led0 = "red"
            self.led1 = "white"
            self.led2 = "red"
            self.led3 = "red"
            self.led4 = "white"
            self.led5 = "red"
            self.led6 = "red"
        if num == "4":
            self.led0 = "white"
            self.led1 = "red"
            self.led2 = "red"
            self.led3 = "red"
            self.led4 = "white"
            self.led5 = "red"
            self.led6 = "white"
        if num == "5":
            self.led0 = "red"
            self.led1 = "red"
            self.led2 = "white"
            self.led3 = "red"
            self.led4 = "red"
            self.led5 = "white"
            self.led6 = "red"
        if num == "6":
            self.led0 = "red"
            self.led1 = "red"
            self.led2 = "white"
            self.led3 = "red"
            self.led4 = "red"
            self.led5 = "red"
            self.led6 = "red"
        if num == "7":
            self.led0 = "red"
            self.led1 = "white"
            self.led2 = "red"
            self.led3 = "white"
            self.led4 = "white"
            self.led5 = "red"
            self.led6 = "white"
        if num == "8":
            self.led0 = "red"
            self.led1 = "red"
            self.led2 = "red"
            self.led3 = "red"
            self.led4 = "red"
            self.led5 = "red"
            self.led6 = "red"
        if num == "9":
            self.led0 = "red"
            self.led1 = "red"
            self.led2 = "red"
            self.led3 = "red"
            self.led4 = "white"
            self.led5 = "red"
            self.led6 = "white"   
    
class DisplayGui:
    def __init__(self, root):
        
        self.spacer_0 = tk.Label(root, width=20).grid(column=0, row=0)
        self.spacer_1 = tk.Label(root, width=10).grid(column=4, row=0)
        self.spacer_2 = tk.Label(root, width=20).grid(column=0, row=6)

        self.label_0 = tk.Label(root, width=5, bg="white")
        self.label_0.grid(column=2, row=1)

        self.label_1 = tk.Label(root, height=3, width=2, bg="white")
        self.label_1.grid(column=1, row=2)

        self.label_2 = tk.Label(root, height=3, width=2, bg="white")
        self.label_2.grid(column=3, row=2)

        self.label_3 = tk.Label(root, width=5, bg="white")
        self.label_3.grid(column=2, row=3)

        self.label_4 = tk.Label(root, height=3, width=2, bg="white")
        self.label_4.grid(column=1, row=4)

        self.label_5 = tk.Label(root, height=3, width=2, bg="white")
        self.label_5.grid(column=3, row=4)

        self.label_6 = tk.Label(root, width=5, bg="white")
        self.label_6.grid(column=2, row=5)

        self.entry_1 = tk.Entry(root, width=5)
        self.entry_1.grid(column=0, row=2)

        self.button_1 = tk.Button(root, text="Enter", command=self.light_leds)
        self.button_1.grid(column=0, row=4)

        self.display = Display()
 
    def light_leds(self):
        num = self.entry_1.get()
        self.display.light_leds(num)
        self.label_0.config(bg=self.display.led0)
        self.label_1.config(bg=self.display.led1)
        self.label_2.config(bg=self.display.led2)
        self.label_3.config(bg=self.display.led3)
        self.label_4.config(bg=self.display.led4)
        self.label_5.config(bg=self.display.led5)
        self.label_6.config(bg=self.display.led6)
              
root = tk.Tk()
#root.geometry("450x650")

display_gui = DisplayGui(root)

root.mainloop()
