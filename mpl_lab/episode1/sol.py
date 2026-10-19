import os
import matplotlib.pyplot as plt

folder = "dead_moroz"
os.makedirs("plots", exist_ok=True)

for name in os.listdir(folder):
    if not name.endswith(".dat"):
        continue

    f = open(os.path.join(folder, name))
    n = int(f.readline())

    xs = []
    ys = []
    for i in range(n):
        x, y = f.readline().split()
        xs.append(float(x))
        ys.append(float(y))
    f.close()

    plt.figure(figsize=(10, 5))
    plt.scatter(xs, ys)
    plt.axis("equal")
    plt.title("Number of points: " + str(n))

    plt.savefig("plots/" + name + ".png")
    plt.show()