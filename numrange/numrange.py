from dataclasses import dataclass


@dataclass
class ClosedRange:
    lower: int
    upper: int

    def __post_init__(self):
        if self.upper < self.lower:
            raise ValueError("Upper value must be larger than lower value")

    def isin(self, num: int) -> bool:
        return num >= self.lower and num <= self.upper

    def to_str(self) -> str:
        upper_str = f"{str(self.upper)}]"
        lower_str = f"[{str(self.lower)}"
        return f"{lower_str}, {upper_str}"
