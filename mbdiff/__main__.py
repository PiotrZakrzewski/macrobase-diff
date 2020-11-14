import sys
from mbdiff.diff_query import DiffQuery
from mbdiff.diff import diff_file

min_risk = 0.1
min_support = 0.00
max_order = 3

def main():
    path = sys.argv[1]
    metric = sys.argv[2]
    op = sys.argv[3]
    value = sys.argv[4]
    query = DiffQuery(metric, op, value)
    explanations= diff_file(path, query, max_order, min_risk, min_support)
    print("Explanations")
    for rr, combination in explanations:
        print(rr, combination)

if __name__ == "__main__":
    main()
