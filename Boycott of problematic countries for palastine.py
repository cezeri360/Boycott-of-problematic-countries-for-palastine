from pyzbar.pyzbar import decode
import cv2
import winsound
import time
import pyttsx3 as pi
from colorama import Fore, Style
engine=pi.init()
cap = cv2.VideoCapture(0)
def extract_country_code(barcode_data):
    country_code = barcode_data[:3]
    return country_code
def qwer(bar_data):
    cqw = barcode_data[:2]
    return cqw
while True:
    ret, frame = cap.read()
    if ret:
        barcodes = decode(frame)
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            country_code = extract_country_code(barcode_data)
            cqw = qwer(bar_data)
            print("Barkod read: " + barcode_data)
            print("Country Code: " + country_code)
            winsound.Beep(3000, 1000)
            if country_code=="869":
                print("This product is of Turkish origin")
                engine.say("This program recommends these products.")
                engine.runAndWait()
            if country_code=="622":
                print("This product is of Egypt origin")
                engine.say("This program recommends these products.")
                engine.runAndWait()
            if country_code=="690":
                print(Fore.RED + "This product is of China origin" + Style.RESET_ALL)
                engine.say("This is a very problematic product.")
                engine.runAndWait()
            if country_code=="729":
                print(Fore.RED + "This product is of ****il origin" + Style.RESET_ALL)
                engine.say("This is a very problematic product.")
                engine.runAndWait()
            if country_code=="978":
                print("This product is book or notebook.")
                engine.say("This product is book or notebook.")
                engine.runAndWait()
            if cqw=="13":
                print(Fore.RED + "This product is of America origin" + Style.RESET_ALL)
                engine.say("This is a very problematic product.")
                engine.runAndWait()
            if country_code=="476":
                print("This product is of Azerbican origin")
                engine.say("This program recommends these products.")
                engine.runAndWait()
            if country_code=="883":
                print(Fore.RED + "This product is of Myanmar origin" + Style.RESET_ALL)
                engine.say("This is a very problematic product.")
                engine.runAndWait()
            else:
                print("This program could not find this product.")
                engine.say("This program could not find this product")
                engine.runAndWait()
    cv2.imshow('Barcode Reader', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break
cap.release()
cv2.destroyAllWindows()
time.sleep(3)
"""
This program was maked to encourage boycotts
of problematic products.
Thanks for reviewing this program. 
"""
#Israel is committing  "Guilty of humanity".
#China is committing genocide in East Turkestan.
#869:Turkey
#622:Egypt
#476:Azerbican
#978:book or notebook
#Barcode Reader
#I'm from Turkey.
####################
















