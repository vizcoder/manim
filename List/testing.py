from manim import *


class ListAddElement(Scene):
    def construct(self):
        # Create the original list
        list_elements = VGroup(
            Tex("1", color=RED_C, font_size=96),
            Tex(", ", color=WHITE, font_size=96),
            Tex("2", color=RED_C, font_size=96),
            Tex(", ", color=WHITE, font_size=96),
            Tex("3", color=RED_C, font_size=96),
            Tex(", ", color=WHITE, font_size=96),
            Tex("4", color=RED_C, font_size=96),
            Tex(", ", color=WHITE, font_size=96),
            Tex("5", color=RED_C, font_size=96)
        )
        list_elements.arrange(RIGHT, buff=0.5)

        # Create the brackets
        opening_bracket = Tex("[", color=WHITE, font_size=96)
        closing_bracket = Tex("]", color=WHITE, font_size=96)

        # Position the brackets
        opening_bracket.next_to(list_elements, LEFT, buff=0.2)
        closing_bracket.next_to(list_elements, RIGHT, buff=0.2)

        # Group the brackets and list elements
        original_list = VGroup(opening_bracket, list_elements, closing_bracket)

        # Display the original list
        self.play(Write(original_list), run_time=1)
        self.wait(2)

        # Create the new element
        new_element = Tex(", 6", color=WHITE, font_size=96)
        new_element.next_to(list_elements[-1], RIGHT, buff=0.5)

        # Add the new element to the list
        updated_list_elements = VGroup(*list_elements, new_element)

        # Animate the addition of the new element
        self.play(Write(new_element), run_time=1)
        self.wait(1)
        self.play(Transform(list_elements, updated_list_elements), run_time=1)
        self.wait(2)
