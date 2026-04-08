from manim import *
import numpy as np


class CubeRotation(ThreeDScene):
    """Rotation matrix in the 3D axes"""
    # Set up the camera orientation for a better view of the 3D scene
    def setup(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, zoom=1)

    # Set up the 3D axes
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-50, 50, 5],
            y_range=[-50, 50, 5],
            z_range=[0, 100, 5],
            x_length=16,
            y_length=16,
            z_length=16,
            axis_config={"color": GREY},
            tips=False,
        )
        # Shift the axes
        axes.shift(RIGHT * 1.2 + UP * 1.1)
        
        origin = axes.get_origin()
        
        
        # Create basis vectors
        i_hat = Arrow3D(origin, axes.c2p(20, 0, 0), color=RED)
        j_hat = Arrow3D(origin, axes.c2p(0, 20, 0), color=GREEN)
        k_hat = Arrow3D(origin, axes.c2p(0, 0, 20), color=BLUE)

        basis_vectors = VGroup(i_hat, j_hat, k_hat)
        
        
        # Label the basis vectors
        label_i = MathTex(r"\hat{i} \, (1, 0, 0)", color=RED, font_size=50)
        label_j = MathTex(r"\hat{j} \, (0, 1, 0)", color=GREEN, font_size=50)
        label_k = MathTex(r"\hat{k} \, (0, 0, 1)", color=BLUE, font_size=50)
        
        label_i.move_to(axes.c2p(25, 0, 0))
        label_j.move_to(axes.c2p(0, 25, 0))
        label_k.move_to(axes.c2p(0, 0, 23))
        
        labels = VGroup(label_i, label_j, label_k)
        
        
        # Create a cube at the center
        cube = Cube(
            side_length=3.2, 
            fill_color=BLUE_C, 
            fill_opacity=0.3,
            stroke_width=1.5, 
            stroke_color=WHITE,
            stroke_opacity=1
        ).move_to(axes.c2p(10, 10, 10))
        

        self.add(axes, basis_vectors, cube)
        self.add_fixed_orientation_mobjects(label_i, label_j, label_k)
        
        self.wait(3)
        
        # ---------------------------------------------------------
        phi = 30 * DEGREES # Define the rotation angle, e.g., 30 degrees
        # Dynamically get the current absolute center coordinates of the cube as the rotation anchor point
        center_point = cube.get_center()

        self.play(
            # 1. Rotate the cube around its center along the X-axis (RIGHT)
            Rotate(cube, angle=phi, axis=LEFT, about_point=center_point),
            run_time=2.5
        )

        self.wait(2)