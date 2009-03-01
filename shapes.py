#!/usr/bin/env python
# -*- coding: utf-8 -*-

import framework

class Shapes(framework.Screen):
    def draw(self, cr, width, height):
        """
        Заливаем площадь рисования белым цветом
        """
        cr.set_source_rgb(1, 1, 1)
        cr.rectangle(0, 0, width, height)
        cr.fill()
                
        
framework.run(Shapes)
