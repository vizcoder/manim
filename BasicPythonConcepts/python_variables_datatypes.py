from manim import *


class PythonConcepts(Scene):
    def construct(self):

        # Display the title of the video
        title = Text("Basic Python Concepts", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Display the text "Declaring Variables and Assigning Values"
        var_title = Text(
            "Declaring Variables and Assigning Values", font_size=36)
        self.play(Create(var_title))
        self.wait(2)
        self.play(FadeOut(var_title))

        # Display an example of declaring a variable and assigning it a value
        code = 'age = 25'
        rendered_code = Code(code=code, tab_width=4, background="window",
                             language="Python", font="Monospace")
        self.play(Create(rendered_code))
        self.wait(2)
        self.play(FadeOut(rendered_code))

        # Display the text "Data Types: Strings, Numbers, Booleans, and None"
        dt_title = Text(
            "Data Types: Strings, Numbers, Booleans, and None", font_size=36)
        self.play(Create(dt_title))
        self.wait(2)
        self.play(FadeOut(dt_title))

        # Display an example of declaring a string variable and assigning it a value
        code = 'name = "Alice"'
        rendered_code = Code(code=code, tab_width=4, background="window",
                             language="Python", font="Monospace")
        self.play(Create(rendered_code))
        self.wait(2)
        self.play(FadeOut(rendered_code))

        # Display an example of declaring a number variable and assigning it a value
        code = 'age = 25'
        rendered_code = Code(code=code, tab_width=4, background="window",
                             language="Python", font="Monospace")
        self.play(Create(rendered_code))
        self.wait(2)
        self.play(FadeOut(rendered_code))

        # Display an example of declaring a boolean variable and assigning it a value
        code = 'is_active = True'
        rendered_code = Code(code=code, tab_width=4, background="window",
                             language="Python", font="Monospace")
        self.play(Create(rendered_code))
        self.wait(2)
        self.play(FadeOut(rendered_code))

        # Display an example of declaring a None variable
        code = 'value = None'
        rendered_code = Code(code=code, tab_width=4, background="window",
                             language="Python", font="Monospace")
        self.play(Create(rendered_code))
        self.wait(2)
        self.play(FadeOut(rendered_code))

        # Display a visual aid showing the relationship between variables and memory
        memory = Text("Memory", font_size=36)
        var_a = Circle(radius=0.4, color=RED).shift(LEFT*2)
        var_b = Circle(radius=0.4, color=YELLOW).next_to(var_a, RIGHT)
        arrow = Arrow(var_a, var_b)
        self.play(Create(memory))
        self.wait(2)
        # self.play(Create(var_a, LEFT), Create(
        self.play(Create(var_a), Create(
            var_b), Create(arrow))
        self.wait(2)
        self.play(FadeOut(var_a, var_b, arrow))

        # Display the conclusion of the video
        conclusion = Text(
            "These are some of the basic Python concepts you need to know to get started!", font_size=36)
        self.play(Create(conclusion))
        self.wait(2)
