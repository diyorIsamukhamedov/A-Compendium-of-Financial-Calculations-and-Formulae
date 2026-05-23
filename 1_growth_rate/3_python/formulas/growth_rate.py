class GrowthRate:
    """Represents a growth rate calculation between two periods."""

    def __init__(self, v0: float, v1: float, name: str) -> None:
        if v0 == 0:
            raise ValueError("Base-period value cannot be zero.")
        
        self.v0 = v0
        self.v1 = v1
        self.name = name

    def percentage(self) -> float:
        return ((self.v1 - self.v0) / self.v0) * 100


if __name__ == "__main__":
    total = GrowthRate(v0=1250, v1=1475, name="Total Portfolio")
    sum_part = GrowthRate(v0=930, v1=1185, name="Sum-denominated")
    fx_part = GrowthRate(v0=320, v1=290, name="FX Component")

    # Make calculations colourful in stdout
    NEON_GREEN = "\033[1;92m"
    RESET = "\033[0m"

    print(f"{total.name}: {NEON_GREEN}{total.percentage():+.2f}%{RESET}")
    print(f"{sum_part.name}: {NEON_GREEN}{sum_part.percentage():+.2f}%{RESET}")
    print(f"{fx_part.name}: {NEON_GREEN}{fx_part.percentage():+.2f}%{RESET}")