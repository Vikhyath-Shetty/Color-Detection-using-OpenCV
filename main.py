from detection import detect_color


def main():
    print("Running Color detection task...")
    try:
        detect_color(0, "red")
    except (RuntimeError, ValueError) as e:
        print(f"[ERROR]{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
