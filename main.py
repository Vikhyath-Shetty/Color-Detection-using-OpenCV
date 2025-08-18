import argparse
from detection import detect_color
from type import ColorInput


# cam_src -> 0 or http://....
# color -> either of {"red", "blue", "green", "yellow"} or combination of the same.
def main(cam_src: int | str, color: ColorInput):
    print("Running Color detection task...")
    try:
        detect_color(cam_src, color)
    except (RuntimeError, ValueError) as e:
        print(f"[ERROR]{type(e).__name__}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Color Detection")
    parser.add_argument(
        "--camera", type=int, default=0, help="Camera source (default=0)"
    )
    parser.add_argument(
        "--color",
        nargs="+",
        choices=["red", "green", "blue", "yellow"],
        default="red",
        help="Color(s) to detect",
    )
    args = parser.parse_args()

    try:
        camera = int(args.camera)
    except:
        camera = args.camera

    if len(args.color) == 1:
        colors = args.color[0]
    else:
        colors = set(args.color)
    main(camera, colors)
