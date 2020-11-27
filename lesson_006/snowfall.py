import simple_draw as sd
import snowfall_module

sd.resolution = (1200, 700)


while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    snowfall_module.create_snow(3)
    while True:
        snowfall_module.draw_snow_color(sd.background_color)
        snowfall_module.move_snowflakes()
        snowfall_module.draw_snow_color(sd.COLOR_YELLOW)

        sd.sleep(.5)
        if sd.user_want_exit():
            break

    if sd.user_want_exit():
        break

sd.pause()
