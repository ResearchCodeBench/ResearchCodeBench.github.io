#!/usr/bin/env python3
"""
mov2gif_crop.py
---------------
Crop a video from a configurable starting point to specified end coordinates and export as a GIF or image sequence.

Dependencies:
    pip install moviepy

Usage example:
    python mov2gif_crop.py \
        --input in.mov \
        --output out.gif \
        --start_x 100 --start_y 50 \
        --crop_x 640 --crop_y 360 \
        --gif_width 320 --gif_height 180 \
        --fps 12 --loop 0
        
    # Or save as image sequence:
    python mov2gif_crop.py \
        --input in.mov \
        --images_folder frames_output \
        --start_x 100 --start_y 50 \
        --crop_x 640 --crop_y 360 \
        --fps 12
"""
import argparse
from pathlib import Path

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.Crop import Crop
from moviepy.video.fx.Resize import Resize


def parse_args():
    p = argparse.ArgumentParser(
        description="Crop a MOV (or any video) and turn it into a GIF or image sequence."
    )
    p.add_argument("--input", "-i", required=True, help="Path to input .mov")
    
    # Output options - either GIF or image folder (or both)
    p.add_argument("--output", "-o", help="Path to output .gif (optional if using --images_folder)")
    p.add_argument("--images_folder", help="Folder to save individual frame images (optional alternative to GIF)")

    # Crop region starting point (top-left corner of crop region)
    p.add_argument("--start_x", type=int, default=0, help="X coordinate of crop region start (default: 0)")
    p.add_argument("--start_y", type=int, default=0, help="Y coordinate of crop region start (default: 0)")
    
    # Crop region end point (bottom-right corner of crop region)
    p.add_argument("--crop_x", type=int, required=True, help="X coordinate of crop region end (bottom-right corner)")
    p.add_argument("--crop_y", type=int, required=True, help="Y coordinate of crop region end (bottom-right corner)")

    # Optional final GIF resolution (default = keep cropped size)
    p.add_argument("--gif_width", type=int, help="Target GIF width")
    p.add_argument("--gif_height", type=int, help="Target GIF height")

    p.add_argument(
        "--fps",
        type=int,
        default=15,
        help="Frames per second in the output GIF or frame extraction rate (default 15)",
    )
    p.add_argument(
        "--loop",
        type=int,
        default=0,
        help="How many times to loop: 0 = forever (default), 1 = play once, etc.",
    )
    p.add_argument(
        "--image_format",
        default="png",
        choices=["png", "jpg", "jpeg"],
        help="Image format for saved frames (default: png)",
    )
    return p.parse_args()


def main():
    args = parse_args()
    
    # Validate that at least one output option is specified
    if not args.output and not args.images_folder:
        raise ValueError("Must specify either --output (for GIF) or --images_folder (for image sequence) or both")

    in_path = Path(args.input)
    if not in_path.exists():
        raise FileNotFoundError(f"{in_path} doesn't exist")

    print(f"Loading {in_path} …")
    clip = VideoFileClip(str(in_path))

    crop_width = args.crop_x - args.start_x
    crop_height = args.crop_y - args.start_y
    print(f"Cropping from ({args.start_x},{args.start_y}) to ({args.crop_x},{args.crop_y}) - {crop_width}×{crop_height} px")
    clip = clip.with_effects([Crop(x1=args.start_x, y1=args.start_y, x2=args.crop_x, y2=args.crop_y)])

    # Optional resize
    if args.gif_width and args.gif_height:
        print(f"Resizing to {args.gif_width}×{args.gif_height} px")
        clip = clip.with_effects([Resize(newsize=(args.gif_width, args.gif_height))])

    # Save as GIF if output path specified
    if args.output:
        out_path = Path(args.output)
        print(
            f"Writing GIF → {out_path}  "
            f"({args.fps} fps, loop={args.loop if args.loop else '∞'})"
        )
        # write_gif handles palette generation internally
        clip.write_gif(str(out_path), fps=args.fps)
        print("GIF created ✔️")

    # Save as image sequence if images_folder specified
    if args.images_folder:
        images_dir = Path(args.images_folder)
        images_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"Saving frames to {images_dir}/ at {args.fps} fps as .{args.image_format} files")
        
        # Create filename pattern with proper zero-padding
        total_frames = int(clip.duration * args.fps)
        padding = len(str(total_frames))
        filename_pattern = f"frame_%0{padding}d.{args.image_format}"
        
        clip.write_images_sequence(
            str(images_dir / filename_pattern), 
            fps=args.fps
        )
        print(f"Image sequence created ✔️ ({total_frames} frames)")

    print("Done ✔️")


if __name__ == "__main__":
    main()
