import matplotlib.pyplot as plt

# читаем файл (подставь своё имя файла)
f = open("students.csv")
rows = []
for line in f.readlines():
    line = line.strip()
    if line == "":
        continue
    parts = line.split(";")
    prep = parts[0]
    group = parts[1]
    mark = int(parts[2])
    rows.append((prep, group, mark))
f.close()

def draw(ax, rows, key_index, title):
    keys = sorted(set(r[key_index] for r in rows))
    marks = sorted(set(r[2] for r in rows))

    count = {}
    for k in keys:
        for m in marks:
            count[(k, m)] = 0
    for r in rows:
        count[(r[key_index], r[2])] += 1

    bottom = [0] * len(keys)
    for m in marks:
        heights = [count[(k, m)] for k in keys]
        ax.bar(keys, heights, bottom=bottom, label=str(m))
        for i in range(len(keys)):
            bottom[i] += heights[i]

    ax.set_title(title)
    ax.legend(title="Оценка", bbox_to_anchor=(1.01, 1), loc="upper left")


fig, axes = plt.subplots(2, 1, figsize=(10, 9))
draw(axes[0], rows, 0, "Marks per prep")
draw(axes[1], rows, 1, "Marks per group")

plt.tight_layout()
plt.savefig("marks.png", dpi=150)
plt.show()