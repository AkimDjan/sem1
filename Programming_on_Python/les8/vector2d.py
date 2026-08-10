from math import acos
from numbers import Real
from typing import Union

class Vector2D:
    _abscissa: Real
    _ordinate: Real

    #можно было и через @dataclass, но я уже пошел таким путем)

    def __init__(self, a:Real=0.0 , o:Real=0.0) -> None:
        self._abscissa=float(a)
        self._ordinate=float(o)

    @property
    def abscissa(self) -> Real:
        return self._abscissa
    
    @property
    def ordinate(self) -> Real:
        return self._ordinate
    
    def __repr__(self) -> str:
        return f"Vector2D(abscissa={self._abscissa}, ordinate={self._ordinate})"

    def __eq__(self, other: "Vector2D") -> bool:
        return (self.abscissa == other.abscissa) and (self.ordinate == other.ordinate)
    
    def __ne__(self, other: "Vector2D") -> bool:
        return (self.abscissa!=other.abscissa) or (self.ordinate != other.ordinate)

    def __lt__(self, other: "Vector2D") -> bool:
        return (self.abscissa < other.abscissa) or ((self.abscissa == other.abscissa) and (self.ordinate < other.ordinate))
    
    def __le__(self, other: "Vector2D") -> bool:
        if self.abscissa!=other.abscissa:
            return self.abscissa <= other.abscissa
        else:
            return self.ordinate <= other.ordinate
    
    def __rt__(self,other: "Vector2D") -> bool:
        return (self.abscissa > other.abscissa) or ((self.abscissa == other.abscissa) and (self.ordinate > other.ordinate))
    
    def __re__(self, other: "Vector2D") -> bool:
        if self.abscissa!=other.abscissa:
            return self.abscissa >= other.abscissa
        else:
            return self.ordinate >= other.ordinate
        
    def __abs__(self) -> Real:
        return (self.abscissa**2+self.ordinate**2)**0.5
    
    def __bool__(self) -> bool:
        return ((self.abscissa**2+self.ordinate**2)**0.5)!=0

    def __mul__(self, other:Union[Real,"Vector2D"]) -> "Vector2D":
        if not isinstance(other, (Real, Vector2D)):
            raise NotImplemented
        return Vector2D(self.abscissa*other, self.ordinate*other)
    
    def __rmul__(self, other:Union[Real,"Vector2D"]) -> "Vector2D":
        if not isinstance(other, (Real, Vector2D)):
            raise ValueError("we can only multipy a vector by a real number")
        return Vector2D(self.abscissa*other, self.ordinate*other)
    
    def __truediv__(self, other:Real) -> "Vector2D":
        if not isinstance(other, Real):
            raise ValueError("we can only divide a vector by a real number")
        return Vector2D(self.abscissa*1/other.real, self.ordinate*1/other.real)
    
    def __add__(self, other:Union["Vector2D", Real]) -> "Vector2D":
        if not isinstance(other, (Vector2D,Real)):
            return NotImplemented
        if isinstance(other,Real):
            return Vector2D(self.abscissa+other.real,self.ordinate+other.real)
        else:
            return Vector2D(self.abscissa+other.abscissa,self.ordinate+other.ordinate)
        
    def __radd__(self, other:Union["Vector2D", Real]) -> "Vector2D":
        if isinstance(other,Real):
            return Vector2D(self.abscissa+other.real,self.ordinate+other.real)
        else:
            return Vector2D(self.abscissa+other.abscissa,self.ordinate+other.ordinate)

    def conjugate(self) -> "Vector2D":
        return Vector2D(self._abscissa,-self._ordinate)

    def __sub__(self, other:Union["Vector2D", Real]) -> "Vector2D":
        if not isinstance(other, (Vector2D, Real)):
            return NotImplemented
        if isinstance(other,Real):
            return Vector2D(self.abscissa-other,self.ordinate-other)
        else:
            return Vector2D(self.abscissa-other.abscissa,self.ordinate-other.ordinate)
        
    def __rsub__(self, other:"Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.abscissa-other.abscissa,self.ordinate-other.ordinate)
    
    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.abscissa,-self.ordinate)
    
    def __matmul__(self, other: "Vector2D") -> Real:
        return self.abscissa*other.abscissa+self.ordinate*other.ordinate

    def __int__(self) -> int:
        return int((self.abscissa**2+self.ordinate**2)**0.5)
    
    def __float__(self) -> float:
        return float((self.abscissa**2+self.ordinate**2)**0.5)
    
    def __complex__(self) -> complex:
        return complex(self.abscissa+1j*self.ordinate)

    def get_angle(self,other:"Vector2D") -> Real:
        if (self.abscissa==0 and self.ordinate==0) or (other.abscissa==0 and other.ordinate==0):
            raise ValueError("You cant get angle from null vector")
        return acos((self.abscissa*other.abscissa+self.ordinate*other.ordinate)/ \
                    (((self.abscissa**2+self.ordinate**2)**0.5)*((other.abscissa**2+other.ordinate**2)**0.5)))
    
print(Vector2D.get_angle(Vector2D(1,0),Vector2D(0,1)))