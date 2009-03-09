#!/usr/bin/env python
# -*- coding: utf-8 -*-

import framework
import threading

height = 40
width  = 40

class Record (dict):
    def __init__ (self, **kwarg):
        super (Record, self).__init__ (**kwarg)
        self.__dict__.update (**kwarg)

color = Record (\
    red = (255,0,0), orange = (255,0xa5,0), yellow = (255,255,0), green = (0,0x80,0), blue = (0,0,255), violet = (0x4b,0,0x82),\
    white = (255,255,255), black = (0,0,0) \
    )

def prepare (f):
    def prepared (cl, *args, **kwargs):
        cl.lock.acquire ()
        f (cl, *args, **kwargs)
        framework.widget.queue_draw ()
        cl.lock.release ()
    return prepared

class  Cover:
    """
    Вспомогательный класс. Используется для отложенного рисования.
    """
    def __init__ (self):
        self.lock = threading.Lock ()
        self.operations = []
        self.screen = None

    @prepare
    def move_to (self, x, y):
        self.operations.append (lambda c: c.move_to(x,y))

    @prepare
    def set_color (self, new_color):
        r,g,b = [i/255.0 for i in new_color]
        self.operations.append (lambda c: c.stroke())
        self.operations.append (lambda c: c.set_source_rgb (r,g,b))

    @prepare
    def line_to (self, x, y):
        self.operations.append (lambda c: c.line_to(x,y))
        
    def line (self, x, y):
        self.move_to (x, y)
        return self.line_to

cover = Cover ()
cover_not_initiated = True
        

class Shapes(framework.Screen):
    def draw(self, cr, w, h):
        """
        Заливаем площадь рисования белым цветом
        """
        global width, height
        width, height = w - 1, h - 1
        if cover_not_initiated:
            cover.screen = self
        cr.set_source_rgb(1, 1, 1)
        cr.rectangle(0, 0, width, height)
        cr.fill()
        cr.set_source_rgb(0, 0, 0)

        cover.lock.acquire ()
        for operation in cover.operations:
            operation (cr)
        cover.lock.release ()
        cr.stroke ()

        

class MyThread (threading.Thread):
    def run (self, *args):
        framework.run(Shapes)

MyThread().start()
