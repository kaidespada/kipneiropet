import tkinter as tk


class DrawingWindow:

    def __init__(self, model):

        self.model = model

        self.window = tk.Tk()

        self.window.title("Распознавание цифры")

        self.window.geometry("400x500")

        self.canvas = tk.Canvas(
            self.window,
            width=280,
            height=280,
            bg="black"
        )

        self.canvas.pack(
            pady=20
        )

        self.canvas.bind(
            "<B1-Motion>",
            self.draw
        )

        self.button_recognize = tk.Button(
            self.window,
            text="Распознать",
            command=self.recognize
        )

        self.button_recognize.pack(
            pady=5
        )

        self.button_clear = tk.Button(
            self.window,
            text="Очистить",
            command=self.clear
        )

        self.button_clear.pack(
            pady=5
        )

        self.result_label = tk.Label(
            self.window,
            text="Нарисуйте цифру от 0 до 5",
            font=("Arial", 14)
        )

        self.result_label.pack(
            pady=20
        )

    def draw(self, event):

        x = event.x
        y = event.y

        self.canvas.create_oval(
            x - 8,
            y - 8,
            x + 8,
            y + 8,
            fill="white",
            outline="white"
        )

    def clear(self):

        self.canvas.delete("all")

        self.result_label.config(
            text="Нарисуйте цифру от 0 до 5"
        )

    def recognize(self):

        print("Распознавание...")

    def run(self):

        self.window.mainloop()