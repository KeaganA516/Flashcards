import tkinter as tk
import random
from tkinter import messagebox
import csv

def load_flashcards(filename):
    flashcards = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            flashcards.append({"question": row["question"], "answer": row["answer"]})
    return flashcards

def show_question():
    question_label.config(text=flash_cards[index]["question"])

def show_answer():
    messagebox.showinfo("Answer", flash_cards[index]["answer"])

def next_card():
    global index
    index = (index + 1) % len(flash_cards)
    show_question()

def previous_card():
    global index
    index = (index - 1) % len(flash_cards)
    show_question()

def shuffle_cards():
    random.shuffle(flash_cards)
    global index
    index = 0
    show_question()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Flash Card App")
    index = 0

    flash_cards = load_flashcards("flashcards.csv")

    question_label = tk.Label(root, text="", font=("Arial", 24))
    question_label.pack(pady=20)

    answer_button = tk.Button(root, text="Show Answer", command=show_answer)
    answer_button.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    previous_button = tk.Button(button_frame, text="Previous", command=previous_card)
    previous_button.pack(side="left", padx=5)

    next_button = tk.Button(button_frame, text="Next", command=next_card)
    next_button.pack(side="left", padx=5)

    shuffle_cards()
    root.mainloop()