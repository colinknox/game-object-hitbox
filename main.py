class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_left_x(self):
        return min(self.x1, self.x2)
    
    def get_right_x(self):
        return max(self.x1, self.x2)
    
    def get_bottom_y(self):
        return min(self.y1, self.y2)

    def get_top_y(self):
        return max(self.y1, self.y2)
    
    def overlaps(self, other):
        if self.get_left_x() <= other.get_right_x() and self.get_right_x() >= other.get_left_x() and self.get_bottom_y() <= other.get_top_y() and self.get_top_y() >= other.get_bottom_y():
            return True
        else:
            return False 

class GameObject:
    def __init__(self, name, center_x, center_y, width, height):
        self.name = name
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.__range_width = self.width / 2
        self.__range_height = self.height / 2
        self.__hitbox = Rectangle(self.center_x - self.__range_width, self.center_y - self.__range_height, self.center_x + self.__range_width, self.center_y + self.__range_height)

    def get_hitbox(self):
        return self.__hitbox

    def collides_with(self, other):
        return self.__hitbox.overlaps(other.get_hitbox())
