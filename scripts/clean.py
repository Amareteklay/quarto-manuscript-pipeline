import pandas as pd
df = pd.read_csv("../data/sample.csv")
df = df[df.y > 2]
df.to_csv("../data/cleaned.csv", index=False)
print("Cleaned data written to data/cleaned.csv")
