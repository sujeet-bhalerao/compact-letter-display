import pandas as pd
import pycld

df = pd.DataFrame({
    'control': [1.2, 3.6, 4.2, 2.9, 3.5],
    'treatment1': [33.4, 53.7, 23.8, 43.9, 33.7],
    'treatment2': [4.2, 2.7, 3.5, 4.1, 3.3],
    'treatment3': [33.3, 51.7, 22.5, 43.0, 32.6]
})

columns = ['control', 'treatment1', 'treatment2', 'treatment3']

alpha = 0.1
result_df = pycld.anova_cld(df, columns, alpha=alpha)

print(result_df)
