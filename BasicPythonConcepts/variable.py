# from manim import *


# class HelloWorld(Scene):
#     def construct(self):
#         # Display "Hello World"
#         hello_world = Text('print("Hello World")', font_size=48).shift(UP*2)
#         self.play(FadeIn(hello_world))
#         # arrow_3 = Arrow(start=LEFT, end=RIGHT)
#         arrow_3 = Arrow(start=DOWN, end=UP).next_to(
#             hello_world, DOWN).shift(RIGHT * .8)
#         underline = Underline(hello_world[6:-1], buff=0.1)

#         self.play(FadeIn(arrow_3), FadeIn(underline))
#         self.wait(2)
#         text1 = Text('This is a String', font_size=24).next_to(arrow_3, DOWN)


from manim import *

class MovingAround(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=1)

        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))