from manim import *
import numpy as np


class CubeRotation(ThreeDScene):
    """3D 坐标轴中的立方体旋转动画"""

    def construct(self):
        # 设置 3D 场景视角
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # 创建坐标轴
        axes = ThreeDAxes(
            x_range=[-0.5, 1.5, 0.5],
            y_range=[-0.5, 1.5, 0.5],
            z_range=[-0.5, 1.5, 0.5],
            axis_config={"color": GREY},
            tips=False,
        )
        
        # 创建基向量
        # x 轴基向量 - 红色
        x_vector = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([1, 0, 0]),
            color=RED,
            thickness=0.1,
        )
        
        # y 轴基向量 - 橙色
        y_vector = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([0, 1, 0]),
            color=ORANGE,
            thickness=0.1,
        )
        
        # z 轴基向量 - 绿色
        z_vector = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([0, 0, 1]),
            color=GREEN,
            thickness=0.1,
        )
        
        # 创建单位立方体（半透明淡蓝色）
        cube = Cube(
            side_length=1,
            fill_color=BLUE_C,
            fill_opacity=0.3,
            stroke_color=BLUE,
            stroke_width=2,
        )
        # 将立方体中心放在 (0.5, 0.5, 0.5)，使其由三个基向量撑出
        cube.move_to(np.array([0.5, 0.5, 0.5]))
        
        # 添加场景元素
        self.add(axes, x_vector, y_vector, z_vector, cube)
        
        # 固定画面 5 秒
        self.wait(5)
        
        # 旋转角度（可修改为 0-90 之间的任意值）
        theta = 45 * DEGREES  # 例如：45 度
        
        # 执行旋转动画（绕 x 轴旋转，yz 平面内旋转）
        # 旋转时长 3 秒
        self.play(
            Rotate(
                cube, 
                angle=theta, 
                axis=np.array([1, 0, 0]), 
                about_point=np.array([0.5, 0.5, 0.5])
            ),
            run_time=3,
        )
        
        self.wait(2)