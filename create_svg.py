import random
import argparse
import os

parser = argparse.ArgumentParser(prog="SVG generator")

class Element:
    def __init__(self, element_type, color):
        self.x_range = (random.randint(0, 256), random.randint(0, 256))
        self.y_range = (random.randint(0, 256), random.randint(0, 256))
        self.element_type = element_type
        self.color = color
        self.code = ""

    def make_shape(self):
        match self.element_type:
            case "circle":
                self.make_circle()
            case "rect":
                self.make_rect()
            case "line":
                self.make_line()
            case "polygon":
                self.make_polygon()
            case "path":
                self.make_path()

        fill_color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
        stroke_color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
        
        match random.randint(0,2):
            case 0:
                self.code += f' stroke="{stroke_color}"'
            case 1:
                self.code += f' fill="{fill_color}"'
            case 2: 
                self.code += f' fill="{fill_color}"'
                self.code += f' stroke="{stroke_color}"'

        self.code += '/>'

    def make_circle(self):
        cx = self.x_range[0] + int((self.x_range[1] - self.x_range[0]) / 2)
        cy = self.y_range[0] + int((self.y_range[1] - self.y_range[0]) / 2)
        r = min(abs(int((self.x_range[1] - self.x_range[0]) / 2)),
                abs(int((self.y_range[1] - self.y_range[0]) / 2)))
        self.code = f'<circle cx="{cx}" cy="{cy}" r="{r}"'

    def make_rect(self):
        width = abs(self.x_range[1] - self.x_range[0])
        height = abs(self.y_range[1] - self.y_range[0])
        self.code = f'<rect x="{self.x_range[0]}" y="{self.y_range[0]}" width="{width}" height="{height}"'

    def make_line(self):
        self.code = f'<line x1="{self.x_range[0]}" y1="{self.y_range[0]}" x2="{self.x_range[1]}" y2="{self.y_range[1]}"'

    def make_polygon(self):
        num_points = random.randint(1, 10)
        pointsList = []
        for _ in range(num_points):
            pointsList.append((self.x_range[0] + (round(random.random(), 2) * (self.x_range[1] - self.x_range[0])),
                                self.y_range[0] + (round(random.random(), 2) * (self.y_range[1] - self.y_range[0]))))
        pointsList.sort()
        pointsString = ""
        for par in pointsList:
            pointsString += f"{par[0]},{par[1]} "
        pointsString.rstrip()
        self.code = f'<polygon points="{pointsString}"'

    def make_path(self):
        num_points = random.randint(1, 10)
        points = ["M", "L", "V", "H", "Z"]
        self.code = '<path d="'
        for _ in range(num_points):
            point = random.choice(points)
            x = random.randint(0, 256)
            y = random.randint(0, 256)

            match point:
                case "M":
                    self.code += f'M{x} {y}'
                case "L":
                    self.code += f'L{x} {y}'
                case "H":
                    self.code += f'H{x}'
                case "V":
                    self.code += f'V{y}'
                case "Z":
                    self.code +='Z'
                    
        self.code += '"'
        
        

# input is matrix that is a quad tree and then the file name of output you can do export to png too GLHF
def generate(args, filename):
    generated_elements = []

    for _ in range(int(args.number)):
        element_types = ["circle", "rect", "line", "polygon", "path"]
        element_type = random.choice(element_types)
        
        # print(f"Generating {element_type}...")
        element = Element(element_type, args.color)
        element.make_shape()
        generated_elements.append(element)


    print(f"Generating {filename}...")
    with open(filename, "w") as file:
        file.write(
            f'<svg viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">')
        for element in generated_elements:
            file.write(f"\n\t{element.code}")
        file.write("\n</svg>")


if __name__ == '__main__':
    parser.add_argument("-e", "--elements", default=1,
                        help="Number of randomly generated elements per SVG")
    parser.add_argument("-f", "--filename", default="generated_svg",
                        help="Name of folder to write SVG to")
    parser.add_argument("-n", "--number", default=20,
                        help="Number of SVG elements to generate")
    parser.add_argument("-t", "--total", default=1,
                        help="Number of files  to generate")
    parser.add_argument('-c', '--color', action='store_true') 

    args = parser.parse_args() 

    for i in range(int(args.total)):
        generate(args, os.path.join(args.filename, f"{i}.svg"))