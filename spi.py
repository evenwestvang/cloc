from quick2wire.spi import *
from time import *

class Spi:
    def __init__(self):
        self.spi0 = SPIDevice(0, 0)
        self.spi0.speed_hz = 100000   # 500Khz
        self.spi0.clock_mode = SPI_MODE_2 | SPI_NO_CS 

    def transmit(self, data):
#        for i in range(255):
#            self.spi0.transaction(writing_bytes(0xf0, 0x80, 0x80,0xf0, 0, 0, 0, 0))
#            sleep(0.1)
        self.spi0.transaction(writing_bytes(data))
