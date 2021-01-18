from tkinter import *
from tkinter import messagebox

main_window = Tk()
main_window.title('Kalkulator BMI Sederhana')

main_window.state('normal')
main_window.resizable(False, False)


def reset():
    input_stop.delete(0, END)
    input_start.delete(0, END)
    label_result['text'] = 0


def open_alert_error(msg):
    """
    menampilkan pesan error
    """
    w_alert = Toplevel(main_window)
    w_alert.title("Error")

    lbl_msg = Label(w_alert, text=msg)
    lbl_msg.grid(row=0, column=0)

    btn_ok = Button(w_alert, text="Ok", command=w_alert.destroy)
    btn_ok.grid(row=1, column=1)


def validate_input():
    """
    validasi semua input
    """
    status = True
    if input_start.get() == "":
        status = False
        open_alert_error("waktu mulai masih kosong")
    elif input_stop.get() == "":
        status = False
        open_alert_error("waktu selesai masih kosong")

    return status

# hitung


def hitung():

    if validate_input():
        end = float(input_stop.get())
        mulai = float(input_start.get())

        ab = (end-mulai)
        cd = 10*(end-mulai)
        ef = round(((ab*100)-40))
        gh = round(((ab*100)-40)/10)
        i = int(ab*3000)
        j = (cd/10)*3000
        k = abs(gh*500)
        l = round(cd % 10*500)
        if ((ab % 2) == 0)or(ab == 2):

            label_result['text'] = f"{i}"
        elif((cd % 10) == 0)and(cd >= 0):

            label_result['text'] = f"{j}"
        elif(ab < 0.10):
            label_result['text'] = f"{500}"
        elif(ab % 2) != 0:

            label_result['text'] = f"{k}"
        elif(end < mulai):
            label_result['text'] = f"{0}"
        else:

            label_result['text'] = f"{l}"


# left
judul = Label(main_window, text='Billing Warnet',
              font='arial 20 bold underline')
desc = Label(main_window, text='Harga per 10 menit adalah Rp.500')
start = Label(main_window, text='waktu mulai (j.m)')
stop = Label(main_window, text='waktu selesai')
input_start = Entry(main_window, width=25)
input_stop = Entry(main_window, width=25)
reset = Button(main_window, text='Reset', padx=40, command=reset)
submit = Button(main_window, text='Submit', padx=40, command=hitung)


judul.grid(row=0, columnspan=4)
desc.grid(row=1, column=0, sticky='w')
start.grid(row=3, column=0, sticky='w')
stop.grid(row=5, column=0, sticky='w')
input_start.grid(row=4, column=0, columnspan=2, sticky='w')
input_stop.grid(row=6, column=0, sticky='w')
reset.grid(row=7, column=0, sticky='w')
submit.grid(row=7, column=1, sticky='w')

# right
label_hitung = Label(main_window, text="Hasil Perhitungan", font=("Arial", 8))
label_result = Label(main_window, text="0", font=("Arial", 44))
lbl_cp = Label(main_window, text="Made in Indonesia")


label_hitung.grid(row=1, column=1)
label_result.grid(column=1, row=4, rowspan=2)
lbl_cp.grid(row=8, column=0)
main_window.mainloop()
