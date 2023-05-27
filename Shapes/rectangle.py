from manim import *


class MyScene1(Scene):
    def construct(self):
        rect_1 = RoundedRectangle(
            height=2.0, width=3.0, corner_radius=0.5, color=BLUE)
        rect_2 = RoundedRectangle(height=4.0, width=4.0, corner_radius=1.5)

        rect_group = Group(rect_1, rect_2).arrange(buff=1)
        self.add(rect_group)
        # self.play(rect_1)


class MyScene(Scene):
    def construct(self):
        rect_1 = RoundedRectangle(
            height=2.0, width=3.0, corner_radius=0.5, color=BLUE)

        # Create the animation
        draw_rect_1 = Create(rect_1)

        # Play the animation
        self.play(draw_rect_1)





