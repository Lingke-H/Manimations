from manim import *

# 1. 我们自己定义一个原生的类
class MyPiCreature(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # 用纯文本生成身体 (完全原生，不需要任何外部文件)
        self.body = MathTex(r"\pi", font_size=120)
        self.body.set_color(BLUE_E)
        
        # 用纯几何图形生成眼睛 (白眼球)
        self.eye_left = Circle(radius=0.15, fill_color=WHITE, fill_opacity=1, stroke_width=0)
        self.eye_right = Circle(radius=0.15, fill_color=WHITE, fill_opacity=1, stroke_width=0)
        
        # 用纯几何图形生成瞳孔 (黑眼珠)
        self.pupil_left = Dot(radius=0.05, color=BLACK)
        self.pupil_right = Dot(radius=0.05, color=BLACK)
        
        # 把眼珠放进眼球里
        self.pupil_left.move_to(self.eye_left.get_center())
        self.pupil_right.move_to(self.eye_right.get_center())
        
        # 把两只完整的眼睛打包
        self.eyes = VGroup(
            VGroup(self.eye_left, self.pupil_left),
            VGroup(self.eye_right, self.pupil_right)
        ).arrange(RIGHT, buff=0.1)
        
        # 把眼睛放在 \pi 的左上方
        self.eyes.next_to(self.body, UP, buff=-0.3).shift(LEFT * 0.2)
        
        # 把身体和眼睛统统打包进这个类
        self.add(self.body, self.eyes)

    # 你甚至可以自己写一个让他转眼珠的专属 Syntax！
    def look_right(self):
        return AnimationGroup(
            self.pupil_left.animate.shift(RIGHT * 0.05),
            self.pupil_right.animate.shift(RIGHT * 0.05)
        )

# 2. 在场景里像调用原生图形一样使用它！
class ShowMyPi(Scene):
    def construct(self):
        # 现在的 Syntax 就这么极其清爽！
        my_pi = MyPiCreature()

        self.play(Write(my_pi), run_time=2)
        self.wait(1)
        
        # 调用我们自己写的动画语法
        self.play(my_pi.look_right())
        self.wait(1)
        
        # 让他开心地跳一下
        self.play(my_pi.animate.shift(UP * 0.5), run_time=0.2)
        self.play(my_pi.animate.shift(DOWN * 0.5), run_time=0.2)
        self.wait(2)