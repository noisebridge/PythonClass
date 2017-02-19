import pandas as pd


bad_df = pd.DataFrame.from_records([
    3
])



good_df = pd.DataFrame.from_records([
    {
        'key': 3
    }
])



good_df.to_csv('out.csv')
