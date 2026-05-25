class StructuralShift:
    """Represents structural shift analysis of a portfolio between two periods.

    Decomposes a portfolio into named parts and computes their shares,
    period-over-period changes in shares (in percentage points),
    and verifies that the structure is closed (sum of share changes equals zero).
    """

    def __init__(
            self,
            whole_v0: float,
            whole_v1: float,
            parts_v0: dict[str, float],
            parts_v1: dict[str, float],
            name: str = ""
    ) -> None:
        """Initialize a StructuralShift instance.

        Args:
            whole_v0: Total (whole) value in the base period. Must be non-zero.
            whole_v1: Total (whole) value in the reporting period. Must be non-zero.
            parts_v0: Mapping of part name to its value in the base period.
                      Example: {"FX": 320, "Sum": 930}
            parts_v1: Mapping of part name to its value in the reporting period.
                      Must contain the same keys as parts_v0.
                      Example: {"FX": 290, "Sum": 1185}
            name: Optional label for the analysis (e.g., "Retail Deposit Portfolio").

        Raises:
            ValueError: If `whole_v0` or `whole_v1` equals zero.
            ValueError: If `parts_v0` and `parts_v1` have different keys.
        """
        if whole_v0 == 0 or whole_v1 == 0:
            raise ValueError("Whole parts must not be zero")
        elif parts_v0.keys() != parts_v1.keys():
            raise ValueError("The keys of parts_v0 and parts_v1 must be the same")
    
        self.whole_v0 = whole_v0
        self.whole_v1 = whole_v1
        self.parts_v0 = parts_v0
        self.parts_v1 = parts_v1
        self.name = name

    def shares(self, period: str) -> dict[str, float]:
        """Compute the share of each part in the whole for the given period.

        Formula:
            Share = (Part / Whole) * 100

        Args:
            period: Either "v0" (base period) or "v1" (reporting period).

        Returns:
            Mapping of part name to its share in percent.
            Example: {"FX": 25.60, "Sum": 74.40}

        Raises:
            ValueError: If `period` is not "v0" or "v1".
        """
        if period == "v0":
            whole = self.whole_v0
            parts = self.parts_v0
        elif period == "v1":
            whole = self.whole_v1
            parts = self.parts_v1
        else:
            raise ValueError(f"period must be 'v0' or 'v1'")
        
        # Build the result dictionary
        result = {}
        for name in parts:
            value = parts[name]
            share = (value / whole) * 100
            result[name] = share

        return result
    
    def delta_pp(self) -> dict[str, float]:
        """Compute the period-over-period change of each part's share, in p.p.

        Formula:
            pp = Share_v1 - Share_v0

        Returns:
            Mapping of part name to its share change in percentage points.
            Example: {"FX": -5.94, "Sum": +5.94}
        """
        shares_v0 = self.shares("v0")
        shares_v1 = self.shares("v1")

        result = {}
        for name in shares_v0:
            delta = shares_v1[name] - shares_v0[name]
            result[name] = delta

        return result
    
    def check_closed(self, tolerance: float = 0.000000001) -> bool:
        """Verify that the structure is closed: the sum of share changes equals zero.

        Args:
            tolerance: Floating-point tolerance to account for rounding errors.

        Returns:
            True if the sum of share changes is within tolerance of zero.
        """

        # Get the dict with share changes for each part, e.g. {"FX": -5.94, "Sum": 5.94}
        deltas = self.delta_pp()

        # Initialize the accumulator (where we'll add up all delta values)
        total = 0

        # Walk through each part name in the dict
        for name in deltas:
            # Add this part's delta to the running total
            total = total + deltas[name]

        # If the absolute value of the total is smaller than the allowed error,
        # the structure is closed (returns True). Otherwise returns False!
        return abs(total) < tolerance
    
    def summary_table(self) -> list[dict]:
        """Return the structural shift analysis as a list of records.

        Each record is a dict suitable for direct conversion into a pandas DataFrame.

        Returns:
            A list of dicts, one per part, with the keys:
                1. "part": part name
                2. "share_v0": share in the base period, %
                3 "share_v1": share in the reporting period, %
                4. "delta_pp": change in share, p.p.
        """
        shares_v0 = self.shares("v0")
        shares_v1 = self.shares("v1")
        deltas = self.delta_pp()

        result = []
        for name in shares_v0:
            row = {
                "part": name,
                "share_v0": shares_v0[name],
                "share_v1": shares_v1[name],
                "delta_pp": deltas[name],
            }

            result.append(row)

        return result
    

if __name__=="__main__":
    shift = StructuralShift(
        whole_v0=1250,
        whole_v1=1475,
        parts_v0={"FX": 320, "Sum":930},
        parts_v1={"FX":290, "Sum":1185}, 
        name = "Retail Deposit Portfolio"
    )

    print(f"Analysis: {shift.name}")
    print(f"Shares v0 (01.01.2024): {shift.shares('v0')}")
    print(f"Shares v1 (01.01.2025): {shift.shares('v1')}")
    print(f"Delta in p.p.: {shift.delta_pp()}")
    print(f"Structure closed: {shift.check_closed()}")
    print(f"Summary table: {shift.summary_table()}")