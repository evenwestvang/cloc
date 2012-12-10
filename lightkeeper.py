#!/usr/bin/env python

# from spi import *
from null import *
from spi import *
from lightsource import *
from numpy import *

class LightKeeper:

    NUMBER_OF_LIGHTS = 32

    def __init__(self):

        self.transmitter = Spi()
        # self.transmitter = Null()
        self.lights = []

        self.lights.append(MainProgressLight())
        self.lights.append(MinuteProgressLight(self.NUMBER_OF_LIGHTS))
        self.lights.append(SecondProgressLight(self.NUMBER_OF_LIGHTS))

    def update(self, progress):
        self.rgb_array = zeros((self.NUMBER_OF_LIGHTS + 1) * 3, 'B')

        for light in self.lights:
            light.update(progress)
            position, l1, l2 = light.render(self.NUMBER_OF_LIGHTS)
            self.set_rgb_values(position, l1)
            self.set_rgb_values(position + 1, l2)
        self.set_buffer()

    def set_rgb_values(self, position, rgb_tuple):
        offset = position * 3
        self.rgb_array[offset + 1] += rgb_tuple[0]
        self.rgb_array[offset + 2] += rgb_tuple[1]
        self.rgb_array[offset + 3] += rgb_tuple[2]

    def set_buffer(self):
        self.transmitter.transmit(self.rgb_array)
