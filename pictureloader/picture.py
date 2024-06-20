import tkinter as tk
from PIL import ImageTk, Image

class DraggableImage:
    def __init__(self, canvas, image, x, y):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.id = self.canvas.create_image(self.x, self.y, image=self.image, anchor='nw')
        self.canvas.tag_bind(self.id, '<ButtonPress-1>', self.start_drag)
        self.canvas.tag_bind(self.id, '<B1-Motion>', self.drag)
        self.canvas.tag_bind(self.id, '<ButtonRelease-1>', self.stop_drag)

        # Variables for dragging
        self.dragging = False
        self.start_x = 0
        self.start_y = 0

    def start_drag(self, event):
        self.dragging = True
        self.start_x = event.x
        self.start_y = event.y

    def drag(self, event):
        if self.dragging:
            dx = event.x - self.start_x
            dy = event.y - self.start_y
            self.x += dx
            self.y += dy
            self.canvas.move(self.id, dx, dy)
            self.start_x = event.x
            self.start_y = event.y

    def stop_drag(self, event):
        self.dragging = False

# Create the main window
root = tk.Tk()

# Set the window to be transparent
root.attributes("-transparentcolor", "white")

root.title("Picture Overlay")

# Load the image
image_path = r"C:\Users\jd4nn\Desktop\pictureloader\elwyn.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create a canvas and display the image
canvas = tk.Canvas(root, width=image.width, height=image.height, highlightthickness=0, bg='white')
canvas.pack()
canvas.create_image(0, 0, anchor='nw', image=photo)

# Make the window completely transparent
root.wm_attributes('-alpha', 0.4)

# Make the image draggable
draggable_image = DraggableImage(canvas, photo, 0, 0)

# Start the Tkinter event loop
root.mainloop()
