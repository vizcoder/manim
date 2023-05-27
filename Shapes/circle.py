from manim import *
# from manim import *
# from manim.animation.composition import cc


class MyScene1(Scene):
    def construct(self):
        circle_1 = Circle(radius=1.0, color=BLUE)

        # Create the animation
        draw_circle_1 = Create(circle_1)

        # Play the animation
        self.play(draw_circle_1)


class MySceneScale(Scene):  # grow or scale
    def construct(self):
        # Create your object here
        circle = Circle(radius=1.0, color=BLUE)

        # Add the object to the scene
        self.add(circle)
        self.wait(2)
        # Create the animation
        grow_circle = circle.animate.scale(2)

        # Play the animation
        self.play(grow_circle, run_time=2)


class MySceneScaleAll(Scene):  # scale all the object present in the scene
    def construct(self):
        # Create your objects here
        circle = Circle(radius=1.0, color=BLUE)
        rectangle = RoundedRectangle(
            height=2.0, width=3.0, corner_radius=0.5, color=GREEN)
        text = Tex("Hello, World!", color=WHITE).scale(2)

        # Add the objects to the scene
        self.add(circle, rectangle, text)
        self.wait(2)

        # Create a list of animations to scale each object
        scale_animations = [obj.animate.scale(1.5) for obj in self.mobjects]

        # Create an AnimationGroup from the list of animations
        group_animation = AnimationGroup(*scale_animations)  # type: ignore

        # Play the AnimationGroup
        self.play(group_animation, run_time=5)


class MyScene(Scene):  # animate multiple animation parallel
    def construct(self):
        # Create your objects here
        circle = Circle(radius=1.0, color=BLUE)
        rectangle = RoundedRectangle(
            height=2.0, width=3.0, corner_radius=0.5, color=GREEN)

        # Add the objects to the scene
        self.add(circle, rectangle)
        self.wait(2)

        # Create the animations
        grow_circle = circle.animate.scale(2)
        rotate_rectangle = rectangle.animate.scale(2)

        # Play the animations together
        self.play(grow_circle, rotate_rectangle, run_time=2)
