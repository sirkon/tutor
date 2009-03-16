#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Здесь можно писать код программы, он даже будет работать
"""

from shapes import cover, color, width, height


cover.set_color(color.pink)
cover.circle(width/2,height/2,width/2-4)
cover.fill()
cover.set_color(color.black)
cover.circle(width/3,height/3,width/9-18)
cover.fill()
cover.set_color(color.black)
cover.circle(width/1.5,height/3,width/9-18)
cover.fill()
cover.set_color(color.red1)
cover.move_to(100,80)
cover.line_to(80,140)
cover.line_to(120,140)
cover.line_to(100,80)
cover.fill()
cover.set_color(color.red)
cover.move_to(70,170)
cover.line_to(130,170)
string= "Денис"
print string

