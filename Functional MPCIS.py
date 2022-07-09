import winsound
import tkinter as tk

winsound.PlaySound("audio16", winsound.SND_ASYNC)

class Mcpi(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Mop Are Performance Computer Interface System")
        self.minsize(1000,800)
        self.state('zoomed')
        self.bind('<Escape>', lambda event: self.state('normal'))
        self.bind('<F11>', lambda event: self.state('zoomed'))
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(relwidth=1, relheight=1)

class StartPage(tk.Frame,):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Frame.place(self, relwidth=1, relheight=1)
        tk.Label(self, bg='black', fg='#6de639', text="Mop Are Performance Computer Interface System", font=('System', 36, "bold", "italic")).place(anchor='nw', relx=0, rely=0,)
        tk.Button(self, bg='black', fg='#6de639', text="Calibrations", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(PageOne)).place(anchor='ne', relx=1.0, rely=0, relheight=.1, relwidth=.2)
        tk.Button(self, bg='black', fg='#6de639', text="Diagnostics", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(PageTwo)).place(anchor='ne', relx=1.0, rely=0.1, relheight=.1, relwidth=.2)
        tk.Button(self, bg='black', fg='#6de639', text="Music", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(PageThree)).place(anchor='ne', relx=1.0, rely=0.2, relheight=.1, relwidth=.2)
        tk.Button(self, bg='black', fg='#6de639', text="Video", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(PageFour)).place(anchor='ne', relx=1.0, rely=0.3, relheight=.1, relwidth=.2)
        tk.Button(self, bg='black', fg='#6de639', text="Notes", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(PageFive)).place(anchor='ne', relx=1.0, rely=0.4, relheight=.1, relwidth=.2)
        tk.Button(self, bg='black', fg='#6de639', text="Utilities", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(PageSix)).place(anchor='ne', relx=1.0, rely=0.5, relheight=.1, relwidth=.2)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, bg='black', fg='#6de639', text="Calibrations", font=('System', 36, "bold", "italic")).place(anchor='nw', relx=0, rely=0)
        tk.Button(self, bg='black', fg='#6de639', text="8 PSI", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(PageSeven)).place(anchor='ne', relx=1.0, rely=0, relheight=.1, relwidth=.2)
        tk.Button(self, bg='black', fg='#6de639', text="12 PSI", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(PageEight)).place(anchor='ne', relx=1.0, rely=0.15, relheight=.1, relwidth=.2)
        tk.Button(self, bg='black', fg='#6de639', text="14 PSI", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(PageNine)).place(anchor='ne', relx=1.0, rely=0.3, relheight=.1, relwidth=.2)
        tk.Button(self, bg='black', fg='#6de639', text="18 PSI", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(PageTen)).place(anchor='ne', relx=1.0, rely=0.45, relheight=.1, relwidth=.2)
        tk.Button(self, bg='black', fg='#6de639', text="Main page", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(StartPage)).place(anchor='ne', relx=1.0, rely=0.6, relheight=.1, relwidth=.2)
        winsound.PlaySound("audio4", winsound.SND_FILENAME)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, bg='black', fg='#6de639', text="Diagnostics", font=('System', 36, "bold", "italic")).place(anchor='nw', relx=0, rely=0)
        tk.Button(self, bg='black', fg='#6de639', text="Main page", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(StartPage)).place(anchor='ne', relx=1.0, rely=0, relheight=.1, relwidth=.2)
        winsound.PlaySound("audio5", winsound.SND_FILENAME)

class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, bg='black', fg='#6de639', text="Music", font=('System', 36, "bold", "italic")).place(anchor='nw', relx=0, rely=0)
        tk.Button(self, bg='black', fg='#6de639', text="Main page", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(StartPage)).place(anchor='ne', relx=1.0, rely=0, relheight=.1, relwidth=.2)
        winsound.PlaySound("audio6", winsound.SND_FILENAME)

class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, bg='black', fg='#6de639', text="Video", font=('System', 36, "bold", "italic")).place(anchor='nw', relx=0, rely=0)
        tk.Button(self, bg='black', fg='#6de639', text="Main page", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(StartPage)).place(anchor='ne', relx=1.0, rely=0, relheight=.1, relwidth=.2)
        winsound.PlaySound("audio7", winsound.SND_FILENAME)

class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, bg='black', fg='#6de639', text="Notes", font=('System', 36, "bold", "italic")).place(anchor='nw', relx=0, rely=0)
        tk.Button(self, bg='black', fg='#6de639', text="Main page", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(StartPage)).place(anchor='ne', relx=1.0, rely=0, relheight=.1, relwidth=.2)
        winsound.PlaySound("audio8", winsound.SND_FILENAME)
class PageSix(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, bg='black', fg='#6de639', text="Utilities", font=('System', 36, "bold", "italic")).place(anchor='nw', relx=0, rely=0)
        tk.Button(self, bg='black', fg='#6de639', text="Main page", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(StartPage)).place(anchor='ne', relx=1.0, rely=0, relheight=.1, relwidth=.2)
        winsound.PlaySound("audio9", winsound.SND_FILENAME)

class PageSeven(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, bg='black', fg='#6de639', text="8 PSI Calibration", font=('System', 36, "bold", "italic")).place(anchor='nw', relx=0, rely=0)
        tk.Label(self, bg='#6de639', fg='black', text="Standard 2.2 TI calibration\n with revised timing and\n fueling for intercooled status.", font=('System', 36, "bold")).place(anchor='nw', relx=0, rely=0.1, relheight=.3, relwidth=.6)
        tk.Button(self, bg='black', fg='#6de639', text="Main page", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(StartPage)).place(anchor='ne', relx=1.0, rely=0, relheight=.1, relwidth=.2)
        winsound.PlaySound("audio11", winsound.SND_FILENAME)

class PageEight(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, bg='black', fg='#6de639', text="12 PSI Calibration", font=('System', 36, "bold", "italic")).place(anchor='nw', relx=0, rely=0)
        tk.Button(self, bg='black', fg='#6de639', text="Main page", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(StartPage)).place(anchor='ne', relx=1.0, rely=0, relheight=.1, relwidth=.2)
        winsound.PlaySound("audio12", winsound.SND_FILENAME)

class PageNine(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, bg='black', fg='#6de639', text="14 PSI Calibration", font=('System', 36, "bold", "italic")).place(anchor='nw', relx=0, rely=0)
        tk.Button(self, bg='black', fg='#6de639', text="Main page", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(StartPage)).place(anchor='ne', relx=1.0, rely=0, relheight=.1, relwidth=.2)
        winsound.PlaySound("audio13", winsound.SND_FILENAME)

class PageTen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='black')
        tk.Label(self, bg='black', fg='#6de639', text="18 PSI Calibration", font=('System', 36, "bold", "italic")).place(anchor='nw', relx=0, rely=0)
        tk.Label(self, bg='#6de639', fg='black', text="Safe Super 60 calibration", font=('System', 36, "bold")).place(anchor='nw', relx=0, rely=0.1, relheight=.4, relwidth=.6)
        tk.Button(self, bg='black', fg='#6de639', text="Main page", font=('System', 18, "bold"),
                  command=lambda: master.switch_frame(StartPage)).place(anchor='ne', relx=1.0, rely=0, relheight=.1, relwidth=.2)       
        winsound.PlaySound("audio15", winsound.SND_FILENAME)
        
if __name__ == "__main__":

    app = Mcpi()
    app.mainloop()

