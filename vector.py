#!/usr/bin/env python
# 
# a python Vector class
# A. Pletzer 5 Jan 00/11 April 2002
#
import math

"""
A list based Vector class that supports elementwise mathematical operations

In this version, the Vector call inherits from list; this 
requires Python 2.2 or later.
"""

class Vector(list):
    """
    A list based Vector class
    """
    # no c'tor

    def __init__ (self, *a):
        if len (a) == 1:
            super(Vector, self).__init__(a[0])
        else:
            super(Vector, self).__init__(a)
            
    def __getslice__(self, i, j):
        try:
            # use the list __getslice__ method and convert
            # result to Vector
            return Vector(super(Vector, self).__getslice__(i,j))
        except:
            raise TypeError, 'Vector::FAILURE in __getslice__'
        
    def __add__(self, other):
        return Vector(map(lambda x,y: x+y, self, other))

    def __neg__(self):
        return Vector(map(lambda x: -x, self))
    
    def __sub__(self, other):
        return Vector(map(lambda x,y: x-y, self, other))

    def __mul__(self, other):
        """
        Element by element multiplication
        """
        try:
            return Vector(map(lambda x,y: x*y, self,other))
        except:
            # other is a const
            return Vector(map(lambda x: x*other, self))


    def __rmul__(self, other):
        return (self*other)


    def __div__(self, other):
        """
        Element by element division.
        """
        try:
            return Vector(map(lambda x,y: x/y, self, other))
        except:
            return Vector(map(lambda x: x/other, self))

    def __rdiv__(self, other):
        """
        The same as __div__
        """
        try:
            return Vector(map(lambda x,y: x/y, other, self))
        except:
            # other is a const
            return Vector(map(lambda x: other/x, self))

        def size(self): return len(self)

    def conjugate(self):
        return Vector(map(lambda x: x.conjugate(), self))

    def ReIm(self):
        """
        Return the real and imaginary parts
        """
        return [
            Vector(map(lambda x: x.real, self)),
            Vector(map(lambda x: x.imag, self)),
            ]
    
    def AbsArg(self):
        """
        Return modulus and phase parts
        """
        return [
            Vector(map(lambda x: abs(x), self)),
            Vector(map(lambda x: math.atan2(x.imag,x.real), self)),
            ]

    x = property (lambda c: c[0], (lambda c,x: c.__setitem__(0,x)))
    y = property (lambda c: c[1], (lambda c,x: c.__setitem__(1,x)))
    z = property (lambda c: c[2], (lambda c,x: c.__setitem__(2,x)))



###############################################################################


def isVector(x):
    """
    Determines if the argument is a Vector class object.
    """
    return hasattr(x,'__class__') and x.__class__ is Vector

def zeros(n):
    """
    Returns a zero Vector of length n.
    """
    return Vector(map(lambda x: 0., range(n)))

def ones(n):
    """
    Returns a Vector of length n with all ones.
    """
    return Vector(map(lambda x: 1., range(n)))

def random(n, lmin=0.0, lmax=1.0):
    """
    Returns a random Vector of length n.
    """
    import whrandom
    new = Vector([])
    gen = whrandom.whrandom()
    dl = lmax-lmin
    return Vector(map(lambda x: dl*gen.random(),
               range(n)))
    
def dot(a, b):
    """
    dot product of two Vectors.
    """
    try:
        return reduce(lambda x, y: x+y, a*b, 0.)
    except:
        raise TypeError, 'Vector::FAILURE in dot'
    

def norm(a):
    """
    Computes the norm of Vector a.
    """
    try:
        return math.sqrt(abs(dot(a,a)))
    except:
        raise TypeError, 'Vector::FAILURE in norm'

def orth(a):
    try:
        return a/norm(a)
    except:
        raise TypeError, 'Vector::FAILURE in ort'


def det(*vectors):
    lengths = set (map(len,vectors))
    if len(lengths) != 1:
        raise TypeError, 'Vector::FAILURE in det'
    if len(vectors) != len(vectors[0]):
        raise TypeError, 'Vectors:FAILURE in det'
    # Don't want to implement vector operations - only 2x2 is provided now
    if len (vectors) != 2:
        raise TypeError, 'Vectors::FAILURE det not implemented for this dimension'
    a,b = vectors
    return a[0]*b[1] - a[1]*b[0]
    
def angle(a,b):
    d = det(a,b)
    d = -1.0 if d < 0.0 else 1.0
    return d*math.acos(dot(a,b)/norm(a)/norm(b))
    
