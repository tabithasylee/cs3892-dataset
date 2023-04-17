# CS 3892 - Image2SVG Dataset Utilities
Please see full_dataset.zip for the SVGs scraped, for the SVGs converted to pngs, and also for the SVGs all converted to paths only. 

## Scrape from the Noun Project
To scrape from SVGs numbering 1 to 100, and saving them as a png with width 256 and height 256
```
python noun_scrape.py -s 1 -e 100 -w 256 - h 256
```

## Minify SVGs
Using Scour 
```
python minify_svg.py
```

## To convert an SVG to SFD
```
python svg2sfd.py
```

## Generating a random SVG
Parameters:
```
-e Number of randomly generated elements per SVG
-f Name of folder to save SVGs to
-n Number of SVG elements to generate
-t Total number of files to generate
-c Whether to generate the SVG with color

python create_svg.py -e 10 -t 1000 

```