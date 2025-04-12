import customtkinter as ctk

from .frames.create_schedule import CreateScheduleFrame
from .frames.see_schedule import SeeScheduleFrame
from .frames.frame_switcher import FrameSwitcher
from .logic.scheduler import Scheduler


class Root(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.scheduler: Scheduler = Scheduler()

        # Setting data for the window
        self._set_globals()

        self.title("Testing Custom Tkinter")
        self.geometry("1000x600")
        self.resizable(False, False)

        # Setting columns / rows of gui
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Frame swapper and frames
        self.frame_switcher: FrameSwitcher = FrameSwitcher(self, self.switch_frames)
        self.frame_switcher.grid(row=0, column=0, rowspan=3, sticky="NSEW")

        self.current_frame: str = "create_schedule"
        self.frames: dict[str, ctk.CTkFrame] = {
            "create_schedule": CreateScheduleFrame(self, self.scheduler),
            "see_schedule": SeeScheduleFrame(self, self.scheduler)
        }

        self.frames[self.current_frame].grid(column=1, row=0, rowspan=3, sticky="NSEW")

    @staticmethod
    def _set_globals():
        ctk.set_default_color_theme("blue")
        ctk.set_appearance_mode("system")

    def switch_frames(self, new_frame):
        self.frames[self.current_frame].grid_forget()

        self.current_frame = new_frame

        self.frames[self.current_frame].renew()
        self.frames[self.current_frame].grid(column=1, row=0, rowspan=3, sticky="NSEW")
