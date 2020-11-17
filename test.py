
import simple_draw as sd

sd.resolution = (800, 600)


def branch(point, angle, length):
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()

    next_point = v1.end_point
    next_angle = v1.angle - 30
    next_length = v1.length * .75

    branch(point=next_point, angle=next_angle, length=next_length)


point_0 = sd.get_point(200,200)
branch(point=point_0, angle=90, length=50)
branch(point=point_0, angle=90, length=100)
branch(point=point_0, angle=90, length=200)


sd.pause()