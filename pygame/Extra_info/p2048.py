from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('2048 - playmate')
root.iconbitmap('Play')
root.geometry("1000x1000")
x=10

#imgX0 = Image.open('image/im2').resize((80,80))
imgX = ImageTk.PhotoImage(Image.open('image/im2').resize((80,80)))
# imgX = PhotoImage(file = 'image/im2')

# imgX2 = Label(image=imgX)
# imgX2.pack(pady=10)

def thing():
	my_label.config(text="Youou clickeed the button...")
	print("Button")


# buttonX = Button(root, text="Click Me", command=thing)


buttonX = Button(root, image=imgX, command=thing, borderwidth=0)
buttonX.pack(pady=10)

my_label = Label(root, text='Hello')
my_label.pack(pady=10)



mainloop()
