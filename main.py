from inky import InkyPHAT
from PIL import Image

# valid colors are red, yellow and black
inky_display = InkyPHAT("black")
inky_display.set_border(InkyPHAT.BLACK)

img = Image.open("/home/pi/src/superporgs/superporgs.png")
inky_display.set_image(img)
inky_display.show()
