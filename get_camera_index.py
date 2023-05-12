import cv2

# Find the indices of all connected cameras
def print_cameras():
    for i in range(10):
        try:
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                print(f"Camera {i}: {cap.get(cv2.CAP_PROP_FPS)} fps")
                cap.release()
        except cv2.error:
            print("Index out of range")
