import subprocess
import sys

try:
    import pytesseract
except ImportError:
    print("pytesseract is not installed. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytesseract"])
    import pytesseract

try:
    import cv2
except ImportError:
    print("cv2 is not installed. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
    import cv2

img = cv2.imread('./1_95.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

height, width, _ = img.shape
configurations = r''
# configurations = r'--oem 3 --psm 6 outputbase digits' """To detect only digits"""
boxes = pytesseract.image_to_data(img, config=configurations)

for index, box in enumerate(boxes.splitlines()):
    """Split each box to a list of strings to get each information individualy"""
    if index != 0:
        box = box.split()
        # print(box)
        if len(box) == 12:
            x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (255, 255, 0), 2)
            cv2.putText(img, box[11], (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0Q), 1)


cv2.imshow('image', img)

while cv2.waitKey(1) != ord('q'):
    pass
