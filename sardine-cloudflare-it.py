import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Cloudflare it!!")
root.geometry("800x600")
sardinha_zul = ImageTk.PhotoImage(Image.open("sardinha_azul.png").resize((30, 30)))
sardinha_laranja = ImageTk.PhotoImage(Image.open("sardinha_laranja.png").resize((30, 30)))
canvas = tk.Canvas(root)
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
frame = tk.Frame(canvas)
scrollable_window = canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas.configure(yscrollcommand=scroll_y.set)
def contar_binario(binario):
    return len(binario)
def printBinario(): 
    inp = inputtxt.get(1.0, "end-1c") 
    binario = ' '.join(format(ord(char), '08b') for char in inp)  
    n_letras = contar_binario(binario) 
    lbl.config(text=n_letras)
    for widget in frame.winfo_children():
        widget.destroy()
 #0 é pra sardinhas azuis e 1 para sardinhas laranjas
    row, col = 0, 0
    max_per_row = 20  
    for bit in binario.replace(" ", ""): 
        img = sardinha_laranja if bit == "1" else sardinha_zul
        label = tk.Label(frame, image=img)
        label.grid(row=row, column=col, padx=2, pady=2)
        col += 1
        if col >= max_per_row:
            col = 0
            row += 1
    frame.update_idletasks()
inputtxt = tk.Text(root, height=3, width=50)
inputtxt.pack(pady=10)
printButton = tk.Button(root, text="Sardine-it!", command=printBinario)
printButton.pack()
lbl = tk.Label(root, text="número de caractéres em binário: 0")
lbl.pack()
root.mainloop()