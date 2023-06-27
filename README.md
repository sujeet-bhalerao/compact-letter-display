# Compact Letter Display

From : "Hans-Peter Piepho (2004), An Algorithm for a Letter-Based Representation of All-Pairwise Comparisons, Journal of Computational and Graphical Statistics, 13(2), 456--466."

In general terms, the insert-and-absorb algorithm can be stated as follows:

1. Generate a column connecting all treatments (i.e., give them all the same letter).

2. For each significant comparison, do the following:

   - For each column currently in the display, do the following:
   
     * If the column connects the two significantly different treatments (i.e., has the same letter for the two significantly different treatments), then do the following:

       - Duplicate the column.

       - In the first of the two columns, delete the letter corresponding to the one treatment. If possible, absorb the column into another column.

       - In the second of the two columns, delete the letter corresponding to the other treatment. If possible, absorb the column into another column.
