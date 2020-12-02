"""Module for abstracing away different implementation of explanation finding."""
from typing import List


class Explanation:
    """Representation of a single explanation."""

    def __init__(self, attrs:List[str], support, score) -> None:
        self.attrs = attrs
        self.support = support
        self.score = score
    
    def __str__(self) -> str:
        attrs = "\t".join(self.attrs)
        return f"{self.score}\t{self.support}\t" + attrs
