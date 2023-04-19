from manim import *


class ListAnimation(Scene):
    def construct(self):
        # Create the list
        my_list = [1, 2, 3]
        list_text = Text("my_list = " + str(my_list)).scale(0.8)
        self.play(Write(list_text))
        self.wait(1)

        # Access the first element in the list
        arrow = Arrow(list_text.get_right(),
                      list_text.get_right() + RIGHT*2).set_color(BLUE)
        index_text = Text("0").next_to(arrow.get_end(), RIGHT)
        element_text = Text(str(my_list[0])).next_to(index_text, RIGHT)
        self.play(Write(arrow), Write(index_text), Write(element_text))
        self.wait(1)

        # Access the second element in the list
        arrow.next_tip = list_text.get_right() + RIGHT*3
        index_text.next_to(arrow.get_end(), RIGHT)
        element_text.next_to(index_text, RIGHT)
        element_text.set_value(str(my_list[1]))
        self.play(Write(arrow), Write(index_text), Write(element_text))
        self.wait(1)

        # Add an element to the list
        arrow.next_tip = list_text.get_right() + RIGHT*4
        index_text.next_to(arrow.get_end(), RIGHT)
        element_text.next_to(index_text, RIGHT)
        new_element_text = Text("4")
        new_element_text.next_to(element_text, RIGHT)
        my_list.append(4)
        list_text.set_value("my_list = " + str(my_list))
        self.play(Write(arrow), Write(index_text), Write(
            element_text), Write(new_element_text))
        self.wait(1)

        # Remove an element from the list
        arrow.next_tip = list_text.get_right() + RIGHT*5
        index_text.next_to(arrow.get_end(), RIGHT)
        element_text.next_to(index_text, RIGHT)
        new_element_text.remove()
        my_list.pop(1)
        list_text.set_value("my_list = " + str(my_list))
        self.play(Write(arrow), Write(index_text), Write(element_text))
        self.wait(1)
