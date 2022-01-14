# Check if two rectangles have intersection and return it

# You have to think dimensions independently. X1 shouldnt fall less
# than X2 + width and so on for all and then to find intersection
# min max the co-ordinates and add remove verice magnitude from width/height

# O(1)
# O(1)


class Rectangle:
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def intersect_rectangle(r1, r2):
    def is_intersect(r1, r2):
        x_overlap = r1.x + r1.width >= r2.x and r2.x + r2.width <= r1.x
        y_overlap = r1.y + r1.height >= r2.y and r2.y + r2.height <= r1.y
        return x_overlap and y_overlap

    if not is_intersect(r1, r2):
        return None
    return Rectangle(
        max(r1.x, r2.x),
        max(r1.y, r2.y),
        min(r1.x + r1.width, r2.x + r2.width - max(r1.x, r2.x)),
        min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y),
    )
