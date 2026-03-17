import numpy as np
import matplotlib.pyplot as plt

files = [
    "/Users/xiechangen/Downloads/6_3mW_10s3run.txt",
    "/Users/xiechangen/Downloads/6-1_3mW.txt",
    "/Users/xiechangen/Downloads/6-2_3mW.txt",
    "/Users/xiechangen/Downloads/6-3_3mW.txt"
]

plt.figure()

for i, fname in enumerate(files, start=1):
    # 自動判斷分隔符
    try:
        data = np.loadtxt(fname, delimiter=',')
    except:
        data = np.loadtxt(fname)

    x = data[:, 0]  # Raman shift (cm^-1)
    y = data[:, 1]  # Raman intensity (a.u.)

    # 2D band 區間
    mask = (x >= 2600) & (x <= 2750)

    plt.plot(
        x[mask],
        y[mask],
        label=f"file {i}"
    )

plt.xlabel("Raman shift (cm$^{-1}$)")
plt.ylabel("Raman intensity (a.u.)")
plt.title("Raman 2D band (2650–2700 cm$^{-1}$)")
plt.legend()
plt.tight_layout()
plt.show()
