"""Python Types for Internal Logging Objects."""
from typing import Dict
from typing import Union


LOG_VALUE_TYPE = Union[str, int, float]
LOG_TYPE = Dict[str, LOG_VALUE_TYPE]

LOG_INLINE_DICT_TYPE = Dict[str, Union[LOG_VALUE_TYPE, LOG_TYPE]]
