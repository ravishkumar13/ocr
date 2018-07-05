import cv2
import pytesseract
from PIL import Image
#Get file path from the user
path = input("Enter the file path:").strip()
#read the image
image = cv2.imread(path)
#convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#image preprocessing
temp = input("Do you want to pre-process the image ?\nThreshold : 1\nGrey : 2\nNone : 0\nEnter your choice : ").strip()

# If user enter 1, Process Threshold or if user enters 2, then process medianBlur. Else, do nothing.

if temp == "1":
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

elif temp == "2":
    gray = cv2.medianBlur(gray, 3)

filename = "{}.png".format(temp)
cv2.imwrite(filename, gray)

#apply ocr to the image
text = pytesseract.image_to_string(Image.open(filename))
print(text)