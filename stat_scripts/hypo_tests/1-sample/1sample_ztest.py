############### IMPORTS ###############

import pandas as pd
from statsmodels.stats.weightstats import ztest

############### VARIABLES ###############

file = r'C:\Users\Public\examples\hypo_tests\1-sample\FatContent_1sample_z.csv'
df = pd.read_csv(file)
col = 'PercentFat'
target = 15

############### FUNCTIONS ###############

# INPUT: a dataframe, the numeric column, and the target being tested
# OUTPUT: the results of the 1-sample z-test, testing two-sided, greater-than, and less-than
# ASSUMPTIONS: the confidence level is 95% (alpha = 0.05)
def OneSampleZtest(df,col,target):
    z_stat, p_val = ztest(df[col],value=target)
    print('These are the descriptive statistics for the sample: \n%s\n'%df[col].describe())
    print('The z-statistic is %s'%z_stat)
    print('The p-value for two-sided testing is %s'%p_val)
    if p_val < 0.05:
        print('Reject null hypothesis for two-sided z-test. The sample mean is statistically different than the target.\n')
        OneSampleZtest_larger(df,col,target)
        OneSampleZtest_smaller(df,col,target)
    else:
        print('Accept null hypothesis for two-sided z-test. The sample mean is not statistically different than the target.\n')

# INPUT: a dataframe, the numeric column, and the target being tested
# OUTPUT: the results of the 1-sample z-test testing for whether the sample mean is greater than the target
# ASSUMPTIONS: the confidence level is 95% (alpha = 0.05)
def OneSampleZtest_larger(df,col,target):
    z_stat, p_val = ztest(df[col],value=target,alternative='larger')
    print('The p-value when testing for greater is %s'%p_val)
    if p_val < 0.05:
        print('Reject null hypothesis for greater than z-test. The sample mean is statistically greater than the target.\n')
    else:
        print('Accept null hypothesis for greater than z-test. The sample mean is not statistically greater than the target.\n')

# INPUT: a dataframe, the numeric column, and the target being tested
# OUTPUT: the results of the 1-sample z-test testing for whether the sample mean is less than the target
# ASSUMPTIONS: the confidence level is 95% (alpha = 0.05)
def OneSampleZtest_smaller(df,col,target):
    z_stat, p_val = ztest(df[col],value=target,alternative='smaller')
    print('The p-value when testing for less is %s'%p_val)
    if p_val < 0.05:
        print('Reject null hypothesis for less than z-test. The sample mean is statistically less than the target.\n')
    else:
        print('Accept null hypothesis for less than z-test. The sample mean is not statistically less than the target.\n')

############### MAIN ###############

if __name__ == "__main__":
    OneSampleZtest(df,col,target)