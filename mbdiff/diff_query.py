from pandas import DataFrame

# Allowed operators
OPS = {">", "=", "<", "<=", ">="}


class DiffQuery:
    """Data Structure for holding a query to differentiate outliers from inliers."""

    def __init__(self, column: str, op: str, value):
        if op not in OPS:
            raise ValueError(f"Operator must be one of {OPS}")
        self.column = column
        self.op = op
        if op != "=":
            self.value = float(value)
        else:
            self.value = value

    def __str__(self):
        return f"{self.column} {self.op} {self.value}"

    def apply(self, df: DataFrame):
        """Apply query to a pandas table."""
        if self.op == ">":
            return df[df[self.column] > self.value]
        elif self.op == "<":
            return df[df[self.column] < self.value]
        elif self.op == "=":
            return df[df[self.column] == self.value]
        elif self.op == ">=":
            return df[df[self.column] >= self.value]
        elif self.op == "<=":
            return df[df[self.column] <= self.value]
        raise ValueError("Incorrect operator")

    def row_matches(self, row):
        if self.op == ">":
            return row[self.column] > self.value
        elif self.op == "<":
            return row[self.column] < self.value
        elif self.op == "=":
            return str(row[self.column]) == str(self.value)
        elif self.op == ">=":
            return row[self.column] >= self.value
        elif self.op == "<=":
            return row[self.column] <= self.value
        raise ValueError("Incorrect operator")

    def mark_groups(self, df: DataFrame):
        """Add column 'outlier 'to df telling outliers from inliers based on a query."""

        def fn(row):
            return "outlier" if self.row_matches(row) else "inlier"

        df["outlier"] = df.apply(fn, axis=1)

class InvalidQuery(ValueError):
    pass
