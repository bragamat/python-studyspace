from dataclasses import dataclass, field
from typing import List 

@dataclass(init=True)
class Student:
    """Class for managing BJJ students."""
    name: str
    belt: str = "white"
    stripes: int = 0
    moves: List = field(default_factory=lambda: [])


    def learn_move(self, move_name: str) -> None:
        self.moves.append(move_name)
