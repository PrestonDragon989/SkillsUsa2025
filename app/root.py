import customtkinter as ctk


class Root(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Setting data for the window
        self._set_globals()

        self.title("Testing Custom Tkinter")
        self.geometry("1000x600")
        self.minsize(800, 360)

    @staticmethod
    def _set_globals():
        ctk.set_default_color_theme("blue")
        ctk.set_appearance_mode("system")
