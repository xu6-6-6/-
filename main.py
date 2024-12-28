import tkinter as tk
from gui import StudentRandomQuestionSystem

def main():
    root = tk.Tk()
    app = StudentRandomQuestionSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()