# totul este un obiect
# un obiect este derivat dintr-o clasă.
# (este instanța unei clase)

# clasă: int
# instanță: int()
# instanță: int("fe", 16)

class Numele:
    ATTR = 15

    def __init__(self):
        print("eu sunt", self)

        self.a = a
        self.b = b

    def mymethod(self):
        print("a-ul meu:", self.a)
        print("b-ul meu:", self.b)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x}, {self.y}"


import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


class Vector:
    def __init__(self, length, angle):
        self.length = length
        self.angle = angle

    def __repr__(self):
        return f"{self.__class__.__name__}(length={self.length}, angle={self.angle})"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            #raise TypeError() # maybe?
            return False
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x or (
            self.x == other.x and self.y < other.y
        )

    def __sub__(self, other):
        length = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        angle = 25 # niște trigonometrie
        return Vector(length, angle)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __str__(self):
        return str(self.as_tuple())

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def as_tuple(self):
        return (self.x, self.y)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            #raise TypeError() # maybe?
            return False
        return self.as_tuple() == other.as_tuple()

    def __lt__(self, other):
        return self.as_tuple() < other.as_tuple()

    def __le__(self, other):
        return self.as_tuple() <= other.as_tuple()


    def __sub__(self, other):
        length = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        angle = 25 # niște trigonometrie
        return Vector(length, angle)



class Point:
    def __init__(self, x, y, default1="ceva", default2="altceva"):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}{repr(self.as_tuple())}"

    def __str__(self):
        return str(self.as_tuple())

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @staticmethod
    def distance_between(p1, p2):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    @property
    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def as_tuple(self):
        return (self.x, self.y)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            #raise TypeError() # maybe?
            return False
        return self.as_tuple() == other.as_tuple()

    def __lt__(self, other):
        return self.as_tuple() < other.as_tuple()

    def __le__(self, other):
        return self.as_tuple() <= other.as_tuple()

    def __sub__(self, other):
        length = Point.distance_between(self, other)
        angle = 25 # niște trigonometrie
        return Vector(length, angle)


class ThreeDPoint(Point):
    def __init__(self, x, y, z, my_default="ceva", **kwargs):
        super().__init__(x, y, **kwargs)
        self.z = z

    def as_tuple(self):
        return (self.x, self.y, self.z)

    @staticmethod
    def distance_between(p1, p2):
        # calculăm Pitagora 3d...
        pass

print(
    ThreeDPoint(1, 2, 3) == ThreeDPoint(1, 2, 3)
)