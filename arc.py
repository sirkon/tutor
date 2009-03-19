# -*- coding: utf-8 -*-

import vector
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
    M = (edge2 + mp)/2.0
    d = math.sqrt(R**2 - norm(M-edge2)**2)
    n = orth(Vector(-b.x,b.y))*d
    L = lambda p: dot(n,p) - dot(n,edge2)
    N = M + n
    if sgn(N) != sgn(edge1):
        N = M - n
    i = Vector(1.0,0.0)
    a1 = angle(i,edge1)
    a2 = angle(i,edge2)
    b1 = angle(
    if a1 > a2:
        a1, a2 = a2, a1
    if a1 < alpha < a2:
        return Record(R = R, center = N, phi1 = a1, phi2 = a2)
    

    
