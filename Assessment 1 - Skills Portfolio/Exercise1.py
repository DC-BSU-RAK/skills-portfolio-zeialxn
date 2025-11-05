from tkinter import *
import tkinter.messagebox as messagebox # messagebox is for showing popup messages
import random # for generating random numbers & operations

root = Tk()
root.title("Exercise 1 - Maths Quiz")
root.geometry('400x300')
root.config(bg="#451742") # bg color of the window

def destroy(): # function to clear all widgets
    for widget in root.winfo_children():
        widget.destroy()

def randomInt(level): # function to return a number depending on the level
    if level == "Easy":
        return random.randint(1,9) # will generate random number from 1-9
    elif level == "Moderate":
        return random.randint(10,99) # will generate random numbers from 10-99
    else:
        return random.randint(1000,9999) # will generate random numbers from 1000-9999
    
def decideOperation():
    return random.choice(["+", "-"]) # random operation for the questions

def displayProblem(level, score=0, question=1, attempt=1): # function to display the questions
    if question > 10: # stops the questions at number 10 then displays the scores
        displayResults(score)
        return
    
    # storing the result of th function to a variable
    left = randomInt(level) 
    right = randomInt(level) 
    operation = decideOperation() 

    if operation == "-" and left < right: # if the operation is subtraction, and the left number is less than the right number
        left, right = right, left # this is to swap so it won't equal to a negative number

    answer = left + right if operation == "+" else left - right # to calculate the correct answer then store it to the variable

    destroy() # to destroy all the widget on the window

    Label(root, text=f"Question #{question}", bg="#451742", fg="white", font=("Arial", 14)).place(x=50, y=60) # displays the question
    Label(root, text=f"{left} {operation} {right} = ?", bg="#451742", fg="white", font=("Arial", 16)).place(x=50, y=100) # the math problem
    entry = Entry(root, font=("Arial", 12)) # user input
    entry.place(x=50, y=140)
    Button(root, text="Submit", bg="#fc5263", fg="white", # submit button
           command=lambda: correctAns(level, score, question, attempt, entry, answer)).place(x=50, y=200) # calls for the function
    
def correctAns(level, score, question, attempt, entry, answer): # function to check the answer
    try:
        user = int(entry.get()) # converts the entry input to integer
    except:
        messagebox.showwarning("Invalid Input", "Please enter a number.") # if not an int it will show this message
        return
    
    if user == answer: # correct answer
        points = 10 if attempt == 1 else 5 # if the answer on the first attempt is correct it gives 10 points, else only 5 points
        score += points # adds the points to the score
        messagebox.showinfo("Correct!", f"Your answer is correct! You earned {points} points!")
        displayProblem(level, score, question + 1, 1) # displays another question and adds 1 to the question number
    else: # wrong answer
        if attempt == 1: # first attempt
            messagebox.showwarning("Incorrect", "Oops! Try again.") #if incorrect it will display this message
            entry.delete(0, END) # clears the entry input
            Button(root, text="Submit", bg="#fc5263", fg="white",
                   command=lambda: correctAns(level, score, question, 2, entry, answer)).place(x=50, y=200) # allows to call the function again
        else:
            messagebox.showerror("Incorrect", f"The answer is {answer}") # shows correct answer
            messagebox.showinfo("Ran out of Attempts", "Sorry, you did not earn any points for this question.")
            displayProblem(level, score, question + 1, 1)

def displayResults(score):
    destroy()
    Label(root, text=f"Your final score is {score}/100", bg="#451742", fg="white", font=("Arial", 14)).place(x=80, y=70) # displays final score

    # assigns a rank based on the user's score
    if score >= 90:
        rank = "Excellent"
    elif score >= 80:
        rank = "Good"
    elif score >= 70:
        rank = "Fair"
    elif score >= 60:
        rank = "Bad"
    else:
        rank = "Fail"

    Label(root, text=f"Your rank is {rank}. Thank you for playing!", bg="#451742", fg="white", font=("Arial", 12)).place(x=40, y=110) # displays the rank
    Button(root, text="Play Again", bg="#fc5263", fg="white", command=home_screen).place(x=160, y=155) # will display the home screen again
    Button(root, text="Leave", bg="#777f83", fg="white", command=root.destroy).place(x=175, y=190) # will destroy or close the window

def displayMenu(): # function to display the difficulty level
    destroy()
    Label(root, text="Select Difficulty Level", bg="#451742", fg="white", font=("Arial", 14)).place(x=100, y=60)
    Button(root, text="Easy", bg="#fc5263", fg="white",
           command=lambda: displayProblem("Easy")).place(x=175, y=110)
    Button(root, text="Moderate", bg="#fc5263", fg="white",
           command=lambda: displayProblem("Moderate")).place(x=160, y=150)
    Button(root, text="Advanced", bg="#fc5263", fg="white",
           command=lambda: displayProblem("Advanced")).place(x=160, y=190)

def home_screen(): # the starting or home screen that shows title and play button only
    destroy()
    Label(root, text="Math Quiz Game", bg="#451742", fg="white", font=("Arial", 16)).place(x=130, y=90)
    Button(root, text="Play", bg="#fc5263", fg="white", font=("Arial", 14),
           command=displayMenu).place(x=180, y=140)
    
home_screen() # this will show at start
root.mainloop()