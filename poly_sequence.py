"""**Objective 2**:
    Implement a Custom Polygon sequence type:

    1. Where initializer takes in:
        * number of vertices for largest polygon in the sequence
        * common circumradius for all polygons
        * that can provide these properties:
        * max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
     2. that has these functionalities:
        * functions as a sequence type (__getitem__)
        * supports the len() function (__len__)
        * has a proper representation (__repr__)
"""
from polygon import Polygon

class Polygons:
    """
    Custom polygon sequence containing polygons where maximum number of edges in a polygon is given
    by m  and circumradius (R) for all polygons is is given by circumradius and is same for all polygons"
    """
    def __init__(self, m, r):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._r = r
        self._efficiency = None

    def __len__(self):
        """ This function gives the length of the Polygon Sequence object """
        return self._m - 2

    def __repr__(self):
        """ This function gives the details of the Polygon Sequence object"""
        return f'Polygons(m={self._m}, R={self._r})'

    def __getitem__(self, s):
        """ This function returns the element of a Polygon sequence or a list of
        element of Polygon sequence"""
        if isinstance(s, int):
            if s < 0:
                s = self._m - 2 + s
            if s < 0 or s >= (self._m - 2):
                raise IndexError
            else:
                return self._polygon(s + 3)
        else:
            start, stop, step = s.indices(self._m-2)
            rng = range(start, stop, step)
            return [self._polygon(i+3) for i in rng]

    def __iter__(self):
        """Iterable Function--> This function returns the iterator for the 
        Polygon object"""
        print("Calling Polygon instance __iter__")
        return self.PolygonIterator(self._m - 2, self._r)

    def _polygon(self, num_edges):
        """Function returning a polygon of particular num of edges and \
        circumradius along with all the properties"""
        return Polygon(num_edges, self._r)

    @property
    def max_efficiency_polygon(self):
        """ This function returns the maximum efficiency polygon.
        Here, a maximum efficiency polygon is one that has the highest area to
        perimeter ratio."""
        if self._efficiency is None:
            self._efficiency = sorted(self._polygons,
                                      key=lambda p: p.area/p.perimeter,
                                      reverse=True)[-1]
        return self._efficiency

    class PolygonIterator:
        """This is an Iterator for the polygons class"""
        def __init__(self, max_edges, radius):
            """Function initializing the polygon Iterator and
            index. Index is used to return the next element in the polygon
            sequence when used as a iterator"""
            print("Calling PolygonIterator __init__")
            self._r = radius
            self._index = 0
            self._max_edges = max_edges

        def __iter__(self):
            """ PolygonIterator instance returning self"""
            print("Calling PolygonIterator instance __iter__")
            return self

        def __next__(self):
            """PolygonIterator next function which return the next element in 
            Polygons sequence if current index is less than length of Polygons obj"""
            print("Calling PolygonIterator __next__")
            if self._index >= self._max_edges:
                raise StopIteration
            else:
                index = self._index
                item = Polygon(index + 3, self._r)
                self._index += 1
                print(f'here: {self._index}')
                return item
