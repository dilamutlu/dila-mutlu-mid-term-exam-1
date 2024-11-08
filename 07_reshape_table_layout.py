import pandas as pd

titanic = pd.read_csv("dila-mutlu-mid-term-exam-1/titanic.csv")
print(titanic.head())

air_quality = pd.read_csv("dila-mutlu-mid-term-exam-1/air_quality_long.csv", index_col="date.utc", parse_dates=True)
print(air_quality.head())

print(titanic.sort_values(by="Age").head())

print(titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head())

no2 = air_quality[air_quality["parameter"] == "no2"]
no2_subset = no2.sort_index().groupby(["location"]).head(2)
print(no2_subset)

print(no2_subset.pivot(columns="location", values="value"))
print(no2.head())

print(no2.pivot(columns="location", values="value").plot())

