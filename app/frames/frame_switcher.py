import customtkinter as ctk


class FrameSwitcher(ctk.CTkFrame):
    def __init__(self, root, frame_swapper_function):
        super().__init__(root, border_width=2)

        self.frame_swapper_function = frame_swapper_function

        # Buttons to switch pages
        self.create_load = ctk.CTkButton(self, text="Create Schedule", corner_radius=0, width=200, height=50, command=lambda: frame_swapper_function("create_schedule"))
        self.create_load.pack(pady=20, padx=15, fill=ctk.X)

        self.see_schedule = ctk.CTkButton(self, text="See Schedule", corner_radius=0, width=200, height=50, command=lambda: frame_swapper_function("see_schedule"))
        self.see_schedule.pack(pady=20, padx=15, fill=ctk.X)
