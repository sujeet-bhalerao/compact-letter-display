# Compact Letter Display in Python

## Description
This is a collection of scripts that perform analysis of variance (ANOVA), posthoc comparison tests (Tukey HSD and Fisher's LSD), and generate a compact letter display, representing a summary of the results.

## Compact Letter Display Algorithm
`cld_calculator.py` uses the insert-absorb algorithm from "Hans-Peter Piepho (2004), An Algorithm for a Letter-Based Representation of All-Pairwise Comparisons, Journal of Computational and Graphical Statistics, 13(2), 456--466."

Here is the insert-and-absorb algorithm:

1. Generate a column connecting all treatments (i.e., give them all the same letter).
2. For each significant comparison, do the following:
  - For each column currently in the display, do the following:
    * If the column connects the two significantly different treatments (i.e., has the same letter for the two significantly different treatments), then do the following:
      - Duplicate the column.
      - In the first of the two columns, delete the letter corresponding to the one treatment. If possible, absorb the column into another column.
      - In the second of the two columns, delete the letter corresponding to the other treatment. If possible, absorb the column into another column.

## Parameters for `anova_cld()`
The following parameters can be customized when using anova_cld():

1. `data`: This can be a pandas DataFrame or a path to a .csv or .xlsx file which contains the data to be analyzed.

2. `columns` (default: None): This is an optional parameter, a list of column names to be used in the test. If it is None, the test is performed on all columns in the data.

3. `alpha` (default: 0.05): This sets the significance level for the ANOVA and pairwise comparison tests.

4. `method` (default: "TukeyHSD"): This lets you choose the method for pairwise comparison. It can either be "TukeyHSD"  for Tukey's Honest Significant Difference test or "FisherLSD" for Fisher's Least Significant Difference test.

5. `verbose` (default: "False"): This lets you print results of the ANOVA and pairwise comparison tests.

## Usage

An example of creating a compact letter display from a pandas DataFrame:

```python
import pandas as pd
import compactletterdisplay

# Create your DataFrame:
df = pd.DataFrame({
'control': [1.2, 3.6, 4.2, 2.9, 3.5],
'treatment1': [33.4, 53.7, 23.8, 43.9, 33.7],
'treatment2': [4.2, 2.7, 3.5, 4.1, 3.3],
'treatment3': [33.3, 51.7, 22.5, 43.0, 32.6]
})

# Define columns to perform comparison test on.
columns = ['control', 'treatment1', 'treatment2', 'treatment3']

# Perform ANOVA, pairwise comparison, get compact letter displays
alpha = 0.1
result_df = compactletterdisplay.anova_cld(df, columns, alpha)

print(result_df)
```

An example using a CSV file:

```python
from compactletterdisplay.pairwise_comp import anova_cld

filepath = "example.csv"  # update with your csv or xlsx file path
alpha = 0.05

# directly pass the filepath to the function
result_df = anova_cld(filepath, alpha=alpha, method="FisherLSD", verbose = True)

print(result_df)

list_of_cld = result_df['CLD'].tolist()

print(list_of_cld)

```


## Output

The output of the CSV file example above is:

```
ANOVA results:
F: 29.851698144175202
p-value: 8.654291303569279e-07

 Fisher's LSD results:
==========================================================
  group1     group2   p-value     reject
----------------------------------------------------------
  control   treatment1    0.00015     True
  control   treatment2    0.43360     False
  control   treatment3    0.00015     True
  treatment1   treatment2    0.00016     True
  treatment1   treatment3    0.88336     False
  treatment2   treatment3    0.00016     True
========================================================== 

        Group   Mean CLD
0     control   3.08   a
1  treatment1  37.70   b
2  treatment2   3.56   a
3  treatment3  36.62   b
['a', 'b', 'a', 'b']

```