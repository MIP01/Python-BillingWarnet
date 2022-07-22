from tkinter import *
from tkinter import messagebox


main_window = Tk()
main_window.title('Billing Warnet')

main_window.state('normal')
main_window.resizable(False, False)

    
def reset():
    input_stop.delete(0,END)
    input_start.delete(0,END)
    label_result['text'] = 0
    f = open('history.txt', 'a')

#hitung
def hitung():
    f = open('history.txt', 'a')
    if input_start.get() == '':
        messagebox.showerror("Error", "waktu mulai tidak boleh kosong")
    else:
        if input_stop.get() == '':
            messagebox.showerror("Error", "waktu selesai tidak boleh kosong")            
        else:
            end = float(input_stop.get())
            mulai = float(input_start.get())
            ab=(end-mulai)
            cd=10*(end-mulai)
            ef=round(((ab*100)-40))
            gh=round(((ab*100)-40)/10)
            i=int(ab*3000)
            j=(cd/10)*3000
            k=abs(gh*500)
            l=round(cd%10*500)
            if ((ab % 2)==0)or(ab==2):
                z=int(ab*3000)
                f.write(str(z)+"\n")
                label_result['text'] = f"{i}"
                
            elif((cd % 10)==0)and(cd>=0):
                z=(cd/10)*3000
                f.write(str(z)+"\n")
                label_result['text'] = f"{j}"
                
            elif(ab<0.10):
                f.write(str("500")+"\n")
                f.close()
                label_result['text'] = f"{500}"
                
            elif(ab % 2)!=0:
                z=abs(gh*500)
                f.write(str(z)+"\n")
                label_result['text'] = f"{k}"
                
            elif(selesai<mulai):
                f.write(str("input salah")+"\n")
                label_result['text'] = f"{0}"
                
            else:
                z=round(cd%10*500)
                f.write(str(z)+"\n")
                label_result['text'] = f"{l}"
            f.close()   
    
#left
judul = Label(main_window, text='Billing Warnet',font='arial 20 bold underline')
desc = Label(main_window, text='Biaya per 10 menit adalah\nRp.500', pady=20, font='arial 10')
start = Label(main_window, text='waktu mulai (jj.mm)')
stop = Label(main_window, text='waktu selesai (jj.mm)')
input_start = Entry(main_window, width=25)
input_stop = Entry(main_window, width=25)
reset = Button(main_window, text='Reset', padx=40, command=reset)
submit = Button(main_window, text='Submit', padx=40, command=hitung)


judul.grid(row=0, columnspan=4 )
desc.grid(row=1, column=0, sticky='w')
start.grid(row=3, column=0,sticky='w')
stop.grid(row=5, column=0,sticky='w')
input_start.grid(row=4, column=0, columnspan=2, sticky='w')
input_stop.grid(row=6, column=0,sticky='w')
reset.grid(row=7, column=0,sticky='w')
submit.grid(row=7, column=1,sticky='w')

#right
label_hitung = Label(main_window, text="Total Bayar",font=("Arial bold",8))
label_result = Label(main_window, text="0",font=("Arial",44))
lbl_cp = Label(main_window, text="copyright @ π Team")


label_hitung.grid(row = 1, column=1)
label_result.grid(column=1, row=4, rowspan=2)
lbl_cp.grid(row=8, column=0, columnspan=2)



main_window.mainloop()

