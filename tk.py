from tkinter import *
import tkinter as tk
from encoder_decoder import buildHuffmanTree, return_decoded, return_dict, return_encoded, return_freq
from table_dict import run1,run2
import webbrowser

url="https://en.wikipedia.org/wiki/Huffman_coding"




def run():

    root = tk.Tk()
    root.title('Huffman Compression')

    canvas1 = tk.Canvas(root, width=1000, height=500,
                        relief='raised', bg='sky blue')
    canvas1.pack()
    

    label1 = tk.Label(root, text='Huffman Coding to compress data.')
    label1.config(font=('helvetica', 20))
    canvas1.create_window(500, 25, window=label1)
    label1.config(bg='pink', fg='black')






    b = tk.Button(text='i', command=lambda: webbrowser.open(url,new=0,autoraise=True), bg='blue', font=('times', 13, "bold italic"), fg='white')
    canvas1.create_window(990, 20, window=b)






    label2 = tk.Label(root, text='Type the string to be compressed:')
    label2.config(font=('helvetica', 14))
    canvas1.create_window(350, 70, window=label2)
    label2.config(bg='sky blue', fg='black')

    entry1 = tk.Entry(root, width=30, font=('helvetica', 12))
    canvas1.create_window(650, 70, window=entry1)



    def clear_entry(e):
        e.delete(0, END)
        e.insert(0, "")


    def huff():

        x1 = entry1.get()
        btn1=tk.Button(root,command=lambda: clear_entry(entry1),bg='red', fg='white', font=('helvetica', 9, 'bold'),text="x")
        canvas1.create_window(800,70,window=btn1)
        if x1:


            buildHuffmanTree(x1)
            label00 = tk.Label(text='Data is compressed.', bg='brown',
                               fg='white', font=('helvetica', 12, 'bold'))
            canvas1.create_window(500, 130, window=label00)

            options = ["Original String", "Encoded String",
                       "Decoded String", "Dictionary", "Frequency Table", "View all"]
            variable = StringVar(root)
            variable.set("Select an option")

            w = OptionMenu(root, variable, *options)
            canvas1.create_window(500, 170, window=w)

            def view():
                opt = variable.get()

                if opt == "Original String":
                    label3 = tk.Label(root, text='Results', font=(
                        'helvetica', 15, 'underline'))
                    canvas1.create_window(500, 200, window=label3)
                    label3.config(bg='sky blue', fg='black')

                    label4 = tk.Label(
                        root, text='Original String: ', font=('helvetica', 10))
                    canvas1.create_window(500, 230, window=label4)
                    label4.config(bg='sky blue', fg='black')

                    label5 = tk.Label(root, text=x1, font=(
                        'helvetica', 10, 'bold'))
                    canvas1.create_window(500, 250, window=label5)
                    label5.config(bg='sky blue', fg='black')

                    button0 = tk.Button(text='Clear Screen', command=lambda: [label00.destroy(), label3.destroy(), label4.destroy(), label5.destroy(), button0.destroy(), w.destroy(), button.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650, 130, window=button0)





                if opt == "Encoded String":
                    label3 = tk.Label(root, text='Results', font=(
                        'helvetica', 15, 'underline'))
                    canvas1.create_window(500, 200, window=label3)
                    label3.config(bg='sky blue', fg='black')



                    label4 = tk.Label(
                        root, text='Encoded String: ', font=('helvetica', 10))
                    canvas1.create_window(500, 230, window=label4)
                    label4.config(bg='sky blue', fg='black')

                    x2=return_encoded(x1)

                    ss="(Length= "+str(len(x2))+")"
                    label88 = tk.Label(
                        root, text=ss, font=('helvetica', 10, 'italic'))
                    canvas1.create_window(600, 230, window=label88)
                    label88.config(bg='sky blue', fg='black')

                    label5 = tk.Label(root, text=x2, font=(
                        'helvetica', 10, 'bold'))
                    canvas1.create_window(500, 250, window=label5)
                    label5.config(bg='sky blue', fg='black')

                    button0 = tk.Button(text='Clear Screen', command=lambda: [label88.destroy(),label00.destroy(), label3.destroy(), label4.destroy(), label5.destroy(), button0.destroy(), w.destroy(), button.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650, 130, window=button0)












                if opt == "Decoded String":
                    label3 = tk.Label(root, text='Results', font=(
                        'helvetica', 15, 'underline'))
                    canvas1.create_window(500, 200, window=label3)
                    label3.config(bg='sky blue', fg='black')

                    label4 = tk.Label(
                        root, text='Decoded String: ', font=('helvetica', 10))
                    canvas1.create_window(500, 230, window=label4)
                    label4.config(bg='sky blue', fg='black')

                    x2=return_decoded(x1)

                    label5 = tk.Label(root, text=x2, font=(
                        'helvetica', 10, 'bold'))
                    canvas1.create_window(500, 250, window=label5)
                    label5.config(bg='sky blue', fg='black')

                    button0 = tk.Button(text='Clear Screen', command=lambda: [label00.destroy(), label3.destroy(), label4.destroy(), label5.destroy(), button0.destroy(), w.destroy(), button.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650, 130, window=button0)






                if opt == "Frequency Table":

                    button0 = tk.Button(text='Clear Screen', command=lambda: [label00.destroy(), button0.destroy(), w.destroy(), button.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650, 130, window=button0)
                    run2(return_freq(x1))












                if opt == "Dictionary":
                    label3 = tk.Label(root, text='Results', font=(
                        'helvetica', 15, 'underline'))
                    canvas1.create_window(500, 200, window=label3)
                    label3.config(bg='sky blue', fg='black')

                    label4 = tk.Label(
                        root, text='Dictionary: ', font=('helvetica', 10))
                    canvas1.create_window(500, 230, window=label4)
                    label4.config(bg='sky blue', fg='black')

                    x2=return_dict(x1)


                    label5 = tk.Label(root, text=x2, font=(
                        'helvetica', 10, 'bold'))
                    canvas1.create_window(500, 250, window=label5)
                    label5.config(bg='sky blue', fg='black')

                    button00 = tk.Button(text='View dictionary as table', command=lambda: run1(x2),
                                         bg='red', fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650, 230, window=button00)

                    button0 = tk.Button(text='Clear Screen', command=lambda: [button00.destroy(), label00.destroy(), label3.destroy(), label4.destroy(), label5.destroy(), button0.destroy(), w.destroy(), button.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650, 130, window=button0)

















                elif opt == "View all":
                    label3 = tk.Label(root, text='Results', font=(
                        'helvetica', 15, 'underline'))
                    canvas1.create_window(500, 200, window=label3)
                    label3.config(bg='sky blue', fg='black')

                    #buildHuffmanTree(x1)
                    x2 = return_dict(x1)
                    x3 = return_encoded(x1)
                    x4 = return_decoded(x1)
                    x5=return_freq(x1)

                    label4 = tk.Label(
                        root, text='Original String: ', font=('helvetica', 10))
                    canvas1.create_window(500, 230, window=label4)
                    label4.config(bg='sky blue', fg='black')

                    button000 = tk.Button(text='View Frequency table', command=lambda: run2(x5),
                                         bg='red', fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650, 230, window=button000)


                    label5 = tk.Label(root, text=x1, font=(
                        'helvetica', 10, 'bold'))
                    canvas1.create_window(500, 250, window=label5)
                    label5.config(bg='sky blue', fg='black')

                    label6 = tk.Label(root, text='Dictionary: ',
                                      font=('helvetica', 10))
                    canvas1.create_window(500, 270, window=label6)
                    label6.config(bg='sky blue', fg='black')

                    label7 = tk.Label(root, text=x2, font=(
                        'helvetica', 10, 'bold'))
                    canvas1.create_window(500, 290, window=label7)
                    label7.config(bg='sky blue', fg='black')

                    label8 = tk.Label(
                        root, text='Encoded string: ', font=('helvetica', 10))
                    canvas1.create_window(500, 310, window=label8)
                    label8.config(bg='sky blue', fg='black')

                    ss="(Length= "+str(len(x3))+")"
                    label88 = tk.Label(
                        root, text=ss, font=('helvetica', 10, 'italic'))
                    canvas1.create_window(600, 310, window=label88)
                    label88.config(bg='sky blue', fg='black')


                    label9 = tk.Label(root, text=x3, font=(
                        'helvetica', 10, 'bold'))
                    canvas1.create_window(500, 330, window=label9)
                    label9.config(bg='sky blue', fg='black')

                    label0 = tk.Label(
                        root, text='Decoded String: ', font=('helvetica', 10))
                    canvas1.create_window(500, 350, window=label0)
                    label0.config(bg='sky blue', fg='black')

                    label11 = tk.Label(
                        root, text=x4, font=('helvetica', 10, 'bold'))
                    canvas1.create_window(500, 370, window=label11)
                    label11.config(bg='sky blue', fg='black')

                    button00 = tk.Button(text='View dictionary as table', command=lambda: run1(x2),
                                         bg='red', fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650, 270, window=button00)

                    button0 = tk.Button(text='Clear Screen', command=lambda: [label88.destroy(),button000.destroy(), label00.destroy(), label3.destroy(), label4.destroy(), label5.destroy(), label6.destroy(), label7.destroy(), label8.destroy(
                    ), label9.destroy(), label0.destroy(), label11.destroy(), button0.destroy(), button00.destroy(), w.destroy(), button.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650, 130, window=button0)


            button = Button(root, text="Show", command=lambda: view())
            canvas1.create_window(600, 170, window=button)

        else:
            label12 = tk.Label(
                root, text='Error! String not entered.', font=('helvetica', 13))
            canvas1.create_window(500, 230, window=label12)
            label12.config(bg='sky blue', fg='black')

            button0 = tk.Button(text='Clear Screen', command=lambda: [label12.destroy(
            ), button0.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(500, 162, window=button0)

    button1 = tk.Button(text='Compress the data', command=huff,
                        bg='brown', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(500, 130, window=button1)

    root.mainloop()


if __name__ == '__main__':
    run()