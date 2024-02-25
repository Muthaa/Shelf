from rembg import remove
from PIL import Image

input_path = 'proactive.png'
output_path = 'be.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
