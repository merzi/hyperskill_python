#  You can experiment here, it won’t be checked
from typing import List, Union

def add(x: int, y: float) -> Union[List[int], List[str]]:
    """
    adds two numbers
    :param x: ganzzahlig
    :param y: foat
    :return:
    """
    return x + y

add('', 12)
