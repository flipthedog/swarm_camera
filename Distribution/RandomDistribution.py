import random
import time
class RandomDistribution:

    def __init__(self, swarm_number):
        self.swarm_number = swarm_number

    def createRandomDistribution(self, image):
        black_pixels = self.find_black_pixels(image)

        rand_distr = self.random_distribution(black_pixels)
        return rand_distr

    def find_black_pixels(self, image):
        return_arr = []

        height, width = image.shape

        for i in range(0, width):

            for j in range(0, height):

                if image[j][i] == 0:
                    pixel = [i * 3, j * 3]
                    return_arr.append(pixel)

        return return_arr

    def random_distribution(self, black_pixel_array):

        return_arr = []

        length = len(black_pixel_array)

        for i in range(0, self.swarm_number):
            randomnum = random.randint(0, length - 1)

            return_arr.append(black_pixel_array[randomnum])

        return return_arr