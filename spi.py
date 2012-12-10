from time import *

class Spi:
    def __init__(self):
        self.spidev = file('/dev/spidev0.0', "wb")

    def transmit(self, data):
        self.spidev.write(data)
        self.spidev.flush()
