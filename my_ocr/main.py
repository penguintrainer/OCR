def _main():
    print("Hello World")

def main():
    try:
        _main()
    except Exception:
        print("Unexpected error")

if __name__ == "__main__":
    main()