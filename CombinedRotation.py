from manim import *
import numpy as np

class CubeRotation(ThreeDScene):
    """Rotation matrix in the 3D axes"""
    def setup(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES, zoom=1)

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

        label_i.move_to(axes.c2p(23, 0, 0))
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

        vertex_point = axes.c2p(20, 20, 20)
        vertex_dot = Dot3D(point=vertex_point, radius=0.08, color=YELLOW, fill_opacity=1)
        
        # 将方块和圆点打包为物理刚体
        rotating_group = VGroup(cube, vertex_dot)
        
        self.add(axes, basis_vectors, rotating_group)
        self.add_fixed_orientation_mobjects(label_i, label_j, label_k)
        
        self.wait(3)
        
        # --------------------------------------------------------- 
        # 第一阶段：绕 Z 轴 (OUT) 旋转 30 度
        # ---------------------------------------------------------
        cube_shadow_1 = cube.copy()
        cube_shadow_1.set_fill(color=GREY, opacity=0.1)
        cube_shadow_1.set_stroke(color=WHITE, opacity=0.3, width=0.5)
        self.add(cube_shadow_1)
        
        theta_1 = 30 * DEGREES 
        center_point = cube.get_center()

        path_center_z = axes.c2p(10, 10, 20) 
        path_radius_z = np.linalg.norm(vertex_dot.get_center() - path_center_z)
        
        angle_tracker_z = ValueTracker(0.01) 
        
        trajectory_arc_z = always_redraw(
            lambda: Arc(
                arc_center=path_center_z,
                radius=path_radius_z,
                start_angle=PI/4,
                angle=angle_tracker_z.get_value(), 
                color=BLUE,
                stroke_width=4
            ).set_opacity(0.8).add_tip(tip_length=0.2)
        )
        self.add(trajectory_arc_z)

        self.play(
            Rotate(rotating_group, angle=theta_1, axis=OUT, about_point=center_point),
            angle_tracker_z.animate.set_value(theta_1),
            run_time=2.5
        )
        self.wait(1) # 两次旋转间稍微停顿 1 秒

        # ---------------------------------------------------------
        # 第二阶段：绕 Y 轴 (UP) 旋转 30 度
        # ---------------------------------------------------------
        theta_2 = 30 * DEGREES

        trajectory_arc_y = TracedPath(
            vertex_dot.get_center,  # 实时抓取黄点的物理中心
            stroke_color=GREEN,     # 使用绿色
            stroke_width=4
        ).set_opacity(0.8)
        self.add(trajectory_arc_y)

        # 3. 执行绕 Y 轴的旋转
        self.play(
            Rotate(rotating_group, angle=theta_2, axis=UP, about_point=center_point),
            run_time=2.5
        )

        self.wait(1)
        
        # ---------------------------------------------------------
        # 第三阶段：绕 X 轴 (UP) 旋转 30 度
        # ---------------------------------------------------------
        theta_3 = 30 * DEGREES

        # 1. 抓取第三次旋转起点的绝对几何信息
        P_start_x = vertex_dot.get_center()
        C_rot_x = np.array([P_start_x[0], center_point[1], center_point[2]])
        v_x = P_start_x - C_rot_x

        trajectory_arc_x = ParametricFunction(
            lambda t: C_rot_x + rotate_vector(v_x, angle=t, axis=RIGHT),
            t_range=[0, theta_3], 
            color=RED,
            stroke_width=4
        )
        
        trajectory_arc_x.set_opacity(0.8)

        # 3. 执行动画：Create 和 Rotate 同步
        # Create 像画笔一样把已经准备好的弧线从头画到尾
        self.play(
            Rotate(rotating_group, angle=theta_3, axis=RIGHT, about_point=center_point),
            Create(trajectory_arc_x), 
            run_time=2.5
        )

        self.wait(2)