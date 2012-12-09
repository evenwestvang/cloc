from time import *
from datetime import *
from lightkeeper import *

class TimeKeeper:

    STATE_IDLE = 0
    STATE_IN_SLOT = 1

    def __init__(self):
        self.timeSlots = [
            {'start':'17:00', 'end':'07:00', 'kind':'night'},
            {'start':'08:30', 'end':'17:30', 'kind':'night'}
        ]

        self.state = self.STATE_IDLE

    def run(self):
        slot = None

        # Keep waiting here until we are in a slot
        while self.state == self.STATE_IDLE:
            for slot in self.timeSlots:
                if self.in_slot(slot):
                    self.current_slot = slot
                    self.state = self.STATE_IN_SLOT
                    print "Entering: " + slot['kind']
            sleep(0.2)
            print "."

        start, end = self.convert_to_current_datetimes(self.current_slot)
        total_delta_seconds = (end - start).total_seconds()
        light_keeper = LightKeeper()

        while self.state == self.STATE_IN_SLOT:
            progress = 1 - ((end - datetime.now()).total_seconds() / total_delta_seconds)
            light_keeper.update(progress)

    def in_slot(self, slot):
        start, end = self.convert_to_current_datetimes(slot)
        now = datetime.now()
        return now > start and now < end

    def convert_to_current_datetimes(self, slot):
        start = self.time_as_datetime(slot['start'])
        end = self.time_as_datetime(slot['end'])

        if end < start:
            end += timedelta(days=1)

        return start, end

    def time_as_datetime(self, time):
        hour, minute = time.split(":")
        time = datetime.today().replace(
            hour=int(hour),
            minute=int(minute),
            second=0)
        return time
