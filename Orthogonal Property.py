from manim import *
import numpy as np

class OrthogonalProperty(Scene):
    def construct(self):
        # 1. 创建底层网格
        grid = NumberPlane(
            x_range=[-10, 10, 1], y_range=[-10, 10, 1],
            background_line_style={"stroke_color": GREY, "stroke_opacity": 0.5}
        )
        self.add(grid)

        # 2. 定义两个初始向量
        vec_u = Vector([5, 0], color=RED)
        vec_v = Vector([3, 4], color=GREEN) 
        
        # 3. 静态创建夹角 (删掉 always_redraw！把它变成一个纯粹的几何图形)
        angle_arc = Angle(vec_u, vec_v, radius=0.8, color=WHITE)
        
        # 4. 将网格、向量，【以及夹角弧线本身】全部打包！
        # 这样它就会成为刚体的一部分，乖乖跟着大部队移动和旋转
        moving_group = VGroup(grid, vec_u, vec_v, angle_arc)
        
        moving_group.shift(LEFT * 2 + DOWN * 2)
        
        self.play(
            # 网格在底层稳稳地画 2 秒
            Create(grid, run_time=2), 
            
            # 同时开启一个 2 秒的接力赛：前 1 秒长箭头，后 1 秒画弧线
            Succession(
                AnimationGroup(GrowArrow(vec_u), GrowArrow(vec_v), run_time=1),
                Create(angle_arc, run_time=1)
            )
        )
        self.wait(1)

        # ---------------------------------------------------------
        # 4. 施加正交变换！(纯视觉展示)
        # ---------------------------------------------------------
        theta = 35 * DEGREES
        Q_matrix = [[np.cos(theta), -np.sin(theta)], 
                    [np.sin(theta),  np.cos(theta)]]

        # ---------------------------------------------------------
        # 修复二：加上 about_point 锚点，让它原地乖乖旋转！
        # ---------------------------------------------------------
        self.play(
            # grid.get_origin() 会极其精准地抓取移动后网格的中心坐标
            moving_group.animate.apply_matrix(Q_matrix, about_point=grid.get_origin()),
            run_time=3,
            path_arc=theta 
        )
        self.wait(2)