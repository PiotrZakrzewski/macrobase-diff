# Macrobase Diff minimal implementation
This is a mnimial implementation of an idea from [DIFF: A Relational Interface for Large-Scale Data Explanation F.Abuzaid et al 2018](https://cs.stanford.edu/~matei/papers/2019/vldb_macrobase_diff.pdf).

In short: Given a table of numerical and categorical data and a query dividing the table into two groups (outliers/inliers) return attributes (categorical values) that are more common among the outliers (so called explanations).

See a simple [case study using this prototype](https://pzakrzewski.hashnode.dev/macrobase-diff-case-study-1-imdb-movies).

You can give it a quick try with provided `test.csv`:
```bash
        num_col,cat_col1,cat_col2
   2   │ 99.8,B,A
   3   │ 1.0,A,A
   4   │ 1.1,A,A
   5   │ 1.2,A,A
   6   │ 1.11,B,A
   7   │ 1.12,A,B
   8   │ 1.22,A,A
   9   │ 1.3,A,A
  10   │ 109.0,B,B
```
Run the following command to get the output for the basic risk-ratio pipeline:
```bash
python -m mbdiff --query 'num_col > 20.0' test.csv
```
The output will contain two sections:
- rows satisfying your query (outliers)
- attribute combinations that are most associated with the selected outlier group (num_col above the value of 20.0) sorted by their risk ratio.
```
Outliers:
   num_col cat_col1 cat_col2
0     99.8        B        A
8    109.0        B        B
Explanations
      score  cat_col1    cat_col2
--  -------  ----------  ----------
 0      8    B           B
 1      3.5  -           B
 2      3.5  B           A
Attribute combinations below thresholds
    cat_col1
--  ----------
 0  B
```

## Further Work
The original Macrobase Diff provides more contributions:
- Streaming implementation
- SQL-like REPL interface (to showcase how it could be implemented within an SQL client)
- Plenty of optimizations
All of the above are worthwhile for follow-up work in this project.
