import easyocr
import cv2
import re

reader = easyocr.Reader(['en'])

def read_plate(plate):

    plate = cv2.resize(
        plate,
        None,
        fx=1,
        fy=1,
        interpolation=cv2.INTER_CUBIC
    )

    results = reader.readtext(plate)

    if not results:
        return ""

    results = sorted(results, key=lambda r: r[0][0][0])
    text = ""

    for _, detected_text, _ in results:
        text += detected_text

    text = re.sub(r'[^A-Z0-9]', '', text.upper())

    return text