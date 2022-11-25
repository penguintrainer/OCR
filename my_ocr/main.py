from my_ocr import gui

def _main():
    gui.massage_info("Hello World")

def main():
    try:
        _main()
    except Exception:
        print("Unexpected error")

if __name__ == "__main__":
    main()