from random import choice, seed
from PIL import Image

seed(0x13371337)

YELLOW_EMOJI = "🤔😊😂😭😃😚😅😞😏😋😀😌😝😒"
OTHER_EMOJI = "😡😈👿🤢"

im = Image.open("source.png")
px = im.load()

res = open("../public/task.txt", "w")

for i in range(im.height):
    for j in range(im.width):
        if px[j, i] == 1:
            print(choice(YELLOW_EMOJI), end='', file=res)
        else:
            print(choice(OTHER_EMOJI), end='', file=res)
    print(file=res)
res.close()
