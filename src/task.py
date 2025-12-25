def circle_area(r: int) -> float:
    """Функция вычисляет площадь круга по радиусу"""
    PI = 3.14
    circleArea = PI * r**2
    return circleArea


def format_description(r, area):
    """Получение строки с результатом"""
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_info(r: float):
    """Вывод результата на экран"""
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_info(radius)
