from manim import *


class AddText(Scene):
    def construct(self):
        text = Text("Your Text")
        self.add(text)
        self.wait()
        self.remove(text)
        self.wait()


class WriteText(Scene):
    def construct(self):
        text = Text("Your Text")
        self.play(Write(text), run_time=4)
        self.wait()


class AddLetterByLetter(Scene):
    def construct(self):
        text = Text("Your Text")
        self.play(AddTextLetterByLetter(text))
        self.wait()


class CreateText(Scene):
    def construct(self):
        text = Text("Your Text")
        # run_time sets the animation duration to any float number
        self.play(Create(text), run_time=4)
        self.wait()
        self.play(Uncreate(text), run_time=2)
        self.wait()


class DrawBorderThenFillText(Scene):
    def construct(self):
        text = Text("Your Text")
        self.play(DrawBorderThenFill(text))
        self.wait()


class GrowText(Scene):
    def construct(self):
        text = Text("Your Text")
        # you can also grow from any other point, see below
        self.play(GrowFromCenter(text))
        self.wait()
        # but you can only shrink to the center
        self.play(ShrinkToCenter(text))
        self.wait()


class GrowFromPointText(Scene):
    def construct(self):
        text = Text("Your Text")
        # points have to be defined in 3D coordinates, so [x,y,z], even though there is no actual z coordinate
        self.play(GrowFromPoint(text, point=[-4, 2, 0]))
        self.wait()
        self.play(ShrinkToCenter(text))
        self.wait()


class FadeText(Scene):
    def construct(self):
        text = Text("Your Text")
        self.play(FadeIn(text))
        self.wait()
        self.play(FadeOut(text))
        self.wait()
