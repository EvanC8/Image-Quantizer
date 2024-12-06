from Pixel import Pixel
from PIL import Image
import random
import math

# HOW IT WORKS:
    # Each pixel's RGB color value represents a point in 3D space
    # Central points are chosen at random using a weighted probability
    # Points are then clustered based on their closest central points
    # "k" number of clusters are created
    # Dominant colors - Each cluster is then averaged to one rgb value
    # Image Quantization - Dominant colors can then be mapped to

# K-means++ Algorithm implementation
# Quantize a provided image with "k" number of dominant colors
class KMeans:
    def __init__(self, image, k):
        # open image
        self.image = Image.open(image)
        self.width, self.height = self.image.size

        # Set number of clusters
        self.k = k

        # Initialize centroids array
        self.centers = []

        # Initialize weighted total
        self.weighted_total = None

        # Initialize Pixels array
        self.pixels = []
        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                rgb = self.image.getpixel((x, y))
                rgb = tuple(num / 255 for num in rgb)
                row.append(Pixel(row=y, col=x, rgb=rgb, center=None, weight=None, weight_sum=None))
            self.pixels.append(row)


# ------------MAIN METHODS --BELOW-- -------------------------------

    # Returns a list of the "k" dominant colors in the given image
    def dominate_colors(self):
        for i in range(self.k):
            self.generate_center()

        dom_colors = self.average_clusters()
        return dom_colors

    # Returns the given image quantized with the "k" dominant colors
    def quantize(self):
        quantized = Image.new('RGB', self.image.size)

        dom_colors = self.dominate_colors()

        for y in range(self.height):
            for x in range(self.width):
                original_color = self.image.getpixel((x, y))
                new_color = self.closest_color(original_color, palette=dom_colors)
                quantized.putpixel((x, y), new_color)

        quantized.show()



# ------------PRIVATE HELPER METHODS --BELOW-- ----------------------

    # Generates a new centroid and updates the pixel centers/weights
    def generate_center(self):
        if len(self.centers) == 0:
            rand = random.randint(0, self.width * self.height)
            center = self.pixels_flat()[rand]
            self.centers.append(center)
        else:
            center = self.centers[0]
            while center in self.centers:
                rand = random.uniform(0, self.weighted_total)
                center = KMeans.pixel_search(self.pixels_flat(), 0, len(self.pixels) - 1, rand)
            self.centers.append(center)

        self.set_centers()
        return

    # Updates all pixel centers/weights
    def set_centers(self):
        self.weighted_total = 0

        for row in range(0, self.height):
            for col in range(0, self.width):
                pixel = self.pixels[row][col]

                closest = self.closest_center(pixel)
                pixel.set_center(closest)

                dist = KMeans.distance(pixel.rgb(), closest.rgb())
                pixel.set_weight(dist)
                self.weighted_total += dist
                pixel.set_weight_sum(self.weighted_total)

        return

    # Returns a list of the average color values of the clusters
    def average_clusters(self):
        averages = []

        for center in self.centers:
            cluster = [pixel for pixel in self.pixels_flat() if pixel.center is center]
            avg = KMeans.average_color(cluster)
            if avg is not None:
                r, g, b = (round(num * 255) for num in avg)
                averages += [(r, g, b)]

        return averages

    # Returns the best fitting color from a palette relative to a given color
    def closest_color(self, color, palette):
        shortest_dist = None
        best_color = None

        for option in palette:
            dist = KMeans.distance(color, option)
            if shortest_dist is None or dist < shortest_dist:
                shortest_dist = dist
                best_color = option

        return best_color

    # Returns pixels array represented a flattened 1D array
    def pixels_flat(self):
        return [pixel for row in self.pixels for pixel in row]

    # Returns the Euclidean distance between 2 RGB colors in 3D space
    @staticmethod
    def distance(color1, color2):
        rdx = color1[0] - color2[0]
        gdx = color1[1] - color2[1]
        bdx = color1[2] - color2[2]
        return rdx * rdx + gdx * gdx + bdx * bdx

    # Returns the center closest to a given pixel in the rgb color space
    def closest_center(self, pixel):
        if len(self.centers) == 1:
            return self.centers[0]

        lowest = None
        closest = None

        for center in self.centers:
            distance = KMeans.distance(center.rgb(), pixel.rgb())
            if lowest is None or distance < lowest:
                lowest = distance
                closest = center

        return closest

    # Returns the largest pixel with a weighted sum lower than a given weight
    @staticmethod
    def pixel_search(pixels, low, high, goal_weight):
        if low > high:
            low = low if low < len(pixels) else len(pixels) - 1
            return pixels[low]

        mid = (low + high) // 2
        weighted_sum = pixels[mid].weight_sum

        if weighted_sum >= goal_weight:
            return KMeans.pixel_search(pixels, low, mid - 1, goal_weight)
        else:
            return KMeans.pixel_search(pixels, mid + 1, high, goal_weight)

    # Returns the average rgb color among a group of pixels
    @staticmethod
    def average_color(pixels):
        if len(pixels) == 0:
            return None

        r, g, b, = 0, 0, 0
        for pixel in pixels:
            r += pixel.r
            g += pixel.g
            b += pixel.b

        r /= len(pixels)
        g /= len(pixels)
        b /= len(pixels)

        return r, g, b







