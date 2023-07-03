############### IMPORTS ###############

import pandas as pd
from scipy import stats

############### VARIABLES ###############

file = r'C:\Users\Public\examples\hypo_tests\2-sample\HospitalComparison_2sample_t.csv'
df = pd.read_csv(file)
val_col = 'Rating'
cat_col = 'Hospital'

############### FUNCTIONS ###############

# INPUT: a dataframe, the numeric column name, and the categorical column name
# OUTPUT: the results of the 2-sample t-test, testing two-sided, first sample greater-than, and first sample less-than
# ASSUMPTIONS: the confidence level is 95% (alpha = 0.05), the variances of both populations are equal
def TwoSampleTtest(df,val_col,cat_col):
    if df[cat_col].unique().shape[0] > 2:
        print('Cannot perform 2-sample t-test, there are more than two categorical variables.')
    elif df[cat_col].unique().shape[0] < 2:
        print('Cannot perform 2-sample t-test, there are less than two categorical variables.')
    else:
        samples = []
        for cat in df[cat_col].unique():
            print('These are the descriptive statistics for category %s: \n%s\n'%(cat,df[df[cat_col] == cat][val_col].describe()))
            samples += [(cat,df[df[cat_col] == cat][val_col].to_list())]
        t_stat, p_val = stats.ttest_ind(a=samples[0][1], b=samples[1][1], equal_var=True)
        print('The t-statistic is %s'%t_stat)
        print('The p-value is %s'%p_val)
        if p_val < 0.05:
            print('Reject null hypothesis for two-sided 2-sample t-test. The two samples are statistically different.')
            t_stat_g, p_val_g = stats.ttest_ind(a=samples[0][1], b=samples[1][1], equal_var=True, alternative='greater')
            t_stat_l, p_val_l = stats.ttest_ind(a=samples[0][1], b=samples[1][1], equal_var=True, alternative='less')
            if p_val_l < 0.05:
                print('The mean of sample %s is statistically less than sample %s.'%(samples[0][0],samples[1][0]))
            elif p_val_g < 0.05:
                print('The mean of sample %s is statistically greater than sample %s.'%(samples[0][0],samples[1][0]))
        else:
            print('Accept null hypothesis for two-sided 2-sample t-test. The two samples are not statistically different.')

# INPUT: a dataframe, the numeric column name, and the categorical column name
# OUTPUT: the results of the 2-sample t-test, testing two-sided, first sample greater-than, and first sample less-than
# ASSUMPTIONS: the confidence level is 95% (alpha = 0.05), the variances of both populations are not equal
def WelchsTtest(df,val_col,cat_col):
    if df[cat_col].unique().shape[0] > 2:
        print('Cannot perform 2-sample t-test, there are more than two categorical variables.')
    elif df[cat_col].unique().shape[0] < 2:
        print('Cannot perform 2-sample t-test, there are less than two categorical variables.')
    else:
        samples = []
        for cat in df[cat_col].unique():
            print('These are the descriptive statistics for category %s: \n%s\n'%(cat,df[df[cat_col] == cat][val_col].describe()))
            samples += [(cat,df[df[cat_col] == cat][val_col].to_list())]
        t_stat, p_val = stats.ttest_ind(a=samples[0][1], b=samples[1][1], equal_var=False)
        print('The t-statistic is %s'%t_stat)
        print('The p-value is %s'%p_val)
        if p_val < 0.05:
            print("Reject null hypothesis for two-sided Welch's t-test. The two samples are statistically different.")
            t_stat_g, p_val_g = stats.ttest_ind(a=samples[0][1], b=samples[1][1], equal_var=False, alternative='greater')
            t_stat_l, p_val_l = stats.ttest_ind(a=samples[0][1], b=samples[1][1], equal_var=False, alternative='less')
            if p_val_l < 0.05:
                print('The mean of sample %s is statistically less than sample %s.'%(samples[0][0],samples[1][0]))
            elif p_val_g < 0.05:
                print('The mean of sample %s is statistically greater than sample %s.'%(samples[0][0],samples[1][0]))
        else:
            print("Accept null hypothesis for two-sided Welch's t-test. The two samples are not statistically different.")

############### MAIN ###############

if __name__ == "__main__":
    TwoSampleTtest(df,val_col,cat_col)
    WelchsTtest(df,val_col,cat_col)