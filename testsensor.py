def CheckColor():
    tcs = Adafruit_TCS34725.TCS34725()
    tcs.set_interrupt(False)

    r, g, b, c = tcs.get_raw_data()

    color_temp = Adafruit_TCS34725.calculate_color_temperature(r, g, b)

    lux = Adafruit_TCS34725.calculate_lux(r, g, b)

    if color_temp is None:
        color_temp = 0

    tcs.set_interrupt(True)
    tcs.disable()
    print ("Red: {1}, Green: {2}, Blue: {3}, Clear: {4}".format(r, g, b, c))
    print ("Light Lux: {1}".format(lux))
    print ("Color Temperature: {1} K".format(color_temp))


for i in range(0, 3):
    CheckColor()
