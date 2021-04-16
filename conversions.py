import os
from PIL import Image

path = "./media"
files = os.listdir(path)
for r, d, files in os.walk(path):
    for f in files:
        if f.endswith(".png"):
            jpg_name = os.path.splitext(f)[0]+'.jpg'
            print("executing:", os.path.join(r, f),
                  " to ", os.path.join(r, jpg_name))
            im1 = Image.open(os.path.join(r, f))
            rgb_im = im1.convert('RGB')
            rgb_im.save(os.path.join(r, jpg_name), quality=100)
            os.remove(os.path.join(r, f))
