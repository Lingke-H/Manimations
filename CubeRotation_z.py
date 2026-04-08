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
        label_i = MathTex(r"\hat{i}", color=RED, font_size=70, stroke_width=1.5)
        label_j = MathTex(r"\hat{j}", color=GREEN, font_size=70, stroke_width=1.5)
        label_k = MathTex(r"\hat{k}", color=BLUE, font_size=70, stroke_width=1.5)

        label_i.move_to(axes.c2p(23,0, 0))
        label_j.move_to(axes.c2p(0, 23, 0))
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
        
        self.wait()
        
        # --------------------------------------------------------- 
        cube_shadow = cube.copy()
        cube_shadow.set_fill(color=GREY, opacity=0.1)
        cube_shadow.set_stroke(color=WHITE, opacity=0.3, width=0.5)
        
        self.add(cube_shadow)
        
        # ---------------------------------------------------------
        # ---------------------------------------------------------
        center_point = cube.get_center()

        # 1. 定义轮播的旋转速度（例如：每秒旋转 45 度）
        # 你可以随意修改这个数值来控制转得快还是慢
        rotation_speed = 45 * DEGREES 

        # 2. 【核心魔法】：给立方体挂上更新器
        # m 代表 cube 本身，dt (delta time) 是两帧之间微小的时间差
        # 这句话的意思是：每一帧都让 cube 绕着 z 轴转动 (速度 * 时间差) 的角度
        cube.add_updater(lambda m, dt: m.rotate(rotation_speed * dt, axis=OUT, about_point=center_point))

        # 3. 控制总时长
        # 因为后台挂了 Updater，只要调用 wait()，画面就不会静止，方块会一直转！
        # 比如这里 wait(10)，视频就会录制 10 秒钟的持续旋转画面
        self.wait(10) 
        
        # 💡 额外提示：如果你在后续动画里想让它停下来，只需要执行：
        # cube.clear_updaters() 
        # 它就会瞬间刹车！