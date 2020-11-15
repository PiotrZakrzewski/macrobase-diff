import sys
import click
from mbdiff.diff_query import DiffQuery
from mbdiff.diff import diff_file


@click.command()
@click.argument("data", type=click.Path(exists=True))
@click.option("--min-support", default=0.1)
@click.option("--min-risk", default=0.1)
@click.option("--max-order", default=3)
@click.option("--query")
def main(data, min_support, min_risk, max_order, query):
    metric, op, value = query.split()
    query = DiffQuery(metric, op, value)
    explanations = diff_file(data, query, max_order, min_risk, min_support)
    print("Explanations")
    explanations = sorted(explanations, key=lambda x: x[0], reverse=True)
    for rr, combination in explanations:
        print(rr, combination)


if __name__ == "__main__":
    main()
