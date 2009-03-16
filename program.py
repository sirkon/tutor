#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Здесь можно писать код программы, он даже будет работать
"""

from shapes import cover, color, width, height


cover.set_color(color.red)
cover.circle(width/2,height/2,width/2-4)
cover.fill()
cover.set_color(color.black)
cover.circle(width/3,height/3,width/9-18)
cover.fill()
cover.set_color(color.black)
cover.circle(width/1.5,height/3,width/9-18)
cover.fill()
cover.set_color(color.blue)
cover.line(100,80)(80,140)
cover.line(100,80)(120,140)
cover.line(80,140)(120,140)
cover.fill()
