from tkinter import *
from window import MainWindow
import sv_ttk


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title('Youtube Donwloads')

        # CONFIGURE THE WINDOW
        self.width = 510
        self.height = 520
        self.sys_width = int((self.root.winfo_screenwidth() / 2) - (self.width / 2))
        self.sys_height = int((self.root.winfo_screenheight() / 2) - (self.height / 2))

        self.root.geometry(f'{self.width}x{self.height}+{self.sys_width}+{self.sys_height}')
        self.root.resizable(width=False, height=False)

        # SET THEME
        sv_ttk.set_theme('light')

        # CALL WINDOW
        MainWindow(self.root)

        # START THE APLICATION
        self.root.mainloop()


if __name__ == '__main__':
    Main()
