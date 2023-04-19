from manim import *


class HelloWorld(Scene):
    def construct(self):
        # Display "Hello World"
        hello_world = Text("Hello World", font_size=48)
        self.play(FadeIn(hello_world))

        # Display and explain "print" keyword
        print_kw = Text("print", font_size=36).next_to(hello_world, LEFT)
        print_arrow = Arrow(print_kw.get_right(), hello_world.get_left())
        self.play(FadeIn(print_kw), Create(print_arrow))
        self.wait()

        # Display and explain the opening and closing parenthesis
        parentheses = Text("()", font_size=36).next_to(hello_world, RIGHT)
        open_paren = Text("opening parenthesis",
                          font_size=24).next_to(parentheses, UP)
        close_paren = Text("closing parenthesis",
                           font_size=24).next_to(parentheses, DOWN)
        open_arrow = Arrow(open_paren.get_bottom(), parentheses.get_top())
        close_arrow = Arrow(close_paren.get_top(), parentheses.get_bottom())
        self.play(FadeIn(parentheses), Create(
            open_arrow), Create(close_arrow))
        self.play(FadeIn(open_paren), FadeIn(close_paren))
        self.wait()

        # Display and explain the string "Hello World"
        string_text = Text('"Hello World"', font_size=36).next_to(
            parentheses, RIGHT)
        string_label = Text("string", font_size=24).next_to(string_text, UP)
        string_arrow = Arrow(string_label.get_bottom(), string_text.get_top())
        self.play(FadeIn(string_text), Create(string_arrow))
        self.play(FadeIn(string_label))
        self.wait()

        # Fade out everything
        self.play(FadeOut(print_kw), FadeOut(print_arrow), FadeOut(parentheses), FadeOut(open_paren), FadeOut(
            close_paren), FadeOut(string_text), FadeOut(string_label), FadeOut(string_arrow))
        self.play(FadeOut(hello_world))
