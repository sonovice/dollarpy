import math


class Point:
    def __init__(self, x, y, stroke_id=None):
        self.x = x
        self.y = y
        self.stroke_id = stroke_id

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + '), stroke ' + str(self.stroke_id)


class Template(list):
    def __init__(self, name, points):
        self.name = name
        super(Template, self).__init__(points)


class Recognizer:
    def __init__(self, templates):
        self.templates = templates

    def recognize(self, points, n=32):
        """Recognizer main function.

        Match points against a set of templates by employing the Nearest-Neighbor classification rule.

        Parameters
        ----------
        points:
            List of Point objects.
        n:
            Number of resampled points per gesture.

        Returns
        -------
        gesture:
            Name of the recognized gesture.
        score:
            Normalized match score in [0..1] with 1 denoting perfect match.
        """
        result = None
        points = self._normalize(points, n)
        score = float("inf")

        for template in self.templates:
            template = self._normalize(template, n)
            d = self._greedy_cloud_match(points, template, n)
            if score > d:
                score = d
                result = template
        score = max((2 - score) / 2, 0)
        if result is None or score == 0:
            return None, score
        return result.name, score

    def _greedy_cloud_match(self, points, template, n):
        epsilon = 0.5  # [0..1] controls the number of tested alignments
        step = int(math.floor(n ** (1 - epsilon)))
        minimum = float("inf")

        for i in range(0, n, step):
            d_1 = self._cloud_distance(points, template, n, i)
            d_2 = self._cloud_distance(template, points, n, i)
            minimum = min(minimum, d_1, d_2)
        return minimum

    def _cloud_distance(self, points, template, n, start):
        matched = [False] * n
        sum_distance = 0
        i = start

        while True:
            minimum = float("inf")
            index = None
            for j in [x for x, b in enumerate(matched) if not b]:
                d = self._euclidean_distance(points[i], template[j])
                if d < minimum:
                    minimum = d
                    index = j
            matched[index] = True
            weight = 1 - ((i - start + n) % n) / n
            sum_distance += weight * minimum
            i = (i + 1) % n
            if i == start:
                break
        return sum_distance

    def _euclidean_distance(self, point_1, point_2):
        return math.hypot(point_1.x - point_2.x,
                          point_1.y - point_2.y)

    def _normalize(self, points, n):
        points = self._resample(points, n)
        points = self._scale(points)
        points = self._translate_to_origin(points, n)
        return points

    def _resample(self, points, n):
        I = self._path_length(points) / (n - 1)
        D = 0
        if isinstance(points, Template):
            new_points = Template(points.name, [points[0]])
        else:
            new_points = [points[0]]

        i = 1
        while True:
            if points[i].stroke_id == points[i - 1].stroke_id:
                d = self._euclidean_distance(points[i - 1], points[i])
                if D + d >= I:
                    q = Point(points[i - 1].x + ((I - D) / d) * (points[i].x - points[i - 1].x),
                              points[i - 1].y + ((I - D) / d) * (points[i].y - points[i - 1].y))
                    q.stroke_id = points[i].stroke_id
                    new_points.append(q)
                    points.insert(i, q)
                    D = 0
                else:
                    D += d
            i += 1
            if i == len(points):
                break
        if len(new_points) == n - 1:
            p = points[-1]
            new_points.append(Point(p.x, p.y, p.stroke_id))
        return new_points

    def _path_length(self, points):
        d = 0

        for i in range(1, len(points)):
            if points[i].stroke_id == points[i - 1].stroke_id:
                d += self._euclidean_distance(points[i - 1], points[i])
        return d

    def _scale(self, points):
        x_min = float("inf")
        x_max = 0
        y_min = float("inf")
        y_max = 0

        if isinstance(points, Template):
            new_points = Template(points.name, [])
        else:
            new_points = []

        for p in points:
            x_min = min(x_min, p.x)
            x_max = max(x_max, p.x)
            y_min = min(y_min, p.y)
            y_max = max(y_max, p.y)
        scale = max(x_max - x_min, y_max - y_min)

        for p in points:
            q = Point((p.x - x_min) / scale,
                      (p.y - y_min) / scale,
                      p.stroke_id)
            new_points.append(q)
        return new_points

    def _translate_to_origin(self, points, n):
        if isinstance(points, Template):
            new_points = Template(points.name, [])
        else:
            new_points = []

        x = 0
        y = 0
        for p in points:
            x += p.x
            y += p.y
        x /= n
        y /= n

        for p in points:
            q = Point((p.x - x),
                      (p.y - y),
                      p.stroke_id)
            new_points.append(q)
        return new_points
