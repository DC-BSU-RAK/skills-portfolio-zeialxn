import tkinter as tk
import random
import os

root = tk.Tk()
root.title("Alexa, Tell Me a Joke")
root.geometry("400x300")
root.config(bg="#010100")
root.iconbitmap("alexa.ico")

txt_file = r"C:\Users\alvin\OneDrive\Desktop\CC Year 2\GitHub\CODE LAB II\skills-portfolio-zeialxn\Assessment 1 - Skills Portfolio\randomJokes.txt"

def display_jokes(filename):
    jokes = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                if "?" not in line:
                    print(f"Skipping malformed line: {line}")
                    continue

                question, punchline = line.split("?", 1)
                jokes.append((question.strip() + "?", punchline.strip()))

    except FileNotFoundError:
        print("Error.")
        jokes = [("File not found.")]

    return jokes

def get_random_joke():
    return random.choice(jokes)

def show_setup():
    global current_joke
    current_joke = get_random_joke()
    question_label.config(text=current_joke[0])
    punchline_label.config(text="")

def show_punchline():
    if current_joke:
        punchline_label.config(text=current_joke[1])

jokes = display_jokes(txt_file)
current_joke = None

question_label = tk.Label(root, text="Click button below to start.", wraplength=350, bg="#010100", fg="#00ebfb", font=("Arial", 12, "italic"))
question_label.pack(pady=(40, 5))

punchline_label = tk.Label(root, text="", wraplength=350, bg="#010100", fg="#00ebfb",font=("Arial", 12, "italic"))
punchline_label.pack(pady=10)

joke_btn = tk.Button(root, text="Load a Joke", bg="#00ebfb",command=show_setup)
joke_btn.pack(pady=5)

punchline_btn = tk.Button(root, text="Show Punchline", bg="#00ebfb",command=show_punchline)
punchline_btn.pack(pady=5)

quit_btn = tk.Button(root, text="Quit", bg="#00ebfb", command=root.quit)
quit_btn.pack(pady=20)

root.mainloop()