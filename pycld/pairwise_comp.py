from .anova import perform_anova, perform_pairwise_tukey
from .cld_calculator import compact_letter_display
import pandas as pd
import os
from scipy import stats
from scipy.stats import ttest_ind

def read_data_file(filepath):
    """
    Reads the input data file in the .csv or .xlsx format into a Pandas DataFrame.

    Parameters:
        filepath (str): The path to the data file.

    Returns:
        pd.DataFrame: The content of the data file as a DataFrame object.
    """
    _, file_extension = os.path.splitext(filepath)
    
    if file_extension == '.csv':
        df = pd.read_csv(filepath, index_col=0)
    elif file_extension == '.xlsx':
        df = pd.read_excel(filepath, index_col=0)
    else:
        raise ValueError("Invalid file format. Please provide a .csv or .xlsx file.")
    return df



def perform_fisher_lsd(df, columns, alpha=0.05, verbose = False):
    """
    Performs Fisher's Least Significant Difference (LSD) test on the DataFrame columns after validation through ANOVA.

    Parameters: 
        df (pd.DataFrame): The DataFrame on which the test will be performed.
        columns (list): The list of column names to be used in the test.
        alpha (float): The significance level for the test (default: 0.05).

    Returns:
        pd.DataFrame: Pairs of groups with their 'p value' indicating their significance of difference.
    """
    anova_F, anova_p = perform_anova(df, columns)
            
    if anova_p > alpha:
        raise ValueError("The ANOVA test is not significant, so Fisher's LSD is not appropriate.")
            
    all_pairs = []
    significant_pairs = []
    p_vals = []
    rejects = []

    # Create all pairs and significant pairs list
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            t_stat, p_val = stats.ttest_ind(df[columns[i]], df[columns[j]])
            all_pairs.append((columns[i], columns[j]))
            p_vals.append(p_val)
            if p_val < alpha:
                significant_pairs.append((columns[i], columns[j]))
                rejects.append(True)
            else:
                rejects.append(False)

    lsd_res_df = pd.DataFrame({
        'group1': [pair[0] for pair in all_pairs],
        'group2': [pair[1] for pair in all_pairs],
        'p value': p_vals,
        'reject': rejects
    })

    if verbose: 
        print(" Fisher's LSD results:")
        print("==========================================================")
        print("  group1     group2   p-value     reject")
        print("----------------------------------------------------------")
        for index in range(len(lsd_res_df)):
            result = lsd_res_df.iloc[index]
            print(f"  {result['group1']}   {result['group2']}    {result['p value']:.5f}     {result['reject']}")
        print("========================================================== \n")

    # return both the full results and the significant pairs
    return lsd_res_df, significant_pairs


def perform_comparison(data, columns=None, alpha=0.05, method="TukeyHSD", verbose=False):
    """
    Performs ANOVA on the given DataFrame. If the result is significant, it performs a pairwise comparison.

    Parameters:
        data (str or pd.DataFrame): Either the DataFrame or the path to the .csv or .xlsx file.
        columns (list): List of columns to include in the test (default: all).
        alpha (float): The significance level for the ANOVA (default: 0.05).
        method (str): The type of pairwise test to use (default: "TukeyHSD").

    Returns:
        list: Pairs of groups that are significantly different or an empty list if no groups are significantly different.
    """
    df = read_data_file(data) if isinstance(data, str) else data
    if columns is None:
        columns = df.columns.tolist()

    anova_F, anova_p = perform_anova(df, columns)

    if verbose:
        print(f'ANOVA results:\nF: {anova_F}\np-value: {anova_p}\n')

    if anova_p < alpha:
        if method == "TukeyHSD":
            tukey_res = perform_pairwise_tukey(df, columns)

            if verbose:
                print(f'Tukey HSD results:\n{tukey_res}\n')

            pair_df = pd.DataFrame(data=tukey_res._results_table.data[1:], columns=tukey_res._results_table.data[0])
            significant_pairs = pair_df[pair_df['reject'] == True][['group1', 'group2']].values.tolist()
            #print(significant_pairs)
            return significant_pairs

        elif method == "FisherLSD":
            lsd_res, significant_pairs = perform_fisher_lsd(df, columns, alpha, verbose)
            significant_pairs = significant_pairs
            return significant_pairs

        else:
            raise ValueError('Invalid method. Choose either "TukeyHSD" or "FisherLSD".')

    else:
        print(f'ANOVA test is not significant (p > {alpha}).')
        return []

def anova_cld(data, columns=None, alpha=0.05, method="TukeyHSD", verbose = False):
    """
    Performs statistical test and generates the Compact Letter Display (CLD) for the given data.

    Parameters:
        data (str or pd.DataFrame): Either the DataFrame or the path to the .csv or .xlsx file.
        columns (list): List of columns to include in the test (default: all).
        alpha (float): The significance level for the ANOVA (default: 0.05).
        method (str): The type of pairwise test to use (default: "TukeyHSD").

    Returns:
        pd.DataFrame: DataFrame with groups, their means, and their corresponding CLD or the original DataFrame if no groups are significantly different.
    """
    df = read_data_file(data) if isinstance(data, str) else data
        
    if columns is not None:
        df = df.loc[:, columns]

    significant_pairs = perform_comparison(df, columns=columns, alpha=alpha, method=method, verbose=verbose)

    if not significant_pairs:
        print("No significant pairs found.")

    cld_result = compact_letter_display(significant_pairs, df.columns.tolist())
    means = df.mean().tolist()

    result_df = pd.DataFrame(list(zip(df.columns, means, cld_result)), columns=["Group", "Mean", "CLD"])

    return result_df
