from colorsys import *


class LightSource(object):

    def __init__(self):
        self.position = 0
        self.size = 0
        self.color = (1, 1, 1)

    def render(self, number_of_lights):
        lamp_position = self.position * number_of_lights
        pos = int(lamp_position)
        distribution = lamp_position - pos
        lamp1 = self.rgb_multiply(self.color, 1 - distribution)
        lamp1 = self.rgb_to_integer(lamp1)

        lamp2 = self.rgb_multiply(self.color, distribution)
        lamp2 = self.rgb_to_integer(lamp2)

        return pos, lamp1, lamp2

    def rgb_to_integer(self, rgb):
        return (int(rgb[0] * 255),
                int(rgb[1] * 255),
                int(rgb[2] * 255))

    def rgb_multiply(self, rgb, multipler):
        return (rgb[0] * multipler,
                rgb[1] * multipler,
                rgb[2] * multipler)


class MainProgressLight(LightSource):

    def __init__(self):
        super(MainProgressLight, self).__init__()

    def update(self, progress):
        self.position = progress
        self.color = hls_to_rgb(progress, 0.7, 0.8)


class MinuteProgressLight(LightSource):

    def __init__(self, number_of_lights):
        super(MinuteProgressLight, self).__init__()
        self.number_of_lights = number_of_lights

    def update(self, progress):
        local_progress = (progress * self.number_of_lights) % 1
        self.position = local_progress
        self.color = hls_to_rgb(local_progress, 0.7, 0.8)


class SecondProgressLight(LightSource):

    def __init__(self, number_of_lights):
        super(SecondProgressLight, self).__init__()
        self.number_of_lights = number_of_lights

    def update(self, progress):
        local_progress = (progress * self.number_of_lights * self.number_of_lights) % 1
        self.position = local_progress
        self.color = hls_to_rgb(local_progress, 0.7, 0.8)
