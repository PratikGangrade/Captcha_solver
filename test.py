import requests
from bs4 import BeautifulSoup
from pytesseract import pytesseract
import cv2


# Fetch the Captcha
url = "https://ceoelection.maharashtra.gov.in/searchlist/"

r = requests.get(url)
content = r.content

soup = BeautifulSoup(content, 'html.parser')

captcha_url = url+'Captcha.aspx'

with open('photo'+'.jpg', 'wb') as f:
    im = requests.get(captcha_url)
    f.write(im.content)

#Pre-process the Image 
def invert_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Invert the image
    inverted_image = cv2.bitwise_not(image)

    # Display the original and inverted images
    cv2.imshow('Original Image', image)
    cv2.imshow('Inverted Image', inverted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



#For Recognition 
# class OCR:
#     def __init__(self):
#         self.path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#     def extract(self, filename):
#         try:
#             pytesseract.tesseract_cmd = self.path
#             text = pytesseract.image_to_string(filename)
#             print()
#             return text
#         except Exception as e:
#             print(e)
#             return "error"
        
# ocr = OCR()
# text = ocr.extract('Captcha.jpg')

# print("hello", text)

