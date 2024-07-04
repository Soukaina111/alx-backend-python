#!/usr/bin/env python3
"""
1st element of a sequence-DUCK TYPE
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    function-safe first element
    """
    if lst:
        return lst[0]
    else:
        return None
