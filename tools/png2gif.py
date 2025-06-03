#!/usr/bin/env python3
"""
PNG to GIF Converter
Converts a folder of PNG images to a non-looping animated GIF.
"""

import os
import glob
from PIL import Image
import re

def natural_sort_key(text):
    """
    Sort function for natural ordering of filenames with numbers.
    """
    return [int(c) if c.isdigit() else c for c in re.split(r'(\d+)', text)]

def png_to_gif(input_folder, output_filename, duration=100):
    """
    Convert PNG files in a folder to an animated GIF.
    
    Args:
        input_folder (str): Path to folder containing PNG files
        output_filename (str): Output GIF filename
        duration (int): Duration per frame in milliseconds (default: 100ms)
    """
    
    # Get all PNG files in the folder
    png_files = glob.glob(os.path.join(input_folder, "*.png"))
    
    if not png_files:
        print(f"No PNG files found in {input_folder}")
        return
    
    # Sort files naturally (frame_001.png, frame_002.png, etc.)
    png_files.sort(key=natural_sort_key)
    
    print(f"Found {len(png_files)} PNG files")
    print(f"Processing files from {os.path.basename(png_files[0])} to {os.path.basename(png_files[-1])}")
    
    # Load all images
    images = []
    for png_file in png_files:
        try:
            img = Image.open(png_file)
            # Convert to RGB if necessary (GIF doesn't support transparency the same way)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            images.append(img)
            print(f"Loaded: {os.path.basename(png_file)}")
        except Exception as e:
            print(f"Error loading {png_file}: {e}")
    
    if not images:
        print("No images could be loaded")
        return
    
    # Save as GIF
    try:
        images[0].save(
            output_filename,
            save_all=True,
            append_images=images[1:],
            duration=duration,
            optimize=True
        )
        print(f"Successfully created GIF: {output_filename}")
        print(f"Total frames: {len(images)}")
        print(f"Duration per frame: {duration}ms")
        print("Loop setting: No loop (plays once)")
        
        # Get file size
        file_size = os.path.getsize(output_filename)
        print(f"Output file size: {file_size / 1024 / 1024:.2f} MB")
        
    except Exception as e:
        print(f"Error creating GIF: {e}")

def main():
    """Main function to run the PNG to GIF conversion."""
    
    # Configuration
    input_folder = "output_frames2"
    output_filename = "animation.gif"
    frame_duration = 100  # milliseconds per frame
    
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist")
        return
    
    print("PNG to GIF Converter")
    print("=" * 30)
    print(f"Input folder: {input_folder}")
    print(f"Output file: {output_filename}")
    print(f"Frame duration: {frame_duration}ms")
    print()
    
    # Convert PNG files to GIF
    png_to_gif(input_folder, output_filename, frame_duration)

if __name__ == "__main__":
    main()
