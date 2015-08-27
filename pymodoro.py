import Tkinter

class Pymodoro:
    def __init__(self, master):
        self.master = master
        self.mainframe = Tkinter.Frame(self.master, bg="white")
        self.mainframe.pack(fill=Tkinter.BOTH, expand=True)

        self.build_grid()
        self.build_banner()
        self.build_buttons()


    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

    def build_banner(self):
        banner = Tkinter.Label(
            self.mainframe,
            bg="red",
            text="Pymodoro",
            fg="white",
            font=("Helvetica", 24)
        )

        banner.grid(
            row=0, column=0,
            sticky="ew",
            padx=10, pady=10
        )

    def build_buttons(self):
        button_frame = Tkinter.Frame(self.mainframe)
        button_frame.grid(
            row=2, column=0,
            sticky="nsew",
            padx=10, pady=10
        )
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        self.start_button = Tkinter.Button(
            button_frame,
            text="Start"
        )

        self.stop_button = Tkinter.Button(
            button_frame,
            text="Stop"
        )

        self.start_button.grid(row=0, column=0, sticky="ew")
        self.stop_button.grid(row=0, column=1, sticky="ew")

if __name__ == "__main__":
    root = Tkinter.Tk()
    Pymodoro(root)
    root.mainloop()
