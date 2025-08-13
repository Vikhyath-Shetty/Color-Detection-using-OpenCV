from typing import Union, Literal, Set
import numpy as np
from typing import Tuple, Sequence

color = Literal["red", "green", "blue"]
colorSet = Set[color]
colorInput = Union[color, colorSet]


SingleHSVRange = Tuple[np.ndarray, np.ndarray]
HSVRange = SingleHSVRange | Sequence[SingleHSVRange]