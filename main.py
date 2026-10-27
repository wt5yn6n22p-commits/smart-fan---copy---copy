temp = 0
OLED.init(64, 128)

def on_forever():
    global temp
    temp = 0
basic.forever(on_forever)
