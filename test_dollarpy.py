from dollarpy import Recognizer, Template, Point


def test_recognition_successful():
    tmpl = Template('X', [
        Point(0, 0, 1),
        Point(1, 1, 1),
        Point(0, 1, 2),
        Point(1, 0, 2)
    ])
    recognizer = Recognizer([tmpl])
    result = recognizer.recognize([
        Point(30, 146, 1),
        Point(106, 222, 1),
        Point(30, 225, 2),
        Point(106, 146, 2)
    ])
    assert result[0] == 'X'


def test_recognition_failed():
    tmpl = Template('X', [
        Point(0, 0, 1),
        Point(1, 1, 1),
        Point(0, 1, 2),
        Point(1, 0, 2)
    ])
    recognizer = Recognizer([tmpl])
    result = recognizer.recognize([
        Point(30, 146, 1),
        Point(306, 222, 1),
    ])
    assert result[0] is None
