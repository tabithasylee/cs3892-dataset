import os

from svgpathtools import svg2paths2, wsvg
from wand.image import Image

width = 64
height = 64
total_paths = 0
count = 0

for file in os.listdir("svg"):
    filename = os.fsdecode(os.path.join("svg", file))
    if filename.endswith(".svg"):
        try: 
            if not os.path.exists(os.path.join("processed_svg", file)):
                paths, attributes, svg_attributes = svg2paths2(filename)
                paths = [path for path in paths if path.d()]
                
                wsvg(paths, attributes=attributes, svg_attributes=svg_attributes, filename=os.path.join("processed_svg", file))
            
            png_name = f'{os.path.join("png", os.path.splitext(file)[0])}.png'
            if not os.path.exists(png_name):
                with Image(filename=os.path.join("processed_svg", file), width=width, height=height) as img:
                    with img.convert('png') as output_img:
                        output_img.save(filename=png_name)

            count += 1
        except Exception as e:
            print(f"error with {filename}, {e}")

print(f"Total paths: {total_paths}")
print(f"Count number: {count}")
