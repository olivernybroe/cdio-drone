from pyzbar.pyzbar import decode
from PIL import Image

decode(Image.open('sample.png'))