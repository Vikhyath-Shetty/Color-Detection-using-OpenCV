from typing import Dict
from type import HSVRange
import numpy as np

COLOR_RANGES: Dict[str, HSVRange] = {
    "red": [(np.array([20, 150, 100]), np.array([30, 255, 255])),
            (np.array([170, 100, 100]), np.array([179, 255, 255]))],
    "green": [(np.array([36, 25, 25]), np.array([86, 255, 255]))],
    "blue": [(np.array([94, 80, 2]), np.array([126, 255, 255]))]
}
