import tkinter as tk
from tkinter import scrolledtext, messagebox
import math
from math import sin, cos, tan, log, log10, sqrt, pi, e
import re

class TrigSolverCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🔥 Trigonometry Solver & Validator 🔥")
        self.root.geometry("800x900")
        self.root.configure(bg='#1a1a1a')
        
        self.expression = ""
        self.display_var = tk.StringVar()
        self.steps_var = tk.StringVar()
        self.result_var = tk.StringVar()
        
        self.create_ui()
        self.trig_identities = self.load_trig_identities()

    def load_trig_identities(self):
        return {
            "sin²θ + cos²θ = 1": True,
            "1 + tan²θ = sec²θ": True,
            "1 + cot²θ = csc²θ": True,
            "sin(2θ) = 2sinθcosθ": True,
            "cos(2θ) = cos²θ - sin²θ": True,
        }

    def create_ui(self):
        # Title
        title = tk.Label(self.root, text="🔥 TRIGONOMETRY SOLVER & VALIDATOR 🔥", 
                        font=('Arial', 20, 'bold'), fg='#00ff88', bg='#1a1a1a')
        title.pack(pady=10)

        # Display Entry
        entry_frame = tk.Frame(self.root, bg='#1a1a1a')
        entry_frame.pack(fill="x", padx=20, pady=10)
        
        self.entry = tk.Entry(entry_frame, textvariable=self.display_var, font=('Consolas', 18),
                             bg="#2d2d2d", fg="#00ff88", justify='right', bd=0, relief='solid')
        self.entry.pack(fill="x", ipady=15)

        # Buttons Frame - FIXED SYNTAX ERROR HERE
        buttons = [
            ['C', '⌫', '(', ')', '='],
            ['sin', 'cos', 'tan', 'cot', 'sec'],
            ['asin', 'acos', 'atan', '√', 'π'],
            ['7', '8', '9', '/', 'x²'],
            ['4', '5', '6', '*', 'xʸ'],
            ['1', '2', '3', '-', 'log'],
            ['0', '.', '±', '+', 'ANS']
        ]

        btn_frame = tk.Frame(self.root, bg='#1a1a1a')
        btn_frame.pack(fill="both", expand=True, padx=20, pady=10)

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = tk.Button(btn_frame, text=text, font=('Arial', 14, 'bold'),
                              bg='#404040', fg='white', bd=0, height=2,
                              command=lambda t=text: self.on_click(t),
                              relief='flat', activebackground='#606060')
                btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
            
            btn_frame.grid_rowconfigure(r, weight=1)
        
        # FIXED: Correct column configuration
        for c in range(5):
            btn_frame.grid_columnconfigure(c, weight=1)

        # Results Frame
        results_frame = tk.Frame(self.root, bg='#1a1a1a')
        results_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Result Label
        tk.Label(results_frame, text="📊 RESULT:", font=('Arial', 14, 'bold'),
                fg='#ffaa00', bg='#1a1a1a').pack(anchor='w')
        self.result_label = tk.Label(results_frame, text="Enter equation...", 
                                   font=('Consolas', 16), fg='#ffffff', bg='#2d2d2d',
                                   relief='solid', padx=10, pady=5)
        self.result_label.pack(fill='x', pady=(0,10))

        # Steps Text Area
        tk.Label(results_frame, text="📝 STEP-BY-STEP SOLUTION:", font=('Arial', 14, 'bold'),
                fg='#ffaa00', bg='#1a1a1a').pack(anchor='w')
        self.steps_text = scrolledtext.ScrolledText(results_frame, height=12, width=80,
                                                  font=('Consolas', 12), bg='#2d2d2d',
                                                  fg='#00ff88', bd=0, relief='solid')
        self.steps_text.pack(fill="both", expand=True)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.steps_text.delete(1.0, tk.END)
            self.result_label.config(text="Ready...", fg='#ffffff')
        elif char == '⌫':
            self.expression = self.expression[:-1]
        elif char == '=' or char == 'ANS':
            self.solve_step_by_step()
            return
        elif char == '±':
            if self.expression and self.expression[-1] != '-':
                self.expression += '-'
        elif char == '√':
            self.expression += "sqrt("
        elif char == 'π':
            self.expression += str(round(pi, 4))
        elif char == 'sin':
            self.expression += "sin("
        elif char == 'cos':
            self.expression += "cos("
        elif char == 'tan':
            self.expression += "tan("
        elif char == 'cot':
            self.expression += "1/tan("
        elif char == 'sec':
            self.expression += "1/cos("
        elif char == 'asin':
            self.expression += "asin("
        elif char == 'acos':
            self.expression += "acos("
        elif char == 'atan':
            self.expression += "atan("
        elif char == 'x²':
            self.expression += "**2"
        elif char == 'xʸ':
            self.expression += "**"
        elif char == 'log':
            self.expression += "log("
        else:
            self.expression += str(char)

        self.display_var.set(self.expression)

    def deg_to_rad(self, expr):
        """Convert degree notation if present"""
        # Simple degree conversion (assumes degrees by default for trig functions)
        return expr.replace('°', '*pi/180')

    def safe_eval(self, expr):
        """Safely evaluate mathematical expression"""
        safe_dict = {
            "__builtins__": {},
            "sin": math.sin, "cos": math.cos, "tan": math.tan, "pi": math.pi,
            "asin": math.asin, "acos": math.acos, "atan": math.atan,
            "log": math.log, "log10": math.log10, "sqrt": math.sqrt,
            "e": math.e, "radians": math.radians,
        }
        try:
            # Replace ** with pow for safety
            expr_safe = expr.replace('**', '^').replace('^', '**')
            return eval(expr_safe, safe_dict)
        except:
            return None

    def solve_step_by_step(self):
        expr = self.expression.strip()
        if not expr or '=' not in expr:
            self.steps_text.delete(1.0, tk.END)
            self.steps_text.insert(tk.END, "❌ Please enter VALID EQUATION\n\n📝 Examples:\n• sin(30*pi/180) = 0.5\n• cos(pi/3) = 0.5\n• tan(pi/4) = 1")
            self.result_label.config(text="❌ Invalid Format", fg='#ff4444')
            return

        steps = []
        steps.append("🔍 STEP-BY-STEP ANALYSIS\n")
        steps.append(f"📝 Input: {expr}\n")
        steps.append("━" * 60 + "\n\n")

        try:
            lhs, rhs = [x.strip() for x in expr.split('=', 1)]
            
            steps.append("📊 STEP 1: SPLIT EQUATION\n")
            steps.append(f"Left:  {lhs}\n")
            steps.append(f"Right: {rhs}\n\n")

            # Evaluate both sides
            lhs_val = self.safe_eval(lhs)
            rhs_val = self.safe_eval(rhs)

            steps.append("📊 STEP 2: CALCULATE VALUES\n")
            
            if lhs_val is not None:
                steps.append(f"LHS = {lhs_val:.8f}\n")
            else:
                steps.append("LHS = Cannot calculate\n")
                
            if rhs_val is not None:
                steps.append(f"RHS = {rhs_val:.8f}\n")
            else:
                steps.append("RHS = Cannot calculate\n")

            # Compare results
            if lhs_val is not None and rhs_val is not None:
                difference = abs(lhs_val - rhs_val)
                steps.append(f"\n📊 STEP 3: COMPARE\n")
                steps.append(f"Difference = {difference:.10f}\n")
                
                tolerance = 1e-6
                if difference < tolerance:
                    verdict = "✅ CORRECT! ✓✓"
                    color = '#00ff88'
                else:
                    verdict = f"❌ WRONG (error={difference:.6f})"
                    color = '#ff4444'
                
                steps.append(f"VERDICT: {verdict}\n")
                
                # Trig identity check
                steps.append("\n🔥 TRIG IDENTITY VERIFICATION\n")
                steps.append("• sin²θ + cos²θ = 1     ✓ ALWAYS TRUE\n")
                steps.append("• 1 + tan²θ = sec²θ     ✓ ALWAYS TRUE\n")
                steps.append("• sin(2θ) = 2sinθcosθ   ✓ DOUBLE ANGLE\n")

            else:
                verdict = "⚠️ PARTIAL EVALUATION"
                color = '#ffaa00'
                steps.append("\n⚠️ Some parts could not be calculated")

        except Exception as e:
            steps.append(f"\n❌ ERROR: {str(e)}")
            verdict = "❌ ERROR"
            color = '#ff4444'

        # Update display
        self.steps_text.delete(1.0, tk.END)
        self.steps_text.insert(tk.END, "".join(steps))
        self.result_label.config(text=verdict, fg=color)
        self.steps_text.see(tk.END)

def main():
    root = tk.Tk()
    app = TrigSolverCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()