############### IMPORTS ###############

import pandas as pd
from scipy import stats

############### VARIABLES ###############

file = r'C:\Users\Public\examples\hypo_tests\2-sample\RestingHeartRate_paired_t.csv'
df = pd.read_csv(file)
pre_col = 'Before'
post_col = 'After'

############### FUNCTIONS ###############

# INPUT: a dataframe where the samples are different columns and the names of both columns
# OUTPUT: the results of the paired t-test, testing two-sided, first sample greater-than, and first sample less-than
# ASSUMPTIONS: the confidence level is 95% (alpha = 0.05)
def PairedTtest(df,val_col,cat_col):
    t_stat, p_val = stats.ttest_rel(df[pre_col],df[post_col],nan_policy='raise')
    print('The t-statistic is %s'%t_stat)
    print('The p-value is %s'%p_val)
    if p_val < 0.05:
        print('Reject null hypothesis for two-sided paired t-test. The two samples are statistically different.')
        t_stat_g, p_val_g = stats.ttest_rel(df[pre_col],df[post_col],alternative='greater',nan_policy='raise')
        t_stat_l, p_val_l = stats.ttest_rel(df[pre_col],df[post_col],alternative='less',nan_policy='raise')
        if p_val_l < 0.05:
            print('The mean of sample %s is statistically less than sample %s.'%(pre_col,post_col))
        elif p_val_g < 0.05:
            print('The mean of sample %s is statistically greater than sample %s.'%(pre_col,post_col))
    else:
        print('Accept null hypothesis for two-sided paired t-test. The two samples are not statistically different.')

############### MAIN ###############

if __name__ == "__main__":
    PairedTtest(df,val_col,cat_col)