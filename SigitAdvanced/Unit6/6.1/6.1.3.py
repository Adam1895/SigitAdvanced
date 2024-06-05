import tkinter as tk
from tkinter import PhotoImage

class ImageWindow:
    _image = None

    def __init__(self, root):
        self._root = root
        self._root.title("Adams Question and Answer")

        self._question = "What's my favorite image from the course?"
        self._question_label = tk.Label(self._root, text=self._question)
        self._question_label.pack(pady=10)

        self._button = tk.Button(self._root, text="Show Answer", command=self._show_image)
        self._button.pack(pady=10)

        self._image_label = tk.Label(self._root)
        self._image_label.pack(pady=10)

    def _show_image(self):
        ImageWindow._image = PhotoImage(file="img.png")
        self._image_label.configure(image=ImageWindow._image)
        self._image_label.image = ImageWindow._image

if __name__ == "__main__":
    root = tk.Tk()
    image_window = ImageWindow(root)
    root.mainloop()