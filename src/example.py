from typing import Union

from src.utils.hello import hello, name


def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """функция, складывающая два числа"""
    return x + y


print(name)
print(hello())
