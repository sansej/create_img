from PIL import Image, ImageTk
import tkinter as tk

class ImageManipulator:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.original_image = self.image.copy()
        self.current_image = self.image.copy()
        self.zoom_factor = 1.0

    # def zoom_in(self, factor=1.2):
    #     self.zoom_factor *= factor
    #     self.update_image()

    def zoom_in(self, factor=1.2):
        self.zoom_factor *= factor
        new_size = (int(self.original_image.width * self.zoom_factor), int(self.original_image.height * self.zoom_factor))
        self.current_image = self.original_image.resize(new_size, Image.Resampling.LANCZOS)

    def zoom_out(self, factor=0.8):
        self.zoom_factor *= factor
        self.update_image()

    def pan(self, offset):
        self.current_image = self.original_image.crop(
            (offset[0], offset[1], offset[0] + self.current_image.width, offset[1] + self.current_image.height)
        )

    # def update_image(self):
    #     new_size = (self.original_image.width, self.original_image.height)
    #     self.current_image = self.original_image.resize(new_size, Image.Resampling.LANCZOS)

    def update_image(self):
        new_size = (int(self.original_image.width * self.zoom_factor), int(self.original_image.height * self.zoom_factor))
        self.current_image = self.original_image.resize(new_size, Image.Resampling.LANCZOS)

    def save_image(self, file_path):
        self.current_image.save(file_path, format="JPEG")

    def scale_image(self, scale_factor):
        width, height = self.original_image.size
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        left = (width - new_width) // 2
        top = (height - new_height) // 2
        right = (width + new_width) // 2
        bottom = (height + new_height) // 2
        self.current_image = self.original_image.crop((left, top, right, bottom))

    def generate_scaled_images(self, output_path, num_images):
        initial_scale = 1.0
        scale_step = (2.0 - initial_scale) / (num_images - 1)
        for i in range(num_images):
            current_scale = initial_scale + i * scale_step
            scaled_image = self.original_image.resize((int(self.original_image.width * current_scale), int(self.original_image.height * current_scale)),Image.Resampling.LANCZOS)
            output_filename = f"{output_path}/scaled_image_{i + 1}.jpg"
            scaled_image.save(output_filename, format="JPEG")

    def display_image(self):
        root = tk.Tk()
        root.title("Image Manipulator")

        tk_image = ImageTk.PhotoImage(self.current_image)
        label = tk.Label(root, image=tk_image)
        label.image = tk_image
        label.pack()

        root.mainloop()

# Пример использования
image_path = "moon.jpg"
manipulator = ImageManipulator(image_path)
# manipulator.zoom_in(0.2)
# manipulator.pan((50, 50))
# manipulator.scale_image(0.8)
# manipulator.display_image()

output_path = "scaled_images"
# manipulator.save_image(output_path)

for i in range(20):
            current_scale = 1.0 - i * 0.01
            manipulator.scale_image(current_scale)
            output_filename = f"{output_path}/scaled_image_{i + 1}.jpg"
            manipulator.save_image(output_filename)
