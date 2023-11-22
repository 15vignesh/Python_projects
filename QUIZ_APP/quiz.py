import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self):
        self.quiz_data = [
            {
                "question": "What is the capital of Japan?",
                "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"],
                "correct_answer": 0
            },
            {
                "question": "Who wrote the novel 'Pride and Prejudice'?",
                "options": ["Jane Austen", "Emily Bronte", "Charlotte Bronte", "Louisa May Alcott"],
                "correct_answer": 0
            },
            {
                "question": "What is the chemical symbol for the element Gold?",
                "options": [ "Ag", "Au", "Cu", "Fe"],
                "correct_answer": 1
            },
        ]
        self.current_question_index = 0
        self.score = 0
        self.option_selected=None

        self.window = tk.Tk()
        self.window.title("Quiz App")

        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()

        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame, text="", width=30, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_question_button = tk.Button(self.window, text="Next Question", width=30, command=self.next_question)
        self.next_question_button.pack(pady=10)

    def start_quiz(self):
        self.load_question()
        self.window.mainloop()

    def load_question(self):
        question_data = self.quiz_data[self.current_question_index]
        self.question_label.config(text=question_data["question"])
        options = question_data["options"]
        for button in self.option_buttons:
            button.config(state=tk.NORMAL)
        for i in range(4):
            self.option_buttons[i].config(text=options[i])

    def check_answer(self, selected_option):
        self.option_selected=selected_option
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)
        question_data = self.quiz_data[self.current_question_index]
        correct_answer_index = question_data["correct_answer"]
        correct_answer=question_data["options"]
        if selected_option == correct_answer_index:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Correct answer is: {correct_answer[correct_answer_index]}")

    def next_question(self):
        self.current_question_index += 1
        self.option_selected=None
        for button in self.option_buttons:
            button.config(state=tk.NORMAL)
        if self.current_question_index == len(self.quiz_data):
            messagebox.showinfo("Quiz Over", f"Your score: {self.score}/{len(self.quiz_data)}")
            self.window.quit()
        else:
            self.load_question()

quiz = Quiz()
quiz.start_quiz()