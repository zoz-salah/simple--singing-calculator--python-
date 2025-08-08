import tkinter as tk  # GUI library

class Calculator:
    def __init__(self, root):
        # Window settings
        self.root = root
        self.root.title("SINGING CALC")
        self.root.geometry("420x620")
        self.root.configure(bg="black")
        self.root.resizable(False, False)

        # Calculator data
        self.current = ""
        self.operator = ""
        self.total = 0
        self.reset_next = False

        # Display
        self.display = tk.Label(
            root, text="0", anchor='e', justify="right",
            font=("Arial", 26), bg="black", fg="white",
            padx=24, wraplength=380, height=3
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.create_buttons()

        for i in range(6): self.root.rowconfigure(i, weight=1)
        for i in range(4): self.root.columnconfigure(i, weight=1)

    # Create buttons
    def create_buttons(self):
        buttons = [
            ["AC", "+/-", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        for r, row in enumerate(buttons, start=1):
            for c, key in enumerate(row):
                colspan = 2 if key == "0" else 1
                btn = tk.Button(
                    self.root, text=key, font=("Helvetica", 24),
                    bg=self.get_color(key), fg="white", bd=0,
                    command=lambda x=key: self.button_press(x)
                )
                btn.grid(row=r, column=c, columnspan=colspan, sticky="nsew", padx=1, pady=1)

    # Button colors
    def get_color(self, key):
        if key in ["+", "-", "×", "÷", "="]: return "#FF9500"
        elif key in ["AC", "+/-", "%"]: return "#A5A5A5"
        else: return "#333333"

    # Button actions
    def button_press(self, key):
        if key == "AC":  # Clear
            self.current, self.operator, self.total = "", "", 0
            self.display.config(text="0")

        elif key in "+-×÷":  # Operator
            if self.current:
                self.total = float(self.current)
                self.operator = key
                self.reset_next = True

        elif key == "=":  # Show lyrics
            self.lyrics = [
                "خلينا في ماشكلك",
                "سيبك انتي من مشاكلي",
                "مفيش حاجه بتعدي",
                "سنين و البعد مش بينسي",
                "لما الوقت كان كتير اكيد فكرت فيكي قبلي",
                "ايه ذنبي قوليلي ايه ذنبي",
                "دماغي بتوديني ومش بتجيبني"
            ]
            self.timings = [2000, 2000, 1900, 2299, 4300, 4200, 3500]
            self.current_line = 0
            self.show_lyrics_with_timing()

        elif key == "+/-":  # Change sign
            if self.current:
                self.current = self.current[1:] if self.current.startswith("-") else "-" + self.current
                self.display.config(text=self.current)

        elif key == "%":  # Percentage
            if self.current:
                self.current = str(float(self.current) / 100)
                self.display.config(text=self.format_number(self.current))

        else:  # Number or decimal
            if self.reset_next:
                self.current = ""
                self.reset_next = False
            if key == "." and "." in self.current: return
            self.current += key
            self.display.config(text=self.current)

    # Lyrics timing
    def show_lyrics_with_timing(self):
        if self.current_line < len(self.lyrics):
            self.display.config(text=self.lyrics[self.current_line])
            delay = self.timings[self.current_line]
            self.current_line += 1
            self.root.after(delay, self.show_lyrics_with_timing)
        else:
            self.current, self.operator, self.total = "", "", 0

    # Format number
    def format_number(self, num_str):
        num = float(num_str)
        return str(int(num)) if num == int(num) else str(round(num, 8))

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
