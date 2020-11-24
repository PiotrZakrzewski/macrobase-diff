import click
from mbdiff.diff_query import DiffQuery, OPS, InvalidQuery
from mbdiff.diff import diff_file
from mbdiff.pretty_print import present_explanations, present_invalid


def validate_query(ctx, param, value):
    if not value:
        raise click.BadParameter("Cannot be empty")
    value_sp = value.split()
    if len(value_sp) != 3:
        raise click.BadParameter(
            """Query needs to be in format: "COLUMN OPERATOR VALUE" OPERATOR must be one of: <,>,=,<=,>="""
        )
    metric, op, value = value_sp
    if op not in OPS:
        raise click.BadParameter("Operator must be one of: <,>,=,<=,>=")
    return value_sp
        


@click.command()
@click.argument("data", type=click.Path(exists=True))
@click.option("--min-support", default=0.1)
@click.option("--min-risk", default=0.1)
@click.option("--max-order", default=3)
@click.option("--query", callback=validate_query, default=None)
def main(data, min_support, min_risk, max_order, query):
    metric, op, value = query
    query = DiffQuery(metric, op, value)
    try:
        explanations, invalid = diff_file(data, query, max_order, min_risk, min_support)
    except InvalidQuery as e:
        raise click.BadParameter(e)
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
