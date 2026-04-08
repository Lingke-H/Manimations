from manim import *

class IntroducePi(Scene):
    def construct(self):
        # Load the SVG file (make sure the filename matches what you downloaded)
        pi_creature = SVGMobject("PiCreatures_plain.svg")
        
        # Scale him up a bit so he's easy to see
        pi_creature.scale(2)
        
        # The Pi Creature SVG is usually made of multiple parts (body, eyes, pupils).
        # You can set the primary color of the body like this:
        pi_creature.set_color(BLUE_E)
        
        # If you want to customize specific parts (like making the eyes white), 
        # you can access them by their sub-mobject index. 
        # (Note: The exact index depends on the specific SVG file, but usually 
        # the eyes and pupils are the last few elements).
        
        # Animate him appearing on screen!
        self.play(DrawBorderThenFill(pi_creature), run_time=2)
        self.wait(1)
        
        # Make him "jump" to say hello
        self.play(pi_creature.animate.shift(UP * 1.5), run_time=0.3)
        self.play(pi_creature.animate.shift(DOWN * 1.5), run_time=0.3)
        
        self.wait(2)