import pandas as pd 
from scipy.stats import chi2_contingency
from scipy.stats import binom_test

df = pd.read_csv("clicks.csv")

print (df.head())

df['is_purchase'] = df.click_day.apply(lambda x: "Purchase" if pd.notnull(x) else "No Purchase")

purchase_counts = df.groupby(['group', 'is_purchase']).user_id.count().reset_index()

print (purchase_counts)

contingency = [[316, 1350],
			   [183, 1483],
			   [83, 1583]]

chi2_stat, pvalue, dof, expfreq = chi2_contingency(contingency)
print (pvalue)

is_significant = True

num_visits = len(df)
num_sales_99 = 1000 / .99
num_sales_199 = 1000 / 1.99
num_sales_499 = 1000 / 4.99

p_clicks_099 = num_sales_99 / num_visits
p_clicks_199 = num_sales_199 / num_visits
p_clicks_499 = num_sales_499 / num_visits

pvalueA = binom_test(316, 1666, p_clicks_099)
pvalueB = binom_test(183, 1666, p_clicks_199)
pvalueC = binom_test(83, 1666, p_clicks_499)