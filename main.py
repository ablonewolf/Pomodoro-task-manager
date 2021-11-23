from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    reps = reps + 1
    work_sec = WORK_MIN * 60
    shrt_brk_sec = SHORT_BREAK_MIN * 60
    lng_brk_sec = LONG_BREAK_MIN * 60
    if (reps % 2 != 0):
        count_down(work_sec)
        titlelabel.config(text="Work",fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW, highlightthickness=0)
    elif(reps==8):
        count_down(lng_brk_sec)
        titlelabel.config(text="Break", fg=RED, font=(FONT_NAME, 40, "bold"), bg=YELLOW, highlightthickness=0)
    elif(reps==2 or reps==4 or reps==6):
        count_down(int(shrt_brk_sec))
        titlelabel.config(text="Break", fg=PINK, font=(FONT_NAME, 40, "bold"), bg=YELLOW, highlightthickness=0)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if(count_sec<10):
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if(count>0):
        window.after(1000, count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

titlelabel = Label(text="Timer")
titlelabel.config(fg=GREEN,font=(FONT_NAME,40,"bold"),bg=YELLOW, highlightthickness=0)
titlelabel.grid(column=1, row=0)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_ing = PhotoImage(file="tomato.png")
canvas.create_image(100,110, image=tomato_ing)
timer_text = canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.config(fg="black",bg="white")
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0)
reset_button.config(fg="black", bg="white")
reset_button.grid(column=2,row=2)

check_mark = Label(text="✔",fg=GREEN, bg=YELLOW, font=40)
check_mark.grid(column=1,row=3)

window.mainloop()
