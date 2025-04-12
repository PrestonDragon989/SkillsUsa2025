from .mulch import Mulch


class Truck:
    def __init__(self, size) -> None:
        self.loads: list[Mulch] = []

        self.volume: int = 0
        self.total_volume: int = size

    def add_load(self, load: Mulch) -> None:
        self.loads.append(load)

    def can_fit(self, load: Mulch) -> bool:
        return self.volume_available >= load.volume

    @staticmethod
    def get_time_of_load(load: Mulch) -> int:
        return 30 + load.time_addition

    # Helper properties
    @property
    def volume_available(self) -> int:
        return self.total_volume - self.volume

    @property
    def total_time_used(self) -> int:
        total: int = 0
        for load in self.loads:
            total += 30 + load.time_addition

        return total

    @property
    def total_mulch(self) -> Mulch:
        total_mulch: Mulch = Mulch(0, 0, 0)
        for load in self.loads:
            total_mulch += load

        return total_mulch
