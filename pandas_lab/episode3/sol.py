import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel("students_info.xlsx")
table = pd.read_html("results_ejudge.html")[0]

# соединяем две таблицы по логину
data = table.merge(students, left_on="User", right_on="login")

# Задача 1: средние по группам
by_fac = data.groupby("group_faculty")["Solved"].mean()
by_out = data.groupby("group_out")["Solved"].mean()

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
by_fac.plot(kind="bar", ax=axes[0], title="Среднее число задач по факультетским группам")
by_out.plot(kind="bar", ax=axes[1], title="Среднее число задач по группам по информатике")
for ax in axes:
    ax.set_ylabel("решено задач")
    ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.savefig("solved.png", dpi=150)
plt.show()

# Задача 2: кто набрал больше 10 баллов в G или H
good = data[(data["G"] > 10) | (data["H"] > 10)]
print(good[["User", "G", "H", "group_faculty", "group_out"]])
print("Факультетские группы:", sorted(good["group_faculty"].unique()))
print("Группы по информатике:", sorted(good["group_out"].unique()))


#Доп. задание: проблемы в данных
print("Пустые логины в xlsx:", students["login"].isna().sum())
print("Логины из ejudge, которых нет в xlsx:")
print(sorted(set(table["User"]) - set(students["login"])))