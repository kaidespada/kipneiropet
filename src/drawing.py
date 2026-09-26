import tkinter as tk
import os

from PIL import Image, ImageDraw, ImageOps


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

        # Изображение, которое будет отправляться модели
        self.image = Image.new(
            "L",
            (280, 280),
            0
        )

        self.image_draw = ImageDraw.Draw(
            self.image
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

        # Canvas
        self.canvas.create_oval(
            x - 8,
            y - 8,
            x + 8,
            y + 8,
            fill="white",
            outline="white"
        )

        # Записываем рисунок в PIL Image
        self.image_draw.ellipse(
            (
                x - 8,
                y - 8,
                x + 8,
                y + 8
            ),
            fill=255
        )

    def clear(self):

        self.canvas.delete("all")

        self.image = Image.new(
            "L",
            (280, 280),
            0
        )

        self.image_draw = ImageDraw.Draw(
            self.image
        )

        self.result_label.config(
            text="Нарисуйте цифру от 0 до 5"
        )

    def recognize(self):

        if self.model is None:
            self.result_label.config(
                text="Модель не загружена"
            )
            return

        image = ImageOps.invert(self.image)

        # Приводим размер к размеру, который использовался при обучении
        image = image.resize(
            (64, 64)
        )

        image_path = "temp_digit.png"

        image.save(
            image_path
        )

        # Передаём картинку обученной модели
        class_id, confidence = self.model.predict(
            image_path
        )

        confidence_percent = confidence * 100

        self.result_label.config(
            text=f"Это цифра {class_id}\n"
                 f"Уверенность: {confidence_percent:.2f}%"
        )

        # Удаляем временную картинку
        if os.path.exists(image_path):
            os.remove(image_path)

    def run(self):

        self.window.mainloop()