import tkinter as tk
from encoder_decoder import buildHuffmanTree,test1,test2,test3,test4
import table_dict
from table_dict import run1
root= tk.Tk()
root.title('Huffman Compression')



def run():

    canvas1 = tk.Canvas(root, width = 1000, height = 500,  relief = 'raised',bg='sky blue')
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

            button0 = tk.Button(text='Clear Screen', command=lambda: [label3.destroy(),label4.destroy(),label5.destroy(),label6.destroy(),label7.destroy(),label8.destroy(),label9.destroy(),label0.destroy(),label11.destroy(),button0.destroy(),button00.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(580, 158, window=button0)
            button00=tk.Button(text='View dictionary as table',command=lambda: run1,bg='red',fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(450,158,window=button00)

        else:
            label12 = tk.Label(root, text= 'String not entered. Error.',font=('helvetica', 10))
            canvas1.create_window(500, 230, window=label12)
            button0 = tk.Button(text='Clear Screen', command=lambda: [label12.destroy(),button0.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(500, 158, window=button0)




    button1 = tk.Button(text='Compress the data', command=huff, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(500, 130, window=button1)
    

    

    root.mainloop()
