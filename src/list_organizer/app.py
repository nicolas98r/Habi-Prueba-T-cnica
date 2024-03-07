"""App Package."""

from typing import List


def sort_list(list: List[int]) -> str:
    """Sort a list of int in separate block space.

    Arguments:
        list:List[int] List of int to be sorted.

    Returns:
        str -- Str of numbers sorted and separated by blocks.
    """
    ordered_list = []
    block = []

    for num in list:
        if num == 0:
            if block:
                ordered_list.append("".join(sorted(block)))
                block = []
            else:
                ordered_list.append("X")
        else:
            block.append(str(num))

    if block:
        ordered_list.append("".join(sorted(block)))

    return " ".join(ordered_list)
