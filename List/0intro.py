from manim import *


class PythonListsTitle(Scene):
    def load_image(self):
        img_path = "background.jpg"
        image = ImageMobject(img_path)

        # Scale the image to fill the entire screen
        image_width = self.camera.frame_width
        image_height = self.camera.frame_height
        image.set_height(image_height)
        image.set_width(image_width)
        return image

    def construct(self):
        # img_path = "background.jpg"
        # image = ImageMobject(img_path)

        # # Scale the image to fill the entire screen
        # image_width = self.camera.frame_width
        # image_height = self.camera.frame_height
        # image.set_height(image_height)
        # image.set_width(image_width)
        image = self.load_image()
        # Set the image as the background of the scene
        self.add(image)

        # Create title text
        title = Text("Python Lists", font_size=96, color=WHITE, weight=BOLD)

        # Create bullet points for video contents
        contents = VGroup(
            Text("Introduction to Lists", font_size=36, color=WHITE),
            Text("List Methods", font_size=36, color=WHITE),
            Text("Slicing and Indexing", font_size=36, color=WHITE),
            Text("Nested Lists", font_size=36, color=WHITE),
            Text("List Comprehensions", font_size=36, color=WHITE),
            Text("Common Errors", font_size=36, color=WHITE),
            Text("Best Practices", font_size=36, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT).shift(DOWN)

        # Animate title and bullet points into view
        self.play(Write(title), run_time=1)
        self.play(title.animate.to_edge(UP))
        self.play(*[Write(content) for content in contents], run_time=2
                  )
        self.play(FadeOut(contents), run_time=2)

        # Replace title with new title
        new_title = Text("Introduction to Lists", font_size=72,
                         color=WHITE, weight=BOLD).to_edge(UP)
        self.play(Transform(title, new_title), run_time=1)
        self.wait(2)
