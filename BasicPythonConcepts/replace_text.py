from manim import *


class TextReplace(Scene):
    def construct(self):
        # Display the original text
        text1 = Text("Hello, World!", font_size=72)
        self.play(Write(text1))

        # Remove the word "Hello"
        text2 = Text(", World!", font_size=72)
        self.play(ReplacementTransform(
            text1[0:5], text2[0]), ReplacementTransform(text1[5:], text2[1:]))

        # Display the new text "Goodbye"
        text3 = Text("Goodbye", font_size=72)
        self.play(ReplacementTransform(text2[2:], text3))
        self.wait()
