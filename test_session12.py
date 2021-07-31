from polygon import Polygon
from poly_sequence import Polygons
import math

def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001

    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass

    n = 3
    r = 1
    p = Polygon(n, r)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.count_vertices == n, (f'actual: {p.count_vertices},'
                                   f' expected: {n}')
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
    assert p.circumradius == r, f'actual: {p.circumradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')
    n = 4
    r = 1
    p = Polygon(n, r)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')

    assert math.isclose(p.side_length, math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.side_length},'
                                           f' expected: {math.sqrt(2)}')

    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           f' expected: {4 * math.sqrt(2)}')

    assert math.isclose(p.apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           ' expected: 0.707')
    p = Polygon(6, 2)
    assert math.isclose(p.side_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p = Polygon(12, 3)
    assert math.isclose(p.side_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

    """* Test Polygon Iterator"""
    ps1 = Polygons(7, 5)  # Initializing an Polygon sequence object
    iter_ps = iter(ps1)  # Iterate over polygon sequence object
    try:
        for polygon in iter_ps:
            print(polygon)
        pass
    except ValueError:
        assert False, 'exception received while iterating'

    """check the type of iter_p"""
    r = type(iter_ps)
    assert ((str(r)).find('Polygons.PolygonIterator') != -1)

    """Check the iterable properties  i.e. If something (l for instance above) doesn't get exhausted, 
    and it is iteratable."""
    try:
        for poly in ps1:
            print(poly)

        print("P1 is an unexhaustable source and it an Iterable\n")

        for poly1 in ps1:
            print(poly1)
    except StopIteration:
        assert False, "Error due to exhaust source"


    assert (str(ps1[0:1]) == '[Polygon(n=3, R=5)]'), f'actual: {str(p1[0:1])}'   # check the slicing functionality

    assert (str(ps1[2]) == 'Polygon(n=5, R=5)'), f'actual: {str(p1[2])}'     # check the sequence property

    try:
        iter_ps1 = iter(ps1)
        print(next(iter_ps1))
        print(next(iter_ps1))
        print(next(iter_ps1))
        print(next(iter_ps1))
        print(next(iter_ps1))
        print(next(iter_ps1))
    except StopIteration:  # Check if stopIteration be called after it reaches its limit in an iteration
        assert True, "hits exception"
    
    ps1 = Polygons(7, 5)

    assert (('__iter__' in dir(ps1)) == True), "__iter__ doesn't exist in polygon object"
    assert (sorted(ps1))
