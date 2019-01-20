import random

class RandomDistribution:

    def __init__(self, swarm_number):
        self.swarm_number = swarm_number

    def createRandomDistribution(self, image):
        black_pixels = self.find_black_pixels(image)
        return self.random_distribution(black_pixels)

    def find_black_pixels(self, image):
        return_arr = []

        height, width = image.shape

        for i in range(0, width):

            for j in range(0, height):

                if image[j][i] == 0:
                    pixel = [i, j]
                    return_arr.append(pixel)

        return return_arr

    def random_distribution(self, black_pixel_array):

        return_arr = []

        length = len(black_pixel_array)

        for i in range(0, self.swarm_number):
            randomnum = random.randint(0, length - 1)

            return_arr.append(black_pixel_array[randomnum])

        return return_arr