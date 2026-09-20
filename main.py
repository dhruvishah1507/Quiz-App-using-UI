import customtkinter as ctk
import random as rd

window = ctk.CTk()
window.geometry("300x500")
window.title("Abacus QuizApp")


score = 0
opt = []
a, b = 0,0
btns=[]
timer = None
hScore = 0

def game():
    global a, b, opt, ans, timer
    timer = window.after(3000,Over)
    a, b = rd.randint(1,10), rd.randint(1,10)
    quest.configure(text=f"{a} + {b} = ?")
    ans = a+b
    opt = [ans, ans+1, ans-1, ans+3]
    rd.shuffle(opt)
    btn1.configure(text=f"{opt[0]}")
    btn2.configure(text=f"{opt[1]}")
    btn3.configure(text=f"{opt[2]}")
    btn4.configure(text=f"{opt[3]}")

def check(i):
    global ans, opt, score, timer
    if ans == opt[i]:
        score+=1
        scorecard.configure(text=f"Score : {score}")
        window.after_cancel(timer)
        game()
    else:
        quest.configure(text=f"Game Over! \n Score : {score}")
        btn1.configure(state="Disabled")
        btn2.configure(state="Disabled")
        btn3.configure(state="Disabled")
        btn4.configure(state="Disabled")

        
def Over():
        quest.configure(text=f"Game Over! \n Score : {score}")
        quest.configure(text=f"Game Over! \n Score : {score}")
        btn1.configure(state="Disabled")
        btn2.configure(state="Disabled")
        btn3.configure(state="Disabled")
        btn4.configure(state="Disabled")

# UI Components

quest = ctk.CTkLabel(window, text="", font=("Vardana",25))
quest.pack(pady=20)

btn1 = ctk.CTkButton(window, text="", font=("Vardana",20), command=lambda: check(0))
btn1.pack(pady=10)
btn2 = ctk.CTkButton(window, text="", font=("Vardana",20), command=lambda: check(1))
btn2.pack(pady=10)
btn3 = ctk.CTkButton(window, text="", font=("Vardana",20), command=lambda: check(2))
btn3.pack(pady=10)
btn4 = ctk.CTkButton(window, text="", font=("Vardana",20), command=lambda: check(3))
btn4.pack(pady=10)

scorecard = ctk.CTkLabel(window, text="Score : 0", font=("Vardana", 20))
scorecard.pack()

game()
window.mainloop()