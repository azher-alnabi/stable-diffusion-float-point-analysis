class PixelHashMapCreator:
    def generate_pixel_map(self, pixels: list[int], width: int, height: int) -> dict:
        pixel_map = {}
        for i in range(width):
            for j in range(height):
                pixel = (i+1, j+1)
                pixel_value = pixels[i, j]
                pixel_map[pixel] = pixel_value
        return pixel_map