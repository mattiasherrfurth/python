############### IMPORTS ###############

import pandas as pd
from scipy import stats

############### VARIABLES ###############

file = r'C:\Users\Public\examples\hypo_tests\1-sample\FamilyEnergyCost_1sample_t.csv'
df = pd.read_csv(file)
col = 'EnergyCost'
target = 200

############### FUNCTIONS ###############

# INPUT: a dataframe, the numeric column, and the target being tested
# OUTPUT: the results of the 1-sample t-test, testing two-sided, greater-than, and less-than
# ASSUMPTIONS: the confidence level is 95% (alpha = 0.05)
def OneSampleTtest(df,col,target):
    t_stat, p_val = stats.ttest_1samp(a=df[col],popmean=target)
    print('These are the descriptive statistics for the sample: \n%s\n'%df[col].describe())
    print('The t-statistic is %s'%t_stat)
    print('The p-value for two-sided testing is %s'%p_val)
    if p_val < 0.05:
        print('Reject null hypothesis for two-sided t-test. The sample mean is statistically different than the target.\n')
        OneSampleTtest_greater(df,col,target)
        OneSampleTtest_less(df,col,target)
    else:
        print('Accept null hypothesis for two-sided t-test. The sample mean is not statistically different than the target.\n')

# INPUT: a dataframe, the numeric column, and the target being tested
# OUTPUT: the results of the 1-sample t-test testing for whether the sample mean is greater than the target
# ASSUMPTIONS: the confidence level is 95% (alpha = 0.05)
def OneSampleTtest_greater(df,col,target):
    t_stat, p_val = stats.ttest_1samp(a=df[col],popmean=target,alternative='greater')
    print('The p-value when testing for greater is %s'%p_val)
    if p_val < 0.05:
        print('Reject null hypothesis for greater than t-test. The sample mean is statistically greater than the target.\n')
    else:
        print('Accept null hypothesis for greater than t-test. The sample mean is not statistically greater than the target.\n')

# INPUT: a dataframe, the numeric column, and the target being tested
# OUTPUT: the results of the 1-sample t-test testing for whether the sample mean is less than the target
# ASSUMPTIONS: the confidence level is 95% (alpha = 0.05)
def OneSampleTtest_less(df,col,target):
    t_stat, p_val = stats.ttest_1samp(a=df[col],popmean=target,alternative='less')
    print('The p-value when testing for less is %s'%p_val)
    if p_val < 0.05:
        print('Reject null hypothesis for less than t-test. The sample mean is statistically less than the target.\n')
    else:
        print('Accept null hypothesis for less than t-test. The sample mean is not statistically less than the target.\n')

############### MAIN ###############

if __name__ == "__main__":
    OneSampleTtest(df,col,target)