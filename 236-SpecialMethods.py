# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x, y ):
        self.x = x
        self.y = y


    # Representação de String do meu objeto;
    # Quando este método __str__ é definido dentro da classe,
    # Ele vai ser método que o (fallback) irá usar para exibi-lo no meu print.

    def __str__(self):
        return f'{self.x, self.y}'


    # Demonstração para outros programadores de como o meu objeto é montado.
    # Se apenas o __repr__ estiver definido dentro da minha classe; Ele será o método retornado quando eu tentar printar o objeto.

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(x={self.x}) (y={self.y}) '


p1 = Ponto(1, 2)
p2 = Ponto(3, 1)

# Meios de exibição do __repr__ e do __str__ : 

print(p1) # O método __str__ existe na classe, logo ele será chamado para representação do objeto dentro do print.
print(f'{p1!s}') # Posso especificar também para que seja usado o __str__ por meio de formatação [!s]tring.

print(repr(p2)) # Printando o __repr__ usando o método repr()
print(f'{p2!r}') # Printando o __repr__ por meio de formatação [!r]epr.
