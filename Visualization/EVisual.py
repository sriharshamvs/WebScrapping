import pandas as pd

print("2019 Election Results")
path = "ElectionResults.csv"
ElectionResults = pd.read_csv(path, error_bad_lines=False, warn_bad_lines=False)
ElectionResults = ElectionResults.drop(['O.S.N.'], axis=1)

state_String = str(input('Enter State: '))
constituency_String = str(input('Enter Constituency: '))

ElectionResults_ST_UT_Const = ElectionResults.groupby(['State', 'Constituency'])
df_1 = ElectionResults_ST_UT_Const.get_group((state_String, constituency_String))
df_1.reset_index(inplace=True)
print(df_1.head(12))
