import customtkinter as ctk
import tkinter as tk

from ..logic.mulch import Mulch
from ..logic.scheduler import Scheduler
from ..logic.truck import Truck


class CreateScheduleFrame(ctk.CTkFrame):
    EXPLANATION = ("This is where you schedule things. Please put in the length (feet), width (feet), and depth (inches)"
                   " of the mulch you need, and the time you desire. The time needs to be after 8am, and before 5pm.")

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
        self.explanation.grid(column=0, row=0, columnspan=2, sticky="NEW", padx=10)

        # Inputs
        # Width
        self.width_label = ctk.CTkLabel(self, text="Width (feet): ", font=("", 24, "bold"))
        self.width_label.grid(column=0, row=1, columnspan=1, sticky="EW", padx=10)

        self.width = ctk.CTkEntry(self, placeholder_text="Width")
        self.width.grid(column=1, row=1, columnspan=1, sticky="EW", padx=10)

        # Length
        self.length_label = ctk.CTkLabel(self, text="Length (feet): ", font=("", 24, "bold"))
        self.length_label.grid(column=0, row=2, columnspan=1, sticky="EW", padx=10)

        self.length = ctk.CTkEntry(self, placeholder_text="Length")
        self.length.grid(column=1, row=2, columnspan=1, sticky="EW", padx=10)

        # Depth
        self.depth_label = ctk.CTkLabel(self, text="Depth (inches): ", font=("", 24, "bold"))
        self.depth_label.grid(column=0, row=3, columnspan=1, sticky="EW", padx=10)

        self.depth = ctk.CTkEntry(self, placeholder_text="Depth")
        self.depth.grid(column=1, row=3, columnspan=1, sticky="EW", padx=10)

        # Time
        self.time_label = ctk.CTkLabel(self, text="Time (Format: Hour:Minutes): ", font=("", 24, "bold"))
        self.time_label.grid(column=0, row=4, columnspan=1, sticky="EW", padx=10)

        self.time = ctk.CTkEntry(self, placeholder_text="Time")
        self.time.grid(column=1, row=4, columnspan=1, sticky="EW", padx=10)

        # Submit
        self.submit = ctk.CTkButton(self, text="Submit Info", command=lambda: self.attempt_input())
        self.submit.grid(column=0, row=5, columnspan=2, sticky="EW", padx=10)

    def renew(self):
        pass # this is abstract and is for the other class

    def attempt_input(self):
        # Parsing
        width = self.width.get()
        length = self.length.get()
        depth = self.depth.get()
        time = self.time.get()


        try:
            width = int(width)
            length = int(length)
            depth = int(depth)
        except Exception as e:
            self.explanation.configure(text=self.EXPLANATION + "\n\nCANNOT PUT IN THINGS THAT AREN'T NUMBERS FOR WIDTH/LENGTH/DEPTH")
            return

        if time.count(":") != 1:
            self.explanation.configure(
                text=self.EXPLANATION + "\n\nUSE CORRECT TIME FORMAT (Example: 3:45)")
            print("Time not contain :")
            return

        else:
            time = time.split(":")

            try:
                # time.remove(":")
                time = [int(time[0]), int(time[1])]

                if time[0] >= 8:
                    time[0] = time[0] - 8
                else:
                    time[0] = 4 + time[0]

                time = (time[0] * 60) + time[1]

            except Exception as e:
                self.explanation.configure(
                    text=self.EXPLANATION + "\n\nUSE CORRECT TIME FORMAT (Example: 3:45)")

                return

        # Actually using
        load: Mulch = Mulch(length, width, depth)
        end_time = time + Truck.get_time_of_load(load)

        if not self.total_scheduler.has_space(load):
            self.explanation.configure(
                text=self.EXPLANATION + "\n\nNOT ENOUGH SPACE FOR MULCH")
            return

        if not self.total_scheduler.has_time(time, end_time):
            self.explanation.configure(
                text=self.EXPLANATION + "\n\nNOT ENOUGH TIME FOR MULCH OR OUTSIDE OF SCHEDULE")
            return

        self.total_scheduler.add_mulch(load, time)
        print("===== update of schedules & Trucks =====")
        for s in self.total_scheduler.schedules:
            print(s.name + "\n", s, "\n\n")
        print("===== update of schedules & Trucks =====")