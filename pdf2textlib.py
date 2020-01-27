import PIL.Image
import pdf2image
import pytesseract
from googletrans import Translator

DPI = 200
OUTPUT_FOLDER = None
FIRST_PAGE = None
LAST_PAGE = None
FORMAT = 'jpg'
THREAD_COUNT = 1
USERPWD = None
USE_CROPBOX = False
STRICT = False

index = 0


def pdftopil(PDF_PATH):
    pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE,
                                             last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD,
                                             use_cropbox=USE_CROPBOX, strict=STRICT)
    return pil_images


def save_images(pil_images):
    index = 1
    for image in pil_images:
        image.save("pages\\page_" + str(index) + ".jpg")
        index += 1
    print("Number of pages :", index - 1)
    return index


def search(output, s):
    flag = 0
    for i in s.split():
        if i in output.split():
            flag = 1
        else:
            flag = 0
    if flag:
        print("Found")
        return 1
    else:
        print("Not Found")
        return 0


def translate(s, dest):
    translator = Translator()
    l = translator.translate(s, dest=dest)
    return l


def getText(PDF_PATH, lang):
    index = save_images(pdftopil(PDF_PATH))
    output = ""
    for i in range(1, index):
        output += pytesseract.image_to_string(
            PIL.Image.open(
                'pages\\page_' + str(i) + '.jpg').convert(
                "RGB"),
            lang=lang)
        output += "\n______________________________________________________________________\n"
    print(output)


def getText(PDF_PATH):
    index = save_images(pdftopil(PDF_PATH))
    output = ""
    for i in range(1, index):
        output += pytesseract.image_to_string(
            PIL.Image.open(
                'pages\\page_' + str(i) + '.jpg').convert(
                "RGB"),
            lang='eng')
        output += "\n______________________________________________________________________\n"
    print(output)


if __name__ == "__main__":
    # getText("C:\\Users\\Kingsmanvk\\PycharmProjects\\selfPRO\\sih\\demo.pdf", "urd+tel+eng")
    getText("C:\\Users\\Kingsmanvk\\PycharmProjects\\selfPRO\\sih\\demo.pdf")
