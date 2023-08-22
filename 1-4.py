class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def distance(self, other_point) -> float:
        """ Расстояние между двумя точками """
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


def triangle_area(triangle_points):
    a= triangle_points[0].distance(triangle_points[1])
    b= triangle_points[0].distance(triangle_points[2])
    c= triangle_points[1].distance(triangle_points[2])
    p = (a + b + c) / 2
    return ((p * (p-a) * (p-b) * (p-c))**0.5)


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три,
# но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]

red_points =[]
green_points = []
# Все точки одного цвета соединены линиями и образуют треугольник
# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод distance()

for point in points:
    if point.color == 'red':
        red_points.append(point)
    else: green_points.append(point)


# Задание-3: вычислите площади треугольников образованных из точек одного цвета(зеленый и красный)
# для вычисления площади можно использовать формулу Герона:
# math.sqrt(p * (p-a) * (p-b) * (p-c)), где p - это полупериметр
# TODO: your code here...
print("Площадь красного треугольника = ", triangle_area(red_points))
print("Площадь зеленого треугольника = ", triangle_area(green_points))
