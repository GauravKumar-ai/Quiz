import tkinter as tk
from tkinter import messagebox

# Quiz questions and their options
questions = [
    {
        "question": "What is the correct way to create a function in Python?",
        "options": ["function my_function()", "def my_function()", "create my_function()", "func my_function()"],
        "answer": 1
    },
    {
        "question": "Which of the following is used to insert a comment in Python code?",
        "options": ["# This is a comment", "// This is a comment", "<!-- This is a comment -->", "/* This is a comment */"],
        "answer": 0
    },
    {
        "question": "What is the output of the following code?\nprint(type([1, 2, 3]))",
        "options": ["<class 'tuple'>", "<class 'list'>", "<class 'set'>", "<class 'dict'>"],
        "answer": 1
    },
    {
        "question": "How do you start a while loop in Python?",
        "options": ["while x > y {", "while (x > y)", "while x > y:", "do while (x > y)"],
        "answer": 2
    },
    {
        "question": "Which of these data types is immutable in Python?",
        "options": ["List", "Dictionary", "String", "Set"],
        "answer": 2
    },
    {
        "question": "What is the result of 3 ** 2 in Python?",
        "options": ["6", "9", "5", "8"],
        "answer": 1
    },
    {
        "question": "Which method can be used to remove the last item from a list?",
        "options": ["remove()", "delete()", "pop()", "discard()"],
        "answer": 2
    },
    {
        "question": "What will be the output of the following code?\nx = 5\ny = 10\nprint(x, y)\nx, y = y, x\nprint(x, y)",
        "options": ["5 10 followed by 5 10", "5 10 followed by 10 5", "10 5 followed by 10 5", "Syntax Error"],
        "answer": 1
    },
    {
        "question": "Which keyword is used for exception handling in Python?",
        "options": ["catch", "except", "throw", "try-except"],
        "answer": 1
    },
    {
        "question": "What is the output of the following code?\ndef add(x, y=5):\n    return x + y\nprint(add(10))",
        "options": ["5", "10", "15", "TypeError"],
        "answer": 2
    }
]

# Function to calculate and display the score
def calculate_score():
    score = 0
    for i, question in enumerate(questions):
        if selected_answers[i].get() == question["answer"]:
            score += 1
    messagebox.showinfo("Quiz Result", f"Your Score: {score}/{len(questions)}")

# Function to add scrollbar to the quiz window
def create_quiz_window():
    root = tk.Tk()
    root.title("Python Quiz")
    root.geometry("600x400")

    # Create a main frame
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=1)

    # Create a canvas inside the frame
    canvas = tk.Canvas(main_frame)
    canvas.pack(side="left", fill="both", expand=1)

    # Add a scrollbar to the canvas
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the canvas with the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas to hold all the quiz content
    quiz_frame = tk.Frame(canvas)

    # Add the frame to the canvas
    canvas.create_window((0, 0), window=quiz_frame, anchor="nw")

    # Selected answers storage
    global selected_answers
    selected_answers = []

    # Display quiz questions and options
    for i, question in enumerate(questions):
        # Question label
        question_label = tk.Label(quiz_frame, text=f"{i + 1}. {question['question']}", anchor="w", justify="left")
        question_label.pack(fill="x", pady=5)

        # Variable to store selected option
        selected_answer = tk.IntVar(value=-1)  # Default value is -1 (no option selected)
        selected_answers.append(selected_answer)

        # Display options as radio buttons
        for j, option in enumerate(question['options']):
            radio_btn = tk.Radiobutton(quiz_frame, text=option, variable=selected_answer, value=j)
            radio_btn.pack(anchor="w")

    # Submit button to calculate the score
    submit_btn = tk.Button(quiz_frame, text="Submit", command=calculate_score, bg="green", fg="white", padx=20, pady=10)
    submit_btn.pack(pady=20)

    root.mainloop()

# Call the function to create the quiz window
create_quiz_window()
