# -*- coding: utf-8 -*-

from vector import *
from record import Record
import math

def sgn(a):
    if a < 0.0:
        return -1.0
    if a > 0.0:
        return 1.0
    return 0.0

def calculate_arc_parameters (edge1, edge2, mp):
    a = edge1 - mp
    b = edge2 - mp
    c = edge1 - edge2
    R = reduce (lambda x,y: x*y, Vector(map(norm, [a,b,c])))/abs(2.0*det(a,b))
    M = (edge1 + edge2)/2.0
    l = edge2 - edge1
    d = math.sqrt(R**2 - norm(l/2)**2)
    n = orth(Vector(-l.y,l.x))*d
    L = lambda p: dot(n,p) - dot(n,edge2)
    N = M + n
    print sgn(L(N)), sgn(L(mp))
    if sgn(L(N)) == sgn(L(mp)):
        N = M - n
    i = Vector(1.0,0.0)
    pi2 = 2.0*math.pi
    a = [angle(i,edge1-N) % pi2, angle(i,mp-N) % pi2, angle(i,edge2-N) % pi2]
    if a[0] > a[1] > a[2]:
        a = list(reversed(a))
    return Record(R = R, center = N, phi1 = a[0], phi2 = a[2], phi = a[1])
    

    
