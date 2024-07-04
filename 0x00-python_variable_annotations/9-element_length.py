#!/usr/bin/env python3
"""
iterable object_DUCK
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    size of an element
    """
    return [(i, len(i)) for i in lst]
