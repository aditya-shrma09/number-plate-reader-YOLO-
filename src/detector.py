from ultralytics import YOLO
import cv2
from ocr import read_plate
image = cv2.imread("images\stocksnap-car-2592136_1920.jpg")
model = YOLO("models/license_plate_detector.pt")

results = model("images\stocksnap-car-2592136_1920.jpg")


for box in results[0].boxes:

    x1, y1, x2, y2 = map(int, box.xyxy[0])

    plate = image[y1:y2, x1:x2]

    cv2.imshow("Plate", plate)
    cv2.waitKey(0)
a= read_plate(plate)
for i,char in enumerate(a) :
    print(char)
    if(i==6):
        break
