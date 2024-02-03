import pyperclip
from opencc import OpenCC
from tkinter import *

def convert_text():
    simplified_text = input_box.get("1.0", END).strip()
    if simplified_text:
        cc = OpenCC('s2twp')
        traditional_text = cc.convert(simplified_text)
        pyperclip.copy(traditional_text)
        output_box.delete("1.0", END)
        output_box.insert(END, traditional_text)

def copy_output(event):
    output_text = output_box.get("1.0", END).strip()
    if output_text:
        pyperclip.copy(output_text)

root = Tk()
root.title("Chinese Text Converter")

input_label = Label(root, text="Simplified Chinese:")
input_label.pack()

input_box = Text(root, height=5, width=30)
input_box.pack()

convert_button = Button(root, text="Convert", command=convert_text)
convert_button.pack()

output_label = Label(root, text="Traditional Chinese:")
output_label.pack()

output_box = Text(root, height=5, width=30)
output_box.pack()

# Ctrl+C shortcut for direct output
output_box.bind("<Control-c>", copy_output)

root.mainloop()