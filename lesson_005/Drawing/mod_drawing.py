import simple_draw
import random

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
simple_draw.resolution = [1100, 700]
rainbow_colors = (simple_draw.COLOR_RED, simple_draw.COLOR_ORANGE, simple_draw.COLOR_YELLOW, simple_draw.COLOR_GREEN,
                  simple_draw.COLOR_CYAN, simple_draw.COLOR_BLUE, simple_draw.COLOR_PURPLE)


def add_wall():
    """
    wall
    """
    left_x, left_y = 200, 50
    length_brick, hight_brick = 60, 30
    right_x = left_x + length_brick
    right_y = left_y + hight_brick
    row = 5
    column = 8
    for k in range(column):
        for i in range(row):
            if k % 2 == 0:
                simple_draw.rectangle(simple_draw.get_point(left_x + i * length_brick, left_y + k * hight_brick),
                                      simple_draw.get_point(right_x + i * length_brick, right_y + k * hight_brick),
                                      width=1)
            elif k % 2 != 0:
                if i == 0 or i == row - 1:
                    simple_draw.rectangle(simple_draw.get_point(left_x + i * length_brick, left_y + k * hight_brick),
                                          simple_draw.get_point(right_x, right_y + k * hight_brick),
                                          simple_draw.COLOR_DARK_ORANGE, width=1)
                else:
                    simple_draw.rectangle(
                        simple_draw.get_point((left_x - length_brick / 2) + i * length_brick, left_y + k * hight_brick),
                        simple_draw.get_point((left_x + length_brick / 2) + i * length_brick,
                                              right_y + k * hight_brick), width=1)

    simple_draw.pause()


def rainbow(point, step):
    """
    rainbow
    """
    radius = 1200
    for i in range(7):
        radius += step
        simple_draw.circle(center_position=point, radius=radius, color=rainbow_colors[i], width= 5)
    simple_draw.finish_drawing()


def call_rainbow():
    rainbow(point=simple_draw.get_point(100, -250), step=4)
    simple_draw.finish_drawing()


def call_ground():
    simple_draw.rectangle(left_bottom=simple_draw.get_point(0, 0), right_top=simple_draw.get_point(1200, 50), color=simple_draw.COLOR_GREEN, width=0)
    simple_draw.finish_drawing()


def draw_bunches(start_point, angle1, length, count_color_tree):
    if length < 5:
        return
    if count_color_tree < 5:
        v1 = simple_draw.get_vector(start_point=start_point, angle=angle1, length=length)
        v1.draw(color=simple_draw.COLOR_PURPLE, width=2)
        v1.draw()
    else:
        v1 = simple_draw.get_vector(start_point=start_point, angle=angle1, length=length)
        v1.draw(color=simple_draw.COLOR_GREEN, width=2)
        v1.draw()

    next_count_color_tree = count_color_tree + 1
    next_point = v1.end_point
    next_angle1 = angle1 - simple_draw.random_number(30-30*.4, 30+30*.4)
    next_length = length*random.uniform(.75 - .75*.2, .75 + .75*.2)
    draw_bunches(start_point=next_point, angle1=next_angle1, length=next_length,count_color_tree=next_count_color_tree)
    next_point = v1.end_point
    next_angle1 = angle1 + simple_draw.random_number(30-30*.4, 30+30*.4)
    next_length = length*random.uniform(.75 - .75*.2, .75 + .75*.2)
    draw_bunches(start_point=next_point, angle1=next_angle1, length=next_length,count_color_tree=next_count_color_tree)

    simple_draw.finish_drawing()

