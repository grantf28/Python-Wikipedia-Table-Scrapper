import pandas as pd
html = "https://en.wikipedia.org/w/index.php?title=2020_coronavirus_pandemic_in_South_Africa&oldid=953046086"

df = pd.read_html(html)[3]
df = df.fillna(0)
df.columns = df.columns.map(lambda x: '|'.join([str(i) for i in x]))

df.drop(['EC|EC', 'FS|FS', 'GP|GP', 'KZN|KZN', 'LP|LP', 'MP|MP', 'NW|NW', 'NC|NC', 'WC|WC', 'un|un','Deaths|New','Rec|Rec','Ref|Ref'], axis=1, inplace=True)

df.rename(columns={'2020|2020':'Date','Confirmed|New':'NewCases','Confirmed|Total':'TotalCases','Deaths|Total':'Deaths','Agtests|Agtests':'Tests'}, inplace=True)
df.drop(df.tail(2).index,inplace=True)
df.to_csv('data.csv', encoding='utf-8', index=False)