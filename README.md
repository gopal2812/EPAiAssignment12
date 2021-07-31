# EPAiAssignment12
# Project: Description
The starting point for this project is the Polygon class and the Polygons sequence type we created in the previous project.

The code for these classes along with the unit tests for the Polygon class are below if you want to use those as your starting point. But use whatever you came up with in the last project.

We have two goals:

### Goal 1
Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").

### Goal 2
Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

![image](https://user-images.githubusercontent.com/39087216/127747450-1c3d3e16-aadb-4fd4-b415-c81b49e11522.png)

### Polygon Class

* A regular strictly convex polygon is a polygon that has the following characteristics:
    * All interior angles are less than 180
    * All sides have equal length

* For a regular strictly convex polygon with vertices n and circumradius r:
    * interiorAngle = (n−2) * (180/n)
    * edgeLength, s = 2 * R * sin(π/n) 
    * apothem, a = R * cos(π/n)
    * area = (1/2) * n * a
    * perimeter = n * s
 
* Create a Polygon Class:   
     1. Where initializer takes in:
        * number of edges/vertices
        * circumradius
      2. That can provide these properties:
          * edges
          * vertices
          * interior angle
          * edge length
          * apothem
          * area
          * perimeter
      3. That has these functionalities:
          * a proper __repr__ function
          * implements equality (==) based on # vertices and circumradius (__eq__)
          * implements > based on number of vertices only (__gt__)
          
 * Create a PolygonIterator  Where initializer takes in:
    * number of vertices for largest polygon in the sequence
    * common circumradius for all polygons
    * that can provide these properties:
    * max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
   that has these functionalities:
    * functions as a sequence type (__getitem__)
    * supports the len() function (__len__)
    * has a proper representation (__repr__)
    * has a __iterable__ module (__iter__) which has an polygonIterator and the elements 
      in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.
   
```
   Polygon class to create polygons which are regular strictly convex.
 |  Regular strict polygons have two properties:
 |  1- All interior angles are less than 180.
 |  2- All sides have equal length
 |  
 |  Methods defined here:
 |  
 |  __eq__(self, other)
 |      Provides ability to compare two objects for euality (==).
 |  
 |  __gt__(self, other)
 |      Provide ability to compare two objects for greater than '>' test.
 |  
 |  __init__(self, count_edges: int, circumradius: float) -> None
 |      Initialize the edges, circumradius, interiorAngle, edgeLength ,
 |      apothem, area, perimeter.
 |  
 |  __repr__(self)
 |      This function gives the details of the Polygon Sequence object
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  apothem
 |      apothem of the polygon
 |  
 |  area
 |      area of the polygon
 |  
 |  circumradius
 |      circumradius of the polygon
 |  
 |  count_edges
 |      Number of edges in the polygon
 |  
 |  count_vertices
 |      Number of vertices in the polygon
 |  
 |  interior_angle
 |      Interior angle of the polygon
 |  
 |  perimeter
 |      perimeter of the polygon
 |  
 |  side_length
 |      side length of the polygon
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
 Help on class Polygons in module __main__:

class Polygons(builtins.object)
 |  Polygons(m, r)
 |  
 |  Custom polygon sequence containing polygons where maximum number of edges in a polygon is given
 |  by m  and circumradius (R) for all polygons is is given by circumradius and is same for all polygons"
 |  
 |  Methods defined here:
 |  
 |  __getitem__(self, s)
 |      This function returns the element of a Polygon sequence or a list of
 |      element of Polygon sequence
 |  
 |  __init__(self, m, r)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self)
 |      Iterable Function--> This function returns the iterator for the 
 |      Polygon object
 |  
 |  __len__(self)
 |      This function gives the length of the Polygon Sequence object
 |  
 |  __repr__(self)
 |      This function gives the details of the Polygon Sequence object
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  max_efficiency_polygon
 |      This function returns the maximum efficiency polygon.
 |      Here, a maximum efficiency polygon is one that has the highest area to
 |      perimeter ratio.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  PolygonIterator = <class '__main__.Polygons.PolygonIterator'>
 |      This is an Iterator for the polygons class

class PolygonIterator(builtins.object)
 |  PolygonIterator(max_edges, radius)
 |  
 |  This is an Iterator for the polygons class
 |  
 |  Methods defined here:
 |  
 |  __init__(self, max_edges, radius)
 |      Function initializing the polygon Iterator and
 |      index. Index is used to return the next element in the polygon
 |      sequence when used as a iterator
 |  
 |  __iter__(self)
 |      PolygonIterator instance returning self
 |  
 |  __next__(self)
 |      PolygonIterator next function which return the next element in 
 |      Polygons sequence if current index is less than length of Polygons obj
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
```
