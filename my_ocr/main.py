import gui
from image_process import ocr_process


def _main():
    gui.first_gui()
    gui.massage_info("Hello World")
    print(ocr_process("sample.png"))

def main():
    try:
        _main()
    except Exception:
        print("Unexpected error")

if __name__ == "__main__":
    main()