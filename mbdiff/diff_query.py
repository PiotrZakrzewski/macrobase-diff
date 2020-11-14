from pandas import DataFrame
#Allowed operators
OPS = {'>', '=', '<', '<=', '>='}

class DiffQuery:
    """Data Structure for holding a query to differentiate outliers from inliers."""

    def __init__(self, column: str, op: str, value):
        if op not in OPS:
            raise ValueError(f"Operator must be one of {OPS}")
        self.column = column
        self.op = op
        self.value = value
    
    def __str__(self):
        return f"{self.column} {self.op} {self.value}"
    
    def apply(self, df: DataFrame):
        """Apply query to a pandas table."""
        if self.op == '>':    
            return df[df[self.column] > self.value]
        elif self.op == '<':    
            return df[df[self.column] < self.value]
        elif self.op == '=':    
            return df[df[self.column] == self.value]
        elif self.op == '>=':    
            return df[df[self.column] >= self.value]
        elif self.op == '<=':    
            return df[df[self.column] <= self.value]
        raise ValueError("Incorrect operator")
