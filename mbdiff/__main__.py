import click
from mbdiff.diff_query import DiffQuery
from mbdiff.diff import diff_file
from mbdiff.pretty_print import present_explanations, present_invalid


@click.command()
@click.argument("data", type=click.Path(exists=True))
@click.option("--min-support", default=0.1)
@click.option("--min-risk", default=0.1)
@click.option("--max-order", default=3)
@click.option("--query")
def main(data, min_support, min_risk, max_order, query):
    metric, op, value = query.split()
    query = DiffQuery(metric, op, value)
    explanations, invalid = diff_file(data, query, max_order, min_risk, min_support)
    if explanations:
        explanations = sorted(explanations, key=lambda x: x[0], reverse=True)
        print("Explanations")
        print(present_explanations(explanations))
    else:
        print("Could not find any explanations for this input")
    if invalid:
        print("Attribute combinations below thresholds")
        print(present_invalid(invalid))
    else:
        print("There were no invalid or below threshold attribute combinations")



if __name__ == "__main__":
    main()
