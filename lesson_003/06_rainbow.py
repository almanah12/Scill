# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
def rainbow(point, step):
    radius = 5
    for i in range(7):
        radius += step
        sd.circle(center_position=point, radius=radius, color=rainbow_colors[i], width= 5)

poi = sd.get_point(50, 50)
rainbow(point=poi, step=10)
sd.resolution = (1200, 600)
star_pos = sd.get_point(50, 50)
end_pos = sd.get_point(350, 450)
sd.circle(star_pos, 180, rainbow_colors[1])
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
sd.pause()
