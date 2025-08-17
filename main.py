from config import PHONE_CAM
from detection import detect_color


#detect_color(0) -> webcam
#detect_color(PHONE_CAM) -> other alternate camera
def main():
    print("Running Color detection task...")
    try:
        detect_color(PHONE_CAM, "red")
    except (RuntimeError, ValueError) as e:
        print(f"[ERROR]{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
