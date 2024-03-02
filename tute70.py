# Magic Method and Dunder Method

from typing import Any


class Employee:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __str__(self):
        return f"The Employee name is {self.name} print by str"

    def __repr__(self) -> str:
        return f"print by repr"
    
    def __call__(self) -> Any:
        print("this is araiz")


