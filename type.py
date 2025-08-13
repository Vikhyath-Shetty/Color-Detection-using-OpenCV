from typing import List, Literal, Set
import numpy as np
from typing import Tuple

Color = Literal["red", "green", "blue"]
ColorInput = Set[Color]


HSVRange = List[Tuple[np.ndarray, np.ndarray]]