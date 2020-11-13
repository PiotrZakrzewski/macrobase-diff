import sys

min_risk = 0.1
min_support = 0.01
max_order = 3

def main():
    path = sys.argv[1]
    metric = sys.argv[2]
    explanations, unprocessed = diff(path, metric, max_order, min_risk, min_support)
    print("\n".join(explanations))
    print("Could not include following attributes")
    print("\n".join(unprocessed))

if __name__ == "__main__":
    main()
