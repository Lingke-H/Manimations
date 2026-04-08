from manim import *

class HelloManim(Scene):
    def construct(self):

        greeting = Text("Mathematical Methods for Creating 3D-to-2D Projection", font_size=40, gradient=[BLUE, GREEN, YELLOW])

        self.play(Write(greeting, run_time=2))
        self.wait(5)