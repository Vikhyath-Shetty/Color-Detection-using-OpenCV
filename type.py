from typing import Literal, Set, Union, Tuple, List
import numpy as np
from numpy.typing import NDArray

# Type for color input from user
Color = Literal["red", "green", "blue", "yellow"]
ColorSet = Set[Color]
ColorInput = Union[Color, ColorSet]

# HSV color space representations
HSVBound = NDArray[np.uint8]
HSVPair = Tuple[HSVBound, HSVBound]
HSVRange = List[HSVPair]
