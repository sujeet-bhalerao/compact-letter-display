from compactletterdisplay.pairwise_comp import anova_cld

filepath = "example.csv"  # update with your csv or xlsx file path
alpha = 0.05


# Now directly pass the filepath to the function
result_df = anova_cld(filepath, columns= None, alpha=alpha, method="FisherLSD", verbose=True)

print(result_df)

list_of_cld = result_df['CLD'].tolist()

print(list_of_cld)