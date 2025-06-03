from bs4 import BeautifulSoup
import re

def crop_svg_advanced(input_file, output_file, x, y, width, height):
    with open(input_file, 'r') as f:
        soup = BeautifulSoup(f.read(), 'xml')
    
    svg = soup.find('svg')
    if not svg:
        raise ValueError("No SVG element found")
    
    # Set new viewBox and dimensions
    svg['viewBox'] = f'{x} {y} {width} {height}'
    svg['width'] = str(width)
    svg['height'] = str(height)
    
    # Optionally add clipping path
    defs = svg.find('defs')
    if not defs:
        defs = soup.new_tag('defs')
        svg.insert(0, defs)
    
    clip_path = soup.new_tag('clipPath', id='crop-area')
    rect = soup.new_tag('rect', x=str(x), y=str(y), 
                       width=str(width), height=str(height))
    clip_path.append(rect)
    defs.append(clip_path)
    
    # Apply clipping to main group
    g = soup.new_tag('g')
    g['clip-path'] = 'url(#crop-area)'
    
    # Move all existing content into the clipped group
    for child in list(svg.children):
        if child.name not in ['defs', 'title', 'desc']:
            child.extract()
            g.append(child)
    
    svg.append(g)
    
    # Write output
    with open(output_file, 'w') as f:
        f.write(str(soup))

# Usage
crop_svg_advanced('paper2code_diagrams2.svg', 'output_cropped.svg', x=0, y=0, width=576, height=280)
# Example usage
# crop_svg("paper2code_diagrams.svg", "output_cropped.svg", margin=1000)
