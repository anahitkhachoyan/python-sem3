import pandas as pd
import matplotlib.pyplot as plt

pay = pd.read_csv("transactions.csv", index_col=0)

ok = pay[pay["STATUS"] == "OK"]          # только проведённые платежи

print("Топ-3 платежа:")
print(ok.sort_values("SUM", ascending=False).head(3))

umbrella = ok[ok["CONTRACTOR"] == "Umbrella, Inc"]
print("Сумма для Umbrella:", umbrella["SUM"].sum())