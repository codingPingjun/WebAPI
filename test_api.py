# import the necessary packages
import requests
import cv2
import matplotlib.pyplot as plt

# define the URL to our face detection API
url = "http://localhost:8001/face_detection/detect/"

# use our face detection API to find faces in images via image URL
# image = cv2.imread("obama.jpg")
payload = {"url": "http://www.pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg"}
r = requests.post(url, data=payload).json()
print "obama.jpg: {}".format(r)

# # loop over the faces and draw them on the image
# for (startX, startY, endX, endY) in r["faces"]:
#     cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
#
# cv2.imshow("obama.jpg", image)
# cv2.waitKey(0)
