import cv2 as cv
import logging


import numpy as np
from config import COLOR_RANGES
from type import ColorInput


def create_mask(frame: np.ndarray, color: ColorInput):
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    combined_mask = None

    # Mask for Red
    if "red" in color:
        red_lower_mask = cv.inRange(
            hsv_frame, COLOR_RANGES["red"][0][0], COLOR_RANGES["red"][0][1])
        red_upper_mask = cv.inRange(
            hsv_frame, COLOR_RANGES["red"][1][0], COLOR_RANGES["red"][1][1])
        red_mask = cv.bitwise_or(red_lower_mask, red_upper_mask)
        combined_mask = red_mask

    # Mask for green
    if "green" in color:
        lower, upper = COLOR_RANGES["green"]
        green_mask = cv.inRange(hsv_frame, lower, upper)
        combined_mask = green_mask if combined_mask is None else cv.bitwise_or(
            combined_mask, green_mask)

    # Mask for Blue
    if "blue" in color:
        lower, upper = COLOR_RANGES["blue"]
        blue_mask = cv.inRange(hsv_frame, lower, upper)
        combined_mask = blue_mask if combined_mask is None else cv.bitwise_or(
            combined_mask, blue_mask)

    return combined_mask


def detect_color(cam_src: int | str, color: ColorInput):
    cap = cv.VideoCapture(cam_src)
    if not cap.isOpened():
        logging.error("Failed to open camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            logging.error("Failed to grab frame from camera")
            continue
        mask = create_mask(frame, color)
        masked_frame = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow("Detecting Color", masked_frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
