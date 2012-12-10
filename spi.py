from quick2wire.spi import *
from time import *

class Spi:
    def __init__(self):
        self.spi0 = SPIDevice(0, 0)
        # print ("current speed Hz: " + str(self.spi0.speed_hz))
        # self.spi0.speed_hz = 10000   # 500Khz
        # print ("current speed Hz: " + str(self.spi0.speed_hz))
        # self.spi0.clock_mode = SPI_MODE_1 # | SPI_NO_CS 


    def transmit(self, data):
#            self.spi0.transaction(writing_bytes(0x00, i * 10, i * 10,i * 2))
#            self.spi0.transaction(writing_bytes(0x00, 0, 0))
        self.spi0.transaction(writing_bytes(data))
