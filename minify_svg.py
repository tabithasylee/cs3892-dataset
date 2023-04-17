from scour.scour import start as scour, parse_args as scour_args, getInOut as scour_io
import os

def scour_svg():
    for directory in os.listdir("svg"):
        for file in os.listdir(os.path.join("svg", directory)):
            filename = os.fsdecode(os.path.join("svg", directory, file))
            outfilename = os.path.join("minified", file)
            if filename.endswith(".svg"):
                try:
                    options = scour_args()
                    options.infilename = filename
                    options.outfilename = outfilename
                    
                    (input, output) = scour_io(options)
                    scour(options, input, output)
                except:
                    print(f"error with {filename}")

if __name__ == '__main__': 
    scour_svg()