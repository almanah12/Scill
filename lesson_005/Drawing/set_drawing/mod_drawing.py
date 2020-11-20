import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
simple_draw.resolution = [1200, 700]


def add_wall():
    for k in range(12):
        for i in range(7):
            if k%2 == 0:
                simple_draw.rectangle(simple_draw.get_point(i*100, k*50), simple_draw.get_point(100 + i*100, 50 + k*50), width=1)
            elif k%2 != 0:
                simple_draw.rectangle(simple_draw.get_point(-50 + i*100, k*50), simple_draw.get_point(50 + i*100, 50 + k*50), width=1)
    simple_draw.pause()


rainbow_colors = (simple_draw.COLOR_RED, simple_draw.COLOR_ORANGE, simple_draw.COLOR_YELLOW, simple_draw.COLOR_GREEN,
                  simple_draw.COLOR_CYAN, simple_draw.COLOR_BLUE, simple_draw.COLOR_PURPLE)


def rainbow(point, step):
    radius = 1200
    for i in range(7):
        radius += step
        simple_draw.circle(center_position=point, radius=radius, color=rainbow_colors[i], width= 5)
    simple_draw.finish_drawing()


def call_rainbow():
    rainbow(point=simple_draw.get_point(100, -250), step=4)
    simple_draw.finish_drawing()


def call_test():
    simple_draw.rectangle(simple_draw.get_point(50, 50), simple_draw.get_point(120, 100))
    simple_draw.pause()


def call_ground():
    simple_draw.rectangle(right_top=simple_draw.get_point(0, 0), left_bottom=simple_draw.get_point(1200, 50), color=simple_draw.COLOR_GREEN, width=0)
    simple_draw.pause()