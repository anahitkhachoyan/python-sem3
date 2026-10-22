import pandas as pd
import matplotlib.pyplot as plt

fl = pd.read_csv("flights.csv", index_col=0)

res = fl.groupby("CARGO").agg(
    flights=("PRICE", "count"),   
    price=("PRICE", "sum"),        
    weight=("WEIGHT", "sum"),      
)
print(res)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
res["flights"].plot(kind="bar", ax=axes[0], title="Количество рейсов")
res["price"].plot(kind="bar", ax=axes[1], title="Полная стоимость грузов")
res["weight"].plot(kind="bar", ax=axes[2], title="Полная масса грузов")
for ax in axes:
    ax.set_xlabel("")
    ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.savefig("flights.png", dpi=150)
plt.show()