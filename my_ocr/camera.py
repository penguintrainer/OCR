import cv2
import PIL

def capture_camera(video_source:int) -> None:
    capture = cv2.VideoCapture(video_source)
