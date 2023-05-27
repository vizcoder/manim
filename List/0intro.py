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
        # Set the image as the background of the scene
        image = self.load_image()
        self.add(image)

        # Create title text
        title = Text("Python Lists", font_size=96, color=BLUE_C, weight=BOLD)

        # Create bullet points for video contents
        contents = VGroup(
            Text("Introduction to Lists", font_size=36, color=GOLD_C),
            Text("List Methods", font_size=36, color=GOLD_C),
            Text("Slicing and Indexing", font_size=36, color=GOLD_C),
            Text("Nested Lists", font_size=36, color=GOLD_C),
            Text("List Comprehensions", font_size=36, color=GOLD_C),
            Text("Common Errors", font_size=36, color=GOLD_C),
            Text("Best Practices", font_size=36, color=GOLD_C),
        ).arrange(DOWN, aligned_edge=LEFT).shift(DOWN)

        # Animate title and bullet points into view
        self.play(Write(title), run_time=2)
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        self.play(*[Write(content) for content in contents], run_time=2
                  )
        self.wait(2)
        self.play(FadeOut(contents), run_time=2)

        # Replace title with new title
        new_title = Text("Introduction to Lists", font_size=72,
                         color=BLUE_C, weight=BOLD).to_edge(UP)
        self.play(Transform(title, new_title), run_time=1)
        self.wait(2)

        # Introduction to python
        # code = Text("[1, 2, 3, 'hello', 'world']",
        #             font_size=36, color=BLUE_C, weight=BOLD)
        # self.play(Write(code), run_time=2)
        # self.wait(2)
        # Create the bracket for the list
        bracket = Tex("[ ]", color=RED_C, font_size=96)
        self.play(Write(bracket), run_time=1)
        self.wait(2)

        # Create a list with only numbers
        numbers_list = Tex("[1, 2, 3, 4, 5]", color=RED_C,
                           font_size=72)
        self.play(FadeTransform(bracket, numbers_list), run_time=1)
        self.wait(2)

        # Create a list with only strings
        strings_list = Tex("['hello', 'world', 'manim']",
                           color=RED_C, font_size=72)
        self.play(FadeTransform(numbers_list, strings_list), run_time=1)
        self.wait(2)

        # Create a list with both numbers and strings
        mixed_list = Tex("[1, 'hello', 2, 'world']",
                         color=RED_C, font_size=72)
        self.play(FadeTransform(strings_list, mixed_list), run_time=1)
        self.wait(4)

# "Let's start our introduction to lists by visualizing an empty list. In Python, we represent an empty list using square brackets: []"
# "As we add elements to the list, it grows in size. Here, we have a list with numbers: [1, 2, 3, 4, 5]"
# "Lists can also contain strings. Here, we have a list with strings: ['hello', 'world', 'manim']"
# "Python lists are flexible. We can mix different data types in a single list. Look at this list with both numbers and strings: [1, 'hello', 2, 'world']"

        # List_method

        new_title = Text("List Methods", font_size=72,
                         color=BLUE_C, weight=BOLD).to_edge(UP)
        self.play(Transform(title, new_title), FadeOut(mixed_list), run_time=1)
        # self.play(FadeOut(mixed_list), run_time=2)
        # self.play(FadeOut(strings_list), run_time=2)

        self.wait(2)
        # Define the code as a string
        code = "my_list = [1, 2, 3, 4]"

        # Create the variable as a Code object
        my_list_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace", font_size=36)

        # Create the list as a Text object
        my_list = Tex("[1, 2, 3, 4]", color=RED_C, font_size=96)
        # self.wait(2)

        # Position the list and variable on the screen
        # my_list.to_edge(UP).shift(0.5*DOWN)
        my_list_code.next_to(mixed_list, DOWN).shift(1.5*DOWN)

        # Animate the list and variable into view
        # self.play(Write(mixed_list), run_time=1)
        # self.wait(1)
        self.play(Write(my_list_code), run_time=1)
        self.play(Write(my_list), run_time=1)
        self.wait(2)

        # Define the code as a string
        new_code = """my_list = [1, 2, 3, 4]\nmy_list.append(5)"""

        # Create the variable as a Code object
        new_list_code = Code(code=new_code, tab_width=4, background="window",
                             language="Python", font="Monospace", font_size=36).next_to(mixed_list, DOWN).shift(1.5*DOWN)

        # Animate the change from old code to new code
        self.play(Transform(my_list_code, new_list_code), run_time=1)
        self.wait(5)

        # Create the curved arrow
        curved_arrow = CurvedArrow(start_point=my_list.get_right(
        ) + 0.1*RIGHT, end_point=my_list.get_right()+2*RIGHT, angle=-TAU/4, color=YELLOW)

        # Animate the curved arrow pointing
        self.play(Create(curved_arrow), run_time=1)
        self.wait(1)
        # Create the new element
        new_element = Tex("5", color=YELLOW, font_size=72)
        new_element.next_to(curved_arrow, RIGHT,).shift(DOWN * 0.2)

        # Show the new element after the list
        self.play(Write(new_element), run_time=1)
        self.wait(1)

        self.play(FadeOut(new_element), FadeOut(curved_arrow), run_time=.5)
        # self.wait(1)

        # Update the list with the new element
        updated_list = Tex("[1, 2, 3, 4, 5]", color=RED_C, font_size=96)
        self.play(Transform(my_list, updated_list), run_time=1)
        self.wait(2)

        # Define the code for inserting a value
        insert_code = """my_list = [1, 2, 3, 4, 5]\nmy_list.insert(2, 22)"""

        # Create the code for inserting a value as a Code object
        insert_list_code = Code(code=insert_code, tab_width=4, background="window",
                                language="Python", font="Monospace", font_size=36).next_to(updated_list, DOWN).shift(1.5*DOWN)

        # Animate the change from the previous code to the code for inserting a value
        self.play(Transform(my_list_code, insert_list_code), run_time=1)
        self.wait(5)

        # # Create the new element for insertion
        # insert_element = Tex("22", color=YELLOW, font_size=72)
        # insert_element.next_to(updated_list[2], RIGHT, buff=0.5)

        # # Insert the new element into the list
        # self.play(Write(insert_element), run_time=1)
        # self.wait(1)
        # self.play(
        #     TransformFromCopy(insert_element, updated_list[3]),
        #     TransformFromCopy(updated_list[3:], updated_list[4:]),
        #     run_time=2
        # )
        # self.wait(2)

        # my_list_new = Tex("[1, 2, 3, 4, 5]",
        #                   color=RED_C, font_size=72)
        # self.play(FadeTransform(my_list, my_list_new), run_time=2)
        # self.wait(2)

        # #
        # #
        # #
        # #        # Create the original list
        # original_list = Tex("[1, 2, 3, 4]", color=WHITE, font_size=72)

        # # Display the original list
        # self.play(Write(original_list), run_time=1)
        # self.wait(2)

        #
        #
        #
        #

        # Slicing and Indexing
        # Replace title with new title
        # new_title = Text("Slicing and Indexing", font_size=72,
        #                  color=BLUE_C, weight=BOLD).to_edge(UP)
        # self.play(Transform(title, new_title), run_time=1)
        # self.wait(2)
        # # Define the code as a string
        # code = "my_list = [1, 'hello', 2, 'world']"

        # # Create the variable as a Code object
        # my_list_var = Code(code=code, tab_width=4, background="window",
        #                    language="Python", font="Monospace", font_size=36)

        # # Create the list as a Text object
        # # my_list = Text("[1, 'hello', 2, 'world']", color=WHITE, font_size=72)

        # # Position the list and variable on the screen
        # # my_list.to_edge(UP).shift(0.5*DOWN)
        # my_list_var.next_to(mixed_list, DOWN).shift(1.5*DOWN)

        # # Animate the list and variable into view
        # # self.play(Write(mixed_list), run_time=1)
        # # self.wait(1)
        # self.play(Write(my_list_var), run_time=1)
        # self.wait(1)


class List_Methods(Scene):
    def construct(self):
        # Add a new title to the top of the scene
        title = Text("List Methods", font_size=72,
                     color=BLUE_C, weight=BOLD).to_edge(UP)
        self.play(Write(title), run_time=1)
        self.wait(1)
        # List_method

        code = "my_list = [1, 2, 3, 4]"

        # Create the variable as a Code object
        my_list_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace", font_size=24).to_edge(LEFT)

        # Create the list as a Text object
        my_list = Text("[1, 2, 3, 4]", color=RED_C,
                       font_size=48).to_edge(RIGHT).shift(LEFT*3)

        self.play(Write(my_list_code), run_time=1)
        self.play(Write(my_list), run_time=1)
        self.wait(2)
        # raise Exception("Stopping execution")

        # Create the text object for "append"
        append_text = Text(
            "append()",
            color=PURPLE_D,
            font="Monospace",
            font_size=54
        )
        # Position the text object at the bottom center of the screen
        append_text.to_edge(DOWN)
        append_text.shift(UP * 0.5)

        # Display the "append" text object
        self.play(Write(append_text), run_time=2)
        self.wait(2)

        # Define the code as a string
        new_code = """my_list = [1, 2, 3, 4]\nmy_list.append(5)"""

        # Create the variable as a Code object
        new_list_code = Code(code=new_code, tab_width=4, background="window",
                             language="Python", font="Monospace", font_size=24, line_spacing=1.5).to_edge(LEFT)

        # Animate the change from old code to new code
        self.play(Transform(my_list_code, new_list_code), run_time=1)
        self.wait(5)

        # Create the curved arrow
        curved_arrow = CurvedArrow(end_point=my_list.get_right(
        ) + 0.1*RIGHT, start_point=my_list.get_right()+2*RIGHT, angle=TAU/4, color=YELLOW)

        # Animate the curved arrow pointing
        self.play(Create(curved_arrow), run_time=1)
        self.wait(1)
        # Create the new element
        new_element = Tex("5", color=YELLOW, font_size=72)
        new_element.next_to(curved_arrow, RIGHT,).shift(DOWN * 0.2)

        # Show the new element after the list
        self.play(Write(new_element), run_time=1)
        self.wait(1)

        # self.play(FadeOut(new_element), FadeOut(curved_arrow), run_time=.5)
        # self.wait(1)

        # Update the list with the new element
        updated_list = Text("[1, 2, 3, 4, 5]", color=RED_C,
                            font_size=48, t2c={'5': YELLOW}).to_edge(RIGHT).shift(LEFT*2)
        # updated_list[2].set_color(YELLOW)
        self.play(Transform(my_list, updated_list), FadeOut(
            new_element), FadeOut(curved_arrow), run_time=1)
        self.wait(2)

        # Define the code for inserting a value

        self.play(FadeOut(append_text), run_time=1)
        # insert_code = """my_list = [1, 2, 3, 4, 5]\nmy_list.insert(2, 22)"""

        # # Create the code for inserting a value as a Code object
        # insert_list_code = Code(code=insert_code, tab_width=4, background="window",
        #                         language="Python", font="Monospace", font_size=36).next_to(updated_list, DOWN).shift(1.5*DOWN)

        # # Animate the change from the previous code to the code for inserting a value
        # self.play(Transform(my_list_code, insert_list_code), run_time=1)
        # self.wait(5)
