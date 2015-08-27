import Tkinter

root = Tkinter.Tk()

hi_there = Tkinter.Label(
    root,
    text="hi there!",
    bg="red",
    fg="white"
)
hi_there.pack(fill=Tkinter.BOTH, expand=True)

my_name = Tkinter.Label(root, text="me llamo olivia")
my_name.pack()

root.mainloop()
