import tkinter as tk
import encoder_decoder
from encoder_decoder import buildHuffmanTree
from encoder_decoder import test1,test2,test3,test4

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 1000, height = 1000,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Huffman Coding to compress data.')
label1.config(font=('helvetica', 14))
canvas1.create_window(500, 25, window=label1)
label1.config(bg='pink',fg='black')

label2 = tk.Label(root, text='Type the string to be compressed:')
label2.config(font=('helvetica', 10))
canvas1.create_window(400, 70, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(580, 70, window=entry1)

def huff ():
    
    x1 = entry1.get()
    if x1:
        label3 = tk.Label(root, text= 'Results',font=('helvetica', 15, 'underline'))
        canvas1.create_window(500, 200, window=label3)

        x2=test1(x1)
        x3=test2(x1)
        x4=test3(x1)
        x5=test4(x1)

        label4 = tk.Label(root, text= 'Original String: ',font=('helvetica', 10))
        canvas1.create_window(500, 230, window=label4)

        label5 = tk.Label(root, text=x1,font=('helvetica', 10, 'bold'))
        canvas1.create_window(500, 250, window=label5)

        label6 = tk.Label(root, text= 'Dictionary: ',font=('helvetica', 10))
        canvas1.create_window(500, 270, window=label6)

        label7 = tk.Label(root, text= x2,font=('helvetica', 10, 'bold'))
        canvas1.create_window(500, 290, window=label7)

        label8 = tk.Label(root, text= 'Encoded string: ',font=('helvetica', 10))
        canvas1.create_window(500, 310, window=label8)

        label9 = tk.Label(root, text= x3,font=('helvetica', 10, 'bold'))
        canvas1.create_window(500, 330, window=label9)

        label0 = tk.Label(root, text= 'Decoded String: ',font=('helvetica', 10))
        canvas1.create_window(500, 350, window=label0)

        label11 = tk.Label(root, text= x4,font=('helvetica', 10, 'bold'))
        canvas1.create_window(500, 370, window=label11)
    else:
        label12 = tk.Label(root, text= 'String not entered. Error.',font=('helvetica', 10))
        canvas1.create_window(500, 230, window=label12)





button1 = tk.Button(text='Compress the data', command=huff, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(500, 130, window=button1)

root.mainloop()
