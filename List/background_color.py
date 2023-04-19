# from manim import *


# class MyScene(Scene):
#     def construct(self):
#         # Load the image file
#         img_path = "background.jpg"
#         image = ImageMobject(img_path)
#         print(image)
#         # Scale the image to fill the entire screen
#         image_width = self.camera.get_pixel_width()
#         image_height = self.camera.get_pixel_height()
#         image.set_height(image_height)
#         image.set_width(image_width)

#         # Set the image as the background of the scene
#         self.add(image)

from manim import *


class MyScene(Scene):
    def construct(self):
        # Load the image file
        img_path = "background.jpg"
        image = ImageMobject(img_path)

        # Scale the image to fill the entire screen
        image_width = self.camera.frame_width
        image_height = self.camera.frame_height
        image.set_height(image_height)
        image.set_width(image_width)

        # Set the image as the background of the scene
        self.add(image)
