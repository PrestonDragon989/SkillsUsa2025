from .mulch import Mulch
from .truck import Truck


# Controls all trucks and their schedules
class Scheduler:
    # Truck sizes
    LARGE_TRUCK_VOLUME: int = 100
    MEDIUM_TRUCK_VOLUME: int = 100
    SMALL_TRUCK_VOLUME: int = 100

    # Total Time (8am to 5pm) - Total Hours * Minutes
    TIME_AVAILABLE: int = 10 * 60

    class TruckSchedule:
        def __init__(self, truck_size: int, time_available: int, name: str):
            self.truck: Truck = Truck(truck_size)

            self.time_available: int = time_available
            self.times: list[(int, int)] = []

            self.name = name

        # Basic adding functions
        def add_load(self, load: Mulch):
            self.truck.add_load(load)

        def add_time(self, start: int, end: int) -> None:
            self.times.append((start, end))

        # Checking if things are possible
        def can_fit(self, load: Mulch):
            return self.truck.can_fit(load)

        def fits_in_truck_schedule(self, start: int, end: int) -> bool:
            print(start, end)
            if start >= 0 and end <= self.time_available:
                pass
            else:
                print("Exceeds")
                return False

            # Already has something scheduled there
            for time in self.times:
                if start not in range(time[0], time[1]) and end not in range(time[0], time[1]):
                    continue

                else:
                    return False

            return True

        # Basic debug print
        def __str__(self):
            s = ""

            for t in self.times:
                s += str(t[0]) + ", " + str(t[1]) + "\n"

            s += "Volume: " + str(self.truck.total_volume)

            return s

    def __init__(self):
        # Getting trucks of different sizes
        self.schedules = [
            self.TruckSchedule(self.LARGE_TRUCK_VOLUME, self.TIME_AVAILABLE, "Large Truck"),
            self.TruckSchedule(self.MEDIUM_TRUCK_VOLUME, self.TIME_AVAILABLE, "Medium Truck"),
            self.TruckSchedule(self.SMALL_TRUCK_VOLUME, self.TIME_AVAILABLE, "Small Truck")
        ]

    def can_add(self, load, start_time: int) -> bool:
        """
        Checks all trucks to see if they fit into the schedule, and have the space
        :param load: Mulch load
        :param start_time: Start time of mulching
        :return: True if fits, False if it doesn't
        """
        end_time: int = start_time + Truck.get_time_of_load(load)

        for schedule in self.schedules:
            if schedule.can_fit(load) and schedule.fits_in_truck_schedule(start_time, end_time):
                return True

        return False

    def has_space(self, load: Mulch) -> bool:
        """
        Iterates through trucks to see if they have space
        :param load:
        :return:
        """
        for schedule in self.schedules:
            if schedule.can_fit(load):
                return True

        return False

    def has_time(self, start, end):
        for schedule in self.schedules:
            if schedule.fits_in_truck_schedule(start, end):
                return True

        return False

    def add_mulch(self, load: Mulch, start_time: int) -> bool:
        """
        Adds a load of mulch to the schedule.
        :param start_time: TIme of scheduling start
        :param load: Load of mulch to add
        :return:
        """
        current_schedule = None
        current_total_size_distance: int or None = None

        end_time = Truck.get_time_of_load(load) + start_time

        # Iterates through trucks to check logic, and then collects index
        for schedule in self.schedules:
            if schedule.can_fit(load) and schedule.fits_in_truck_schedule(start_time, end_time):
                if current_schedule is None:
                    current_schedule = schedule

                size_distance = abs(schedule.truck.volume_available - load.volume)

                if current_total_size_distance is None:
                    current_total_size_distance = size_distance
                elif size_distance < current_total_size_distance:
                    current_total_size_distance = size_distance
                    current_schedule = schedule

        if current_schedule is None:
            return False

        # Adding mulch to schedule
        current_schedule.add_load(load)
        current_schedule.add_time(start_time, end_time)

        return True
