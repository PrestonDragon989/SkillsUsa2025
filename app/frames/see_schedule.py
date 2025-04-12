import customtkinter as ctk
import tkinter as tk

from ..logic.mulch import Mulch
from ..logic.scheduler import Scheduler
from ..logic.truck import Truck


class SeeScheduleFrame(ctk.CTkFrame):
    EXPLANATION = "The schedule for all of the trucks!"

    def __init__(self, root, total_scheduler):
        super().__init__(root)

        self.root = root

        self.total_scheduler: Scheduler = total_scheduler

        # Grid
        self.grid_columnconfigure((0, 1), weight=0)

        self.grid_rowconfigure((0, 1, 2 ,3, 4, 5), weight=1)

        # Top Words
        self.explanation = ctk.CTkLabel(self, wraplength=750, text=self.EXPLANATION,
                                        font=("", 15), justify=ctk.CENTER)
        self.explanation.grid(column=0, row=0, columnspan=2, sticky="NEWS", padx=10)

        # Display frame
        self.frame = ctk.CTkScrollableFrame(self, width=750)
        self.frame.grid(row=1, rowspan=4, column=0, columnspan=2, sticky="NSEW")

    def renew(self):
        # Cleaning it
        for s in self.frame.slaves():
            s.destroy()

        # Renewing schedule view
        for s in self.total_scheduler.schedules:
            for t in s.times:
                self.create_frame(s.name, t[0], t[1]).pack(fill="x")


    def create_frame(self, name, start, end):
        # Create the cart schedule
        f = ctk.CTkFrame(self.frame)

        ctk.CTkLabel(f, text=f"Name: {name}").pack()
        ctk.CTkLabel(f, text=f"Time (After opening): {start // 60}:{round(start - (start // 60) * 60)} - {end // 60}:{round(end - (end // 60) * 60)}").pack()
        return f
