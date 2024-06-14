import random
import math
import time
import tkinter as tk
from tkinter import messagebox
import sys
import os

class MentalMathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Math Game")
        self.root.geometry("400x300")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        self.play_button = tk.Button(self.main_frame, text="Play", command=self.start_game)
        self.play_button.pack(pady=20)

        self.game_frame = tk.Frame(root)

        self.score_label = tk.Label(self.game_frame, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(anchor="nw")

        self.timer_label = tk.Label(self.game_frame, text="Time: 120", font=("Arial", 14))
        self.timer_label.pack(anchor="ne")

        self.problem_label = tk.Label(self.game_frame, text="", font=("Arial", 16))
        self.problem_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.game_frame, font=("Arial", 16), bg="#ffc107", bd=2, relief="solid", justify="center")
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)

        self.result_frame = tk.Frame(root)

        self.result_label = tk.Label(self.result_frame, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

        self.back_button = tk.Button(self.result_frame, text="Play Again", command=self.restart_program)
        self.back_button.pack(pady=20)

        self.correct_answers = 0
        self.start_time = 0
        self.current_solution = None
        self.problem_type = None

    def start_game(self):
        self.result_frame.pack_forget()
        self.main_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)
        self.correct_answers = 0
        self.score_label.config(text="Score: 0")
        self.start_time = time.time()
        self.update_timer()
        self.next_problem()

    def next_problem(self):
        problem, solution, self.problem_type = self.generate_problem()
        self.current_solution = solution
        self.problem_label.config(text=problem)
        self.answer_entry.delete(0, tk.END)
        self.root.update_idletasks()
        self.answer_entry.place(x=(self.problem_label.winfo_x() + self.problem_label.winfo_width() / 2 - self.answer_entry.winfo_width() / 2), y=self.problem_label.winfo_y() + 50)

    def generate_problem(self):
        problem_types = ['addition', 'subtraction', 'multiplication', 'division', 'scientific notation', 'percentage', 'square root', 'trigonometry', 'logarithm', 'square', 'unit conversion']
        problem_type = random.choice(problem_types)

        if problem_type == 'addition':
            a = round(random.uniform(1, 100), 1)
            b = round(random.uniform(1, 100), 1)
            problem = f"{a} + {b} = ?"
            solution = a + b

        elif problem_type == 'subtraction':
            a = round(random.uniform(50, 100), 1)
            b = round(random.uniform(1, 49), 1)
            problem = f"{a} - {b} = ?"
            solution = a - b

        elif problem_type == 'multiplication':
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            problem = f"{a} * {b} = ?"
            solution = a * b

        elif problem_type == 'division':
            a = random.randint(20, 100)
            b = random.randint(1, 20)
            problem = f"{a} / {b} = ?"
            solution = a / b

        elif problem_type == 'scientific notation':
            a = round(random.uniform(1, 10), 1)
            b = random.randint(-5, 5)
            problem = f"{a} x 10^{b} = ?"
            solution = a * (10 ** b)

        elif problem_type == 'percentage':
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            problem = f"What is {a}% of {b}?"
            solution = (a / 100) * b

        elif problem_type == 'square root':
            a = random.randint(1, 20)
            problem = f"√{a*a} = ?"
            solution = a

        elif problem_type == 'trigonometry':
            angle = random.choice([0, 30, 45, 60, 90])
            function = random.choice(['sin', 'cos', 'tan'])
            problem = f"{function}({angle}°) = ?"
            if function == 'sin':
                solution = round(math.sin(math.radians(angle)), 2)
            elif function == 'cos':
                solution = round(math.cos(math.radians(angle)), 2)
            elif function == 'tan':
                solution = round(math.tan(math.radians(angle)), 2)

        elif problem_type == 'logarithm':
            if random.choice([True, False]):
                value = random.choice([1, 10, 100, 1000])
                problem = f"log_10({value}) = ?"
                solution = round(math.log10(value), 2)
            else:
                a = round(random.uniform(1, 10), 1)
                b = random.randint(-5, 5)
                value = a * (10 ** b)
                problem = f"log_10({a} x 10^{b}) = ?"
                solution = round(math.log10(value), 2)
        
        elif problem_type == 'square':
            a = random.randint(1, 20)
            problem = f"{a}² = ?"
            solution = a ** 2

        elif problem_type == 'unit conversion':
            conversion_types = ['g to kg', 'kg to g', 'm to cm', 'cm to m', 'L to mL', 'mL to L']
            conversion_type = random.choice(conversion_types)
            if conversion_type == 'g to kg':
                value = random.randint(1, 10000)
                problem = f"Convert {value} g to kg"
                solution = value / 1000
            elif conversion_type == 'kg to g':
                value = random.uniform(0.1, 10)
                problem = f"Convert {value:.1f} kg to g"
                solution = value * 1000
            elif conversion_type == 'm to cm':
                value = random.uniform(0.1, 10)
                problem = f"Convert {value:.1f} m to cm"
                solution = value * 100
            elif conversion_type == 'cm to m':
                value = random.randint(1, 1000)
                problem = f"Convert {value} cm to m"
                solution = value / 100
            elif conversion_type == 'L to mL':
                value = random.uniform(0.1, 10)
                problem = f"Convert {value:.1f} L to mL"
                solution = value * 1000
            elif conversion_type == 'mL to L':
                value = random.randint(1, 10000)
                problem = f"Convert {value} mL to L"
                solution = value / 1000

        return problem, solution, problem_type

    def check_answer(self, event=None):
        user_input = self.answer_entry.get()
        try:
            user_answer = float(user_input)
        except ValueError:
            self.shake_entry()
            return

        if isinstance(self.current_solution, float):
            correct = abs(user_answer - self.current_solution) <= 0.1 * abs(self.current_solution)
        else:
            correct = user_answer == self.current_solution

        if correct:
            self.correct_answers += 1
            self.score_label.config(text=f"Score: {self.correct_answers}")
            self.next_problem()
        else:
            self.shake_entry()

    def shake_entry(self):
        original_x = self.answer_entry.winfo_x()
        for offset in (-10, 10, -5, 5, 0):
            self.answer_entry.place(x=original_x + offset, y=self.answer_entry.winfo_y())
            self.answer_entry.update()
            time.sleep(0.05)
        self.answer_entry.place(x=original_x, y=self.answer_entry.winfo_y())  # Reset to original position

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = 120 - elapsed_time
        self.timer_label.config(text=f"Time: {remaining_time}")
        if remaining_time > 0:
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.game_frame.pack_forget()
        self.result_label.config(text=f"Your final score is {self.correct_answers}")
        self.result_frame.pack(fill="both", expand=True)

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

if __name__ == "__main__":
    root = tk.Tk()
    game = MentalMathGame(root)
    root.mainloop()
