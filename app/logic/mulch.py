from dataclasses import dataclass


@dataclass
class Mulch:
    length: int
    width: int
    depth: int

    @property
    def volume(self) -> int:
        """
        Returns the volume of cubic yards of mulch.
        :return: Integer of cubic yards of mulch
        """
        return min(1, int((self.length * self.width * self.depth) / 324))

    @property
    def time_addition(self) -> int:
        return self.volume

    # Helper function
    def __add__(self, other):
        return Mulch(other.length + self.length, other.width + self.width, other.depth + self.depth)
    def __sub__(self, other):
        return Mulch(self.length - other.width, self.width - other.width, self.depth - other.depth)