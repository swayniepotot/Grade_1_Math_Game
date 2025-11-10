#
# Name: Shreya Sinha, id 752676
# Date: January 18, 2024
# File Name: SS-752676-animal-crossing-flashcards
# Description: This program asks the user for their name, provides instructions
# and offers 4 levels and the option to change the number of questions and
# include negative numbers. Afterwards, it displays math flashcards, and informs
# the user of their results before closing.

#these are the functions that are used to go from page to page
#this function is for the 'submit' button, and takes the user to the next page
#of explanation
def submitname():
    global name
    name = entry_name.get()
    global title_to_nook
    title_to_nook = True
    title_root.destroy()
    
#this one is for the first 'continue' button to go to the second explanation
def continue1():
    global nook_to_nook2
    nook_to_nook2 = True
    nook_root.destroy()

#this one is for the second 'continue' button, and starts the options screen
def continue2():
    global nook2_to_options
    nook2_to_options = True
    nook2_root.destroy()

#this function is for the button that takes us to the math flashcards screen
def start():
    global options_to_flashcards
    options_to_flashcards = True
    options_root.destroy()
    
def done():
    global flashcards_to_results
    flashcards_to_results = True
    flashcards_root.destroy()
    
def stop():
    results_root.destroy()
    
#the next five functions determine the different levels to play with
def level1_clicked():
    global range_max
    range_max = 3
    
    button_lvl1.config(relief=SUNKEN)
    button_lvl2.config(relief=RAISED)
    button_lvl3.config(relief=RAISED)
    button_lvl4.config(relief=RAISED)
    #once the level is selected, the continue button appears
    contbtn = Button(options_root, text="Start", bg="brown",
                     font=("Qlarendon", 40), fg = "orange",
                     command= lambda:[question_num(), start()])
    contbtn.place(x = 455, y= 390)

def level2_clicked():
    global range_max
    range_max = 6
    
    button_lvl1.config(relief=RAISED)
    button_lvl2.config(relief=SUNKEN)
    button_lvl3.config(relief=RAISED)
    button_lvl4.config(relief=RAISED)
    
    contbtn = Button(options_root, text="Start", bg="brown",
                     font=("Qlarendon", 40), fg = "orange",
                     command= lambda:[question_num(), start()])
    contbtn.place(x = 455, y= 390)
    
    
    
def level3_clicked():
    global range_max
    range_max = 9
    
    button_lvl1.config(relief=RAISED)
    button_lvl2.config(relief=RAISED)
    button_lvl3.config(relief=SUNKEN)
    button_lvl4.config(relief=RAISED)
    
    contbtn = Button(options_root, text="Start", bg="brown",
                     font=("Qlarendon", 40), fg = "orange",
                     command= lambda:[question_num(), start()])
    contbtn.place(x = 455, y= 390)
    
def level4_clicked():
    global range_max
    range_max = 12
    
    button_lvl1.config(relief=RAISED)
    button_lvl2.config(relief=RAISED)
    button_lvl3.config(relief=RAISED)
    button_lvl4.config(relief=SUNKEN)
    
    contbtn = Button(options_root, text="Start", bg="brown",
                     font=("Qlarendon", 40), fg = "orange",
                     command= lambda:[question_num(), start()])
    contbtn.place(x = 455, y= 390)
    
    contbtn.place(x = 455, y= 470)
    
    
#these two functions are for whether or not negative numbers are included
def negative_yes():
    global negative
    negative = True
    yes_negative.config(relief=SUNKEN)
    no_negative.config(relief=RAISED)

def negative_no():
    
    yes_negative.config(relief=RAISED)
    no_negative.config(relief=SUNKEN)
    
#this question is used to access the slider data and save it to a variable
def question_num():
    global q_number
    q_number = int(q_slider.get())
    
#this function asks the question on the flashcard page
def ask_question():
    global num1
    global num2
    global operation
    operation = random.choice("+-x")
    num1 = random.randint(1, range_max)
    num2 = random.randint(1, range_max)
    
    if negative == True:
        num1 *=  random.randrange(-1, 1+1, 2)
        num2 *=  random.randrange(-1, 1+1, 2)
    
    op_label.config(text = str(operation))
    num1_label.config(text = str(num1))
    num2_label.config(text = str(num2))

#this function resets the count of correct, incorrect and total questions
def reset():
    global correct
    correct = 0
    global incorrect
    incorrect = 0
    global total
    total = 0
    
    correct_label.config(text = str(correct))
    incorrect_label.config(text = str(incorrect))
    total_questions_label.config(text = str(total))
    
#this function submits the user's inputted answer, and checks whether or 
#not it's correct
def click_submit():
    global total
    global correct
    global incorrect
    global answer
    global correct_answer
    
    submit_button.config(text = "Submit")
    try: 
        user_answer = int(entry_answer.get())
        if operation == 'x':
            correct_answer = num1 * num2
            
        elif operation == '+':
            correct_answer = num1 + num2
            
        elif operation == '-':
            correct_answer = num1 - num2
            
        elif operation == '%':
            correct_answer = num1 % num2

        if user_answer == correct_answer:
            answer = "Correct! That is the right answer."
            total += 1
            correct += 1
            bar["value"] = int(bar["value"]) + 1
        else:
            answer = "Wrong! That is not the right answer."
            total += 1
            incorrect += 1
        bar["value"] = int(bar["value"]) + (100 / q_number)
            

    except:
        answer = "Invalid input! Please enter an integer."
    answer_label.config(text = str(answer))
    correct_label.config(text = str(correct))
    incorrect_label.config(text = str(incorrect))
    total_questions_label.config(text = str(total))
    
    entry_answer.delete(0,END)
    
    if total < q_number:
        ask_question()
    else:
        done()

#main GUI begins
#importing libraries
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import *
import random

#defining variables
name = ""
level = 0
range_max = 4
counter = 0
correct = 0
incorrect = 0
total = 0
answer = ""
correct_answer = 0
operation = ""
num1 = 0
num2 = 0
q_number = 10

title_to_nook = False
nook_to_nook2 = False
nook2_to_options = False
options_to_flashcards = False
flashcards_to_results = False
negative = False


#Main program
#title page, runs until condition to change pages is true
while title_to_nook == False: 
    title_root = Tk()
    title_root.title("Animal Crossing Math Flashcards")
    title_root.geometry("800x600")

    title_bg = PhotoImage(file='titleimg3.png')

    label_title_bg = Label(title_root, image = title_bg)
    label_title_bg.place(x = 0, y = 0)

    entry_name = Entry(title_root, width=10, bg="#783f04",
                       font=("Qlarendon", 16), fg = "orange",
                       insertbackground= "orange")
    entry_name.place(x = 450, y = 395)

    entry_button = Button(title_root, text="Submit", bg="#783f04",
                 font=("Qlarendon", 12), fg = "orange", command=submitname)
    entry_button.place(x = 485, y = 445)
                
    entry_name.focus()
    
    info_text = "Use the mouse to click submit, or press the 'enter' key" + \
                " to continue"

    info_move = Label(title_root, text=info_text, bg="#fff8e5",
                              font=("Qlarendon", 10), fg = "black")
    info_move.place(relx = 0.5, y=555, anchor = CENTER)
    
    title_root.bind('<Return>',lambda event:submitname())
    
        
    title_root.mainloop()
#if the condition to move pages becomes true, this code runs the second page
    if title_to_nook == True:
        nook_root = Tk()
        nook_root.title("Animal Crossing Math Flashcards")
        nook_root.geometry("800x600")

        nook_bg = PhotoImage(file='nook.png')

        label_nook_bg = Label(nook_root, image = nook_bg)
        label_nook_bg.place(x = 0, y = 0)

        button_cont1 = Button(nook_root, text="Continue", bg="#783f04",
                           font=("Qlarendon", 14), fg = "orange",
                           command=continue1)
        button_cont1.place(x = 350, y= 555)
        
        nookspeech1 = "I have an announcement to make; " + name + " is" \
+ "\njoining us on the island! We are \nholding a special contest to " + \
"celebrate their \narrival: a math flashcard competition!"

        label_speech1 = Label(nook_root, text=nookspeech1, bg="#fff8e5",
                              font=("Qlarendon", 20), fg = "black")
        label_speech1.place(relx = 0.5, y=455, anchor = CENTER)
        
        nook_root.bind('<Return>',lambda event:continue1())
        
        nook_root.after(1, lambda: nook_root.focus_force())

        nook_root.mainloop() 
     
#page 3 where nook continues explaining
if nook_to_nook2 == True:
    nook2_root = Tk()
    nook2_root.title("Animal Crossing Math Flashcards")
    nook2_root.geometry("800x600")

    nook_bg2 = PhotoImage(file='nook.png')

    label_nook_bg2 = Label(nook2_root, image = nook_bg2)
    label_nook_bg2.place(x = 0, y = 0)

    button_cont2 = Button(nook2_root, text="Continue", bg="#783f04",
                          font=("Qlarendon", 14), fg = "orange",
                          command=continue2)
    button_cont2.place(x = 350, y= 555)
    
    nookspeech2 = "The contest rules are determined by the guest\n of honor, " \
    + name + " themself. What kind \nof rules would you like in the game, " \
    + name + "?"

    label_speech2 = Label(nook2_root, text=nookspeech2, bg="#fff8e5",
                          font=("Qlarendon", 20), fg = "black")
    label_speech2.place(relx = 0.5, y= 455, anchor = CENTER)
    
    nook2_root.bind('<Return>',lambda event:continue2())
    
    nook2_root.after(1, lambda: nook2_root.focus_force())
    
    nook2_root.mainloop()

#options page where settings are selected
if nook2_to_options == True:
    options_root = Tk()
    options_root.title("Animal Crossing Math Flashcards")
    options_root.geometry("800x600")
    
    options_bg = PhotoImage(file='optionsbg.png')
    label_options_bg = Label(options_root, image = options_bg)
    label_options_bg.place(x = 0, y = 0)

    button_lvl1 = Button(options_root, text="Level 1", bg="#b45f06",
                 font=("Qlarendon", 22), fg = "orange",
                 command = level1_clicked)
    button_lvl1.place(x = 100, y= 125)

    button_lvl2 = Button(options_root, text="Level 2", bg="#b45f06",
                 font=("Qlarendon", 22), fg = "orange",
                 command = level2_clicked)
    button_lvl2.place(x = 100, y= 215)

    button_lvl3 = Button(options_root, text="Level 3", bg="#b45f06",
                 font=("Qlarendon", 22), fg = "orange",
                 command = level3_clicked)
    button_lvl3.place(x = 100, y= 305)

    button_lvl4 = Button(options_root, text="Level 4", bg="#b45f06",
                 font=("Qlarendon", 22), fg = "orange",
                 command = level4_clicked)
    button_lvl4.place(x = 100, y= 395)
    
    yes_negative = Button(options_root, text="Yes", bg="#b45f06",
                 font=("Qlarendon", 14), fg = "orange",
                 command = negative_yes)
    yes_negative.place(x = 400, y= 240)

    no_negative = Button(options_root, text="No", bg="#b45f06",
                 font=("Qlarendon", 14), fg = "orange",
                 command = negative_no)
    no_negative.place(x = 480, y= 240)
    no_negative.config(relief=SUNKEN)
        
    q_slider = Scale(options_root, from_=0, to=100,
               orient="horizontal", background='#b45f06', fg='orange',
               troughcolor='#73B5FA', activebackground='#1065BF',
               font=("Qlarendon", 14))
    q_slider.set(10)
    q_slider.place(x=420, y=140)
    
    options_root.after(1, lambda: options_root.focus_force())

    options_root.mainloop()

#flashcards page
if options_to_flashcards == True:
    flashcards_root = Tk()
    flashcards_root.title("Animal Crossing Math Flashcards")
    flashcards_root.geometry("800x600")

    flashcard_bg = PhotoImage(file='flashcardbg.png')

    label_flashcard_bg = Label(flashcards_root, image = flashcard_bg)
    
    label_flashcard_bg.place(x = 0, y = 0)

    entry_answer = Entry(flashcards_root, width=3, bg="#783f04",
                         font=("Qlarendon", 70), fg = "orange",
                         insertbackground= "orange")
    entry_answer.place(x = 570, y = 145)
    
    button_reset = Button(flashcards_root, text="Reset", bg="#783f04",
                          font=("Qlarendon", 14), fg = "orange",
                          command = reset)
    button_reset.place(x = 550, y= 555)
    
    correct_label = Label(flashcards_root, font=('Qlarendon', 15)\
                          ,text=str(correct),\
                          bg="#b45f06", fg = "orange")
    correct_label.place(x=270, y=485)

    incorrect_label = Label(flashcards_root, font=('Qlarendon', 15)\
                            ,text=str(incorrect)\
                            , bg="#b45f06", fg = "orange")
    incorrect_label.place(x=250, y=530)

    total_questions_label = Label(flashcards_root, font=('Qlarendon', 15)\
                                  ,text=str(total)\
                                  , bg="#b45f06", fg = "orange")
    total_questions_label.place(x=350, y=575)
    
    answer_text = "Input your answer and press submit to try it!"
    answer_label = Label(flashcards_root, text=answer_text,
                         font=('Qlarendon', 20), bg="#b45f06", fg = "orange")
    answer_label.place(relx = 0.5, y=440, anchor = CENTER)
    
    op_label= Label(flashcards_root, text="0", bg="#783f04",
                         font=("Qlarendon", 70), fg = "orange", width=2)
    op_label.place(x = 225, y= 145)

    num1_label= Label(flashcards_root, text="0", bg="#783f04",
                         font=("Qlarendon", 70), fg = "orange", width=2)
    num1_label.place(x = 105, y= 145)

    num2_label= Label(flashcards_root, text="0", bg="#783f04",
                         font=("Qlarendon", 70), fg = "orange", width=2)
    num2_label.place(x = 345, y= 145)
    
    submit_button = Button(flashcards_root, text="Submit",
                           font=("Qlarendon", 25), bg="#b45f06", fg = "orange",
                          command = click_submit)
    submit_button.place(x=550, y=270)
    
    style = ttk.Style()
    style.theme_use("default")
    style.configure("black.Horizontal.TProgressbar", background = "#b45f06")
    bar = Progressbar(flashcards_root, length = 500,
                      style="black.Horizontal.TProgressbar")
    bar["value"] = 0
    bar.place(relx = 0.5, y = 100, anchor = CENTER)

    ask_question()
    
    flashcards_root.bind('<Return>',lambda event:click_submit())
        
    flashcards_root.mainloop()

#results page
if flashcards_to_results == True:
    results_root = Tk()
    results_root.title("Animal Crossing Math Flashcards")
    results_root.geometry("800x600")

    results_bg = PhotoImage(file='nook.png')

    label_results_bg = Label(results_root, image = results_bg)
    label_results_bg.place(x = 0, y = 0)

    nookspeech2 ="Congratulations, " + name + "! \nYou scored " + str(correct) \
                  + " out of " + str(total) + "! \nThanks for playing!"

    label_speech2 = Label(results_root, text=nookspeech2, bg="#fff8e5",
                          font=("Qlarendon", 20), fg = "black")
    label_speech2.place(relx = 0.5, y= 455, anchor = CENTER)
    
    button_cont2 = Button(results_root, text="Bye bye!", bg="#783f04",
                          font=("Qlarendon", 14), fg = "orange",
                          command=stop)
    button_cont2.place(x = 360, y= 555)
    
    results_root.bind('<Return>',lambda event:stop())
    
    results_root.after(1, lambda: results_root.focus_force())
        
    results_root.mainloop()
