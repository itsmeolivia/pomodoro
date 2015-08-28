import Tkinter
import tkMessageBox

DEFAULT_GAP = 1500

class Pymodoro:
    def __init__(self, master):
        self.master = master
        self.mainframe = Tkinter.Frame(self.master, bg="white")
        self.mainframe.pack(fill=Tkinter.BOTH, expand=True)

        self.timer_text = Tkinter.StringVar()
        self.timer_text.trace("w", self.build_timer)
        self.time_remaining = Tkinter.IntVar()
        self.time_remaining.set(DEFAULT_GAP)
        self.time_remaining.trace("w", self.alert)
        self.running = False

        self.build_grid()
        self.build_banner()
        self.build_buttons()
        self.build_timer()

        self.update()


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
            text="Start",
            command=self.start_timer
        )

        self.stop_button = Tkinter.Button(
            button_frame,
            text="Stop",
            command=self.stop_timer
        )

        self.start_button.grid(row=0, column=0, sticky="ew")
        self.stop_button.grid(row=0, column=1, sticky="ew")
        self.stop_button.config(state=Tkinter.DISABLED)

    def build_timer(self, *args):
        timer = Tkinter.Label(
            self.mainframe,
            text=self.timer_text.get(),
            font=("Helvetica", 36)
        )

        timer.grid(row=1, column=0, sticky="nsew")

    def start_timer(self):
        self.time_remaining.set(DEFAULT_GAP)
        self.running = True
        self.start_button.config(state=Tkinter.DISABLED)
        self.stop_button.config(state=Tkinter.NORMAL)

    def stop_timer(self):
        self.running = False
        self.stop_button.config(state=Tkinter.DISABLED)
        self.start_button.config(state=Tkinter.NORMAL)

    def alert(self, *args):
        if not self.time_remaining.get():
            tkMessageBox.showinfo("Time's up", "TIME TO WASTE")


    def minutes_seconds(self, seconds):
        return seconds // 60, int(seconds % 60)

    def update(self):
        time_left = self.time_remaining.get()

        if self.running and time_left:
            minutes, seconds = self.minutes_seconds(time_left)
            self.time_remaining.set(time_left - 1)
        else:
            minutes, seconds = self.minutes_seconds(DEFAULT_GAP)
            self.stop_timer()
        self.timer_text.set(
            "{:0>2}:{:0>2}".format(minutes, seconds)
        )
        self.master.after(1000, self.update)



if __name__ == "__main__":
    root = Tkinter.Tk()
    Pymodoro(root)
    root.mainloop()
