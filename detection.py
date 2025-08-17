import logging
import cv2 as cv
import numpy as np
from type import Color, ColorInput
from config import COLOR_RANGES
from utils import is_color_input

#Function to create mask for red
def create_red_mask(frame: np.ndarray) -> np.ndarray:
    red_range = COLOR_RANGES["red"]
    red_mask_1 = cv.inRange(frame, red_range[0][0], red_range[0][1])
    red_mask_2 = cv.inRange(frame, red_range[1][0], red_range[1][1])
    red_mask = cv.bitwise_or(red_mask_1, red_mask_2)
    return red_mask


#Function to create mask for other colors
def create_other_mask(frame: np.ndarray, color: Color) -> np.ndarray:
    color_range = COLOR_RANGES[color]
    mask = cv.inRange(frame,color_range[0][0],color_range[0][1])
    return mask


#Function to create mask 
def create_mask(frame: np.ndarray, color: ColorInput) -> np.ndarray:
    if isinstance(color, str):
        if str == "red":
            mask = create_red_mask(frame)
        else:
            mask = create_other_mask(frame, color)
    else:
        for col in color:
            if col == "red":
                mask = create_red_mask(frame)
            else:
                mask = create_other_mask(frame,col)    
    return mask


#Function to detect color from the video feed
def detect_color(cam_src: int | str, color: ColorInput) -> None:
    if not is_color_input:
        raise ValueError("Invalid color parameter")
    
    cap = cv.VideoCapture(cam_src)
    if not cap.isOpened():
        raise RuntimeError("Failed to open camera")

    while True:
        ret, frame = cap.read()
        if not ret:
            logging.warning("Failed to read frame from camera")
            continue
        
        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        mask = create_mask(hsv_frame, color)
        result = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('Color Detection', result)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
