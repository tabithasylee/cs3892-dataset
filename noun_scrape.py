import requests
from requests_oauthlib import OAuth1
import argparse
from wand.image import Image
import os

parser = argparse.ArgumentParser(prog="SVG scraper")

keys = []
secrets = []

def get_and_save_svg(args):
    start, end = int(args.start), int(args.end)
    folder_start, folder_end = ((start // 5000) * 5000) + 1, ((start // 5000) + 1) * 5000
    key = int(args.key)
    auth = OAuth1(keys[key], secrets[key])
    
    for num in range(start, end):
        try:
            response = requests.get(f"http://api.thenounproject.com/icon/{num}", auth=auth)
        except requests.exceptions.HTTPError as e:
            print(e.response.text)

        svg_path = f"{num}_svg"
        full_path = os.path.join("svg", f"{folder_start}-{folder_end}", f"{svg_path}.svg")
        if not os.path.exists(full_path):
            try:
                reqUrl = response.json()["icon"]["icon_url"]
                res = requests.get(reqUrl)
                resContent = res.content

                f = open(full_path, "w")
                f.write(resContent.decode('UTF-8'))
                f.close()

                convert_svg_to_png(svg_path, folder_start, folder_end, args.width, args.height)
                print(f"Saved to {svg_path}...")
            except: 
                # print(f"Error with response. Skipping svg {num}")
                pass
        else:
            print(f"{svg_path} already saved.")

def convert_svg_to_png(svg_path, folder_start, folder_end, width, height):
    svg_full_path = os.path.join("svg", f"{folder_start}-{folder_end}", f"{svg_path}.svg")
    if os.path.exists(svg_full_path):
        with Image(filename=svg_full_path, width=width, height=height) as img:
            with img.convert('png') as output_img:
                output_img.save(filename=os.path.join("png", f"{folder_start}-{folder_end}", f"{svg_path}.png"))

if __name__ == "__main__":
    parser.add_argument("-s", "--start", default=1,
                        help="Start of SVGs")
    parser.add_argument("-e", "--end", default=1,
                        help="End of SVGs")
    parser.add_argument("-w", "--width", default=64,
                        help="Width of SVGs")
    parser.add_argument("-he", "--height", default=64,
                        help="Height of SVGs")
    parser.add_argument("-k", "--key", default=0,
                        help="Height of SVGs")
    parser.add_argument('-c', '--convert', action='store_true') 

    args = parser.parse_args()
    
    if args.convert:
        start, end = int(args.start), int(args.end)
        folder_start, folder_end = ((start // 5000) * 5000) + 1, ((start // 5000) + 20) * 5000
        key = int(args.key)
    
        for num in range(start, end):
            svg_path = f"{num}_svg"
            full_path = os.path.join("png", f"{folder_start}-{folder_end}", f"{svg_path}.png")
            if not os.path.exists(full_path):
                convert_svg_to_png(svg_path, folder_start, folder_end, args.width, args.height)
    else:
        get_and_save_svg(args)