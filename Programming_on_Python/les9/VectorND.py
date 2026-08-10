from numbers import Real
from typing import Iterable, Iterator, Union
from array import array


class VectorND:
    _component: array[Real]

    def __init__(self, component: Iterable) -> None:
        try:
            iter(component)
        except TypeError:
            raise TypeError("Vector's component must be iterable object")
        if bool(component) == 0:
            raise ValueError("Vector's component can't be empty")
        self._component = array("f", component)

    def __repr__(self) -> str:
        s=", ".join(list(map(str,self._component)))[:10]+"..."
        return f"V({s})"
    
    def __iter__(self) -> Iterator:
        return iter(self._component)

    def __len__(self) -> int:
        return len(self._component)
    
    def __contains__(self, key: int) -> bool:
        if not isinstance(key,int):
            raise TypeError("Checking through 'in' must be only for integer numbers")
        if key <= 1 or key >= len(self):
            raise ValueError("Key must be among 1 and length of Vector")
        return key < len(self)
    
    def __getitem__(self, key: int) -> Real:
        if not isinstance(key,int):
            raise TypeError("Getting element through '[]' must be only for integer numbers")
        if key <= 1 or key >= len(self):
            raise ValueError("Key must be among 1 and length of Vector")
        return self._component[key-1]
    
    def alignment(self, another: "VectorND") -> None:
        #для повышения читабельности решил добавить эту функцию выравнивания векторов
        #выравниванию подвергаются оба вектора. Михаил Евграфов функцию увидел, посоветовал разобраться с zip_longest
        #IN PROGRESS: разобраться с zip_longest
        
        if len(self) < len(another):
            while len(self) != len(another):
                self._component.append(0)
        else:
            while len(self) != len(another):
                another._component.append(0)
    
    def __eq__(self, another: "VectorND") -> bool:
        if not isinstance(another, VectorND):
            raise TypeError("Comparison can be only among two vectors")
        
        self.alignment(another)
        
        for i in range(len(self)):
            if self._component[i] != another._component[i]:
                return False
        return True
    
    def __ne__(self, another: "VectorND") -> bool:
        if not isinstance(another, VectorND):
            raise TypeError("Comparison can be only among two vectors")
        
        self.alignment(another)

        for i in range(len(self)):
            if self._component[i] != another._component[i]:
                return True
        return False
            
    def __lt__(self, another:"VectorND") -> bool:
        if not isinstance(another, VectorND):
            raise TypeError("Comparison can be only among two vectors")
        
        self.alignment(another)
        
        for i in range(len(self)):
            if self._component[i] == another._component[i]:
                continue
            if self._component[i] > another._component[i]:
                return False
            if self._component[i] < another._component[i]:
                return True
        return (self._component[-1] < another._component[-1])


    def __le__(self, another:"VectorND") -> bool:
        if not isinstance(another, VectorND):
            raise TypeError("Comparison can be only among two vectors")
        
        self.alignment(another)

        for i in range(len(self)):
            if self._component[i] == another._component[i]:
                continue
            if self._component[i] > another._component[i]:
                return False
            if self._component[i] < another._component[i]:
                return True
        return True

    def __rt__(self, another:"VectorND") -> bool:
        if not isinstance(another, VectorND):
            raise TypeError("Comparison can be only among two vectors")

        self.alignment(another)

        for i in range(len(self)):
            if self._component[i] == another._component[i]:
                continue
            if self._component[i] < another._component[i]:
                return False
            if self._component[i] > another._component[i]:
                return True
        return (self._component[-1] > another._component[-1])


    def __re__(self, another:"VectorND") -> bool:
        if not isinstance(another, VectorND):
            raise TypeError("Comparison can be only among two vectors")

        self.alignment(another)

        for i in range(len(self)):
            if self._component[i] == another._component[i]:
                continue
            if self._component[i] > another._component[i]:
                return True
            if self._component[i] < another._component[i]:
                return False
            
        return True

    def __abs__(self) -> Real:
        vectorlen = 0
        for elem in self._component:
            vectorlen += elem * elem
        return vectorlen ** 0.5
    
    def __bool__(self) -> bool:
        return abs(self) != 0

    def __mul__(self, another: Real) -> "VectorND":
        if not isinstance(another, Real):
            raise NotImplemented
        newvec = VectorND(range(len(self)))
        for i in range(len(self)):
            newvec._component[i]=another.real*self._component[i]
        return newvec

    def __rmul__(self, another: Real) -> "VectorND":
        if not isinstance(another, Real):
            raise TypeError("You can multipy vector only with Real numbers")
        newvec = VectorND(range(len(self)))
        for i in range(len(self)):
            newvec._component[i] = another.real*self._component[i]
        return newvec

    def __truediv__(self, another: Real) -> "VectorND":
        if not isinstance(another, Real):
            raise ValueError("You can only divide a vector by a real number")
        newvec = VectorND(range(len(self)))
        for i in range(len(self)):
            newvec._component[i] = 1 / another.real * self._component[i]
        return newvec 

    def __add__(self, another: Union["VectorND", Real]) -> "VectorND":
        if not isinstance(another, (VectorND,Real)):
            return NotImplemented
        
        if isinstance(another, Real):
            newvec = VectorND(range(len(self)))
            for i in range(len(self)):
                newvec._component[i] = self._component[i] + another.real
            return newvec
        else:
            self.alignment(another)
            newvec = VectorND(range(len(self)))
            for i in range(len(self)):
                newvec._component[i] = self._component[i] + another._component[i]
            return newvec
        


    def __radd__(self, another: Union["VectorND", Real]) -> "VectorND":
        if not isinstance(another, (Real, VectorND)):
            raise TypeError("Addition can be only Vec+Real, Real+Vec or Vec+Vec")
        if isinstance(another,Real):
            newvec = VectorND(range(len(self)))
            for i in range(len(self)):
                newvec._component[i] = self._component[i] + another.real
            return newvec
        else:
            self.alignment(another)
            newvec = VectorND(range(len(self)))
            for i in range(len(self)):
                newvec._component[i] = self._component[i] + another._component[i]
            return newvec
        
        
    def __sub__(self, another: Union["VectorND", Real]) -> "VectorND":
        if not isinstance(another, (Real,VectorND)):
            raise NotImplemented
        if isinstance(another,Real):
            newvec = VectorND(range(len(self)))
            for i in range(len(self)):
                newvec._component[i] = self._component[i] - another.real
            return newvec
        else:
            self.alignment(another)
            newvec = VectorND(range(len(self)))
            for i in range(len(self)):
                newvec._component[i] = self._component[i] - another._component[i]
            return newvec
        
    def __rsub__(self, another: Union["VectorND", Real]) -> "VectorND":
        if not isinstance(another, (Real, VectorND)):
            raise TypeError("Substraction can be only Vec-Real, Real-Vec or Vec-Vec")
        if isinstance(another,Real):
            newvec = VectorND(range(len(self)))
            for i in range(len(self)):
                newvec._component[i] = another.real -  self._component[i]
            return newvec
        else:
            self.alignment(another)
            newvec = VectorND(range(len(self)))
            for i in range(len(self)):
                newvec._component[i] = another._component[i] - self._component[i]
            return newvec 
        
    def __neg__(self) -> "VectorND":
        newvec = VectorND(range(len(self)))
        for i in range(len(self)):
            newvec._component[i] = -self._component[i]
        return newvec
    
    def __int__(self) -> int:
        return int(abs(self))

    def __float__(self) -> float:
        return abs(self)
    
    def __matmul__(self, another: "VectorND") -> Real:
        if not isinstance(another, VectorND):
            raise TypeError("Scalar prouct can be only among vec@vec")
        scalarproduct = 0
        self.alignment(another)
        for i in range(len(self)):
            scalarproduct+= self._component[i]*another._component[i]
        return scalarproduct

