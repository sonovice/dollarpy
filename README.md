# dollarpy

*dollarpy* is a python implementation of the [$P Point-Cloud Recognizer](http://depts.washington.edu/aimgroup/proj/dollar/pdollar.html).

[![License](https://img.shields.io/pypi/l/dollarpy.svg)](https://www.gnu.org/licenses/lgpl.html)

[![Python Compatibility](https://img.shields.io/pypi/pyversions/dollarpy.svg)](https://pypi.python.org/pypi/dollarpy/) [![PyPI Version](https://img.shields.io/pypi/v/dollarpy.svg)](https://pypi.python.org/pypi/dollarpy/) [![Format](https://img.shields.io/pypi/format/dollarpy.svg)](https://pypi.python.org/pypi/dollarpy/)

[![Build Status](https://img.shields.io/travis/sonovice/dollarpy.svg)](https://travis-ci.org/sonovice/dollarpy) [![Coverage Status](https://img.shields.io/codecov/c/github/sonovice/dollarpy.svg)](https://codecov.io/gh/sonovice/dollarpy)

From the website:

> The $P Point-Cloud Recognizer is a 2-D gesture recognizer designed for rapid prototyping of gesture-based user interfaces. In machine learning terms, $P is an instance-based nearest-neighbor classifier with a Euclidean scoring function, i.e., a geometric template matcher.
> 
> $P is the latest in the dollar family of recognizers that includes $1 for unistrokes and $N for multistrokes. Although about half of $P’s code is from $1, unlike both $1 and $N, $P does not represent gestures as ordered series of points (i.e., strokes), but as unordered point-clouds. By representing gestures as point-clouds, $P can handle both unistrokes and multistrokes equivalently and without the combinatoric overhead of $N. When comparing two point-clouds, $P solves the classic assignment problem between two bipartite graphs using an approximation of the Hungarian algorithm.

Vatavu, R. D., Anthony, L., & Wobbrock, J. O., ["Gestures as Point Clouds: A $P Recognizer for User Interface Prototypes"](http://faculty.washington.edu/wobbrock/pubs/icmi-12.pdf), in: *Proceedings of the 14th ACM International Conference on Multimodal Interaction (ICMI)*, Santa Monica, LA, USA, 2012, pp. 273-280.

## Installation
*dollarpy* can be installed using pip:

```
pip install dollarpy
```

## Usage
*dollarpy* is used in 3 steps:

``` python
from dollarpy import Recognizer, Template, Point

# Define 'Template' gestures, each consisting of a name and a list of 'Point' elements.
# These 'Point' elements have 'x' and 'y' coordinates and optionally the stroke index a point belongs to.
tmpl_1 = Template('X', [
    Point(0, 0, 1),
    Point(1, 1, 1),
    Point(0, 1, 2),
    Point(1, 0, 2)])
tmpl_2 = Template('line', [
    Point(0, 0),
    Point(1, 0)])

# Create a 'Recognizer' object and pass the created 'Template' objects as a list.
recognizer = Recognizer([tmpl_1, tmpl_2])

# Call 'recognize(...)' to match a list of 'Point' elements to the previously defined templates.
result = recognizer.recognize([
    Point( 31, 141, 1),
    Point(109, 222, 1),
    Point( 22, 219, 2),
    Point(113, 146, 2)])
print(result)  # Output: ('X', 0.733770116545184)
```
