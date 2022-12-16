import pyocr
from PIL import Image


def ocr_process(path):
    pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    # OCRエンジン取得
    tools = pyocr.get_available_tools()
    tool = tools[0]

    # OCRの設定
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)

    img = Image.open(path)

    img_g = img.convert('L')  # Gray変換

    # 画像からOCRで日本語を読んで、文字列として取り出す
    txt_pyocr = tool.image_to_string(img_g , lang='jpn', builder=builder)

    # 半角スペースを消す ※読みやすくするため
    txt_pyocr = txt_pyocr.replace(' ', '')

    print(txt_pyocr)

if __name__ == "__main__":
    ocr_process('sample.png')