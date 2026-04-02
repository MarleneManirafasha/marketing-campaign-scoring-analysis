df = df.drop_duplicates()
df = df.dropna(subset=["response"])

from sklearn.linear_model import LogisticRegression

X = df[["age", "nb_achats", "montant_total"]]
y = df["response_flag"]

model = LogisticRegression()
model.fit(X, y)

df["score"] = model.predict_proba(X)[:,1]