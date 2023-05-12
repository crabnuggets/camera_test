import cv2
import os
from get_camera_index import print_cameras

# # Select camera to use
# print_cameras()

# Set up the camera
try:
    camera_number = int(input("Select camera number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FPS,60)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
cap.set(cv2.CAP_PROP_EXPOSURE, 10)

# Capture an image
ret, frame = cap.read()

# Get the exposure time used
exposure_time = cap.get(cv2.CAP_PROP_EXPOSURE)

# Add a watermark with the exposure time
text = f"{exposure_time:.2f} s"
cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Save the image to a folder called "img"
if not os.path.exists("img"):
    os.makedirs("img")
filename = f"img/image_{exposure_time:.2f}s.png"
if os.path.exists(filename):
    os.remove(filename)  # Delete the existing file
cv2.imwrite(filename, frame)

# Release the camera
cap.release()
