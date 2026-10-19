import math
import matplotlib.pyplot as plt

f = open("frames.dat.txt")
lines = []
for line in f.readlines():
    if line.strip() != "":
        lines.append(line)
f.close()

frames = []
for i in range(0, len(lines), 2):
    xs = [float(a) for a in lines[i].split()]
    ys = [float(a) for a in lines[i + 1].split()]
    frames.append((xs, ys))

xmin = min(min(xs) for xs, ys in frames)
xmax = max(max(xs) for xs, ys in frames)
ymin = min(min(ys) for xs, ys in frames)
ymax = max(max(ys) for xs, ys in frames)

n = len(frames)
cols = 2
rows = math.ceil(n / cols)

fig, axes = plt.subplots(rows, cols, figsize=(8, 3.3 * rows))
axes = axes.flatten()

for i in range(n):
    xs, ys = frames[i]
    ax = axes[i]
    ax.plot(xs, ys)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.grid(True, alpha=0.5)
    ax.set_title("Frame " + str(i))

for j in range(n, len(axes)):
    axes[j].axis("off")

plt.tight_layout()
plt.savefig("all_frames.png", dpi=150)
plt.show()