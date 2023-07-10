import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def perform_anova(df, columns):
    """
    Perform ANOVA test on certain columns of a DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data.
    columns (list of str): List of column names in df to perform ANOVA on.

    Returns:
    F (float): The computed F-value of the test.
    p (float): The associated p-value from the F-distribution.
    """
    
    F, p = stats.f_oneway(*[df[col] for col in columns])

    return F, p

def perform_pairwise_tukey(df, columns):
    """
    Perform pairwise Tukey HSD (Honest Significant Difference) test.
  
    The pairwise Tukey HSD test is a post-hoc test to determine significant differences
    between all possible pairs of groups of data.

    Parameters:
    df (pd.DataFrame): DataFrame containing the data.
    columns (list of str): List of column names in df to perform the Tukey HSD test on.

    Returns:
    tukey (pairwise_tukeyhsd): Result of the Tukey HSD test.
    """

    # Preparing data for Tukey HSD
    df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=columns)
    df_melt.columns = ['index', 'treatments', 'value']
    
    # Performing Tukey HSD
    tukey = pairwise_tukeyhsd(endog=df_melt['value'],
                              groups=df_melt['treatments'],
                              alpha=0.05)

    return tukey
