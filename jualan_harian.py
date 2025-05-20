import matplotlib.pyplot as plt
import numpy as np

# Data jualan
hari = [
    "Ahad", "Isnin", "Selasa", "Rabu", "Khamis", "Jumaat", "Sabtu",
    "Ahad", "Isnin", "Selasa", "Khamis", "Jumaat", "Sabtu",
    "Ahad", "Isnin", "Selasa", "Rabu", "Khamis", "Jumaat",
    "Sabtu", "Ahad", "Isnin", "Selasa", "Rabu"
]
tarikh = [
    "2/3", "3/3", "4/3", "5/3", "6/3", "7/3", "8/3",
    "9/3", "10/3", "11/3", "13/3", "14/3", "15/3",
    "16/3", "17/3", "18/3", "19/3", "20/3", "21/3",
    "22/3", "24/3", "25/3", "26/3", "27/3"
]
sale = [
    321, 285, 225, 193, 168, 111, 217,
    372, 261, 278, 175, 227, 144,
    275, 244, 209, 131, 199, 147,
    242, 319, 269, 295, 348
]

# Check if the lengths match
if len(hari) != len(tarikh) or len(tarikh) != len(sale):
    print("Error: The lengths of 'hari', 'tarikh', and 'sale' do not match.")
else:
    # Gabungkan nama hari dan tarikh untuk label paksi-x
    label_x = [f"{h} ({d})" for h, d in zip(hari, tarikh)]

    # Kira jumlah jualan
    jumlah_sale = sum(sale)

    # Buat figure dengan 1 subplot
    fig, ax = plt.subplots(figsize=(14, 7))
    x_indexes = np.arange(len(hari))

    # Warna untuk bar chart
    color_sale = '#28B463'

    # Subplot: Jualan
    ax.bar(x_indexes, sale, color=color_sale)
    ax.set_xlabel("Hari dan Tarikh")
    ax.set_ylabel("Jualan (RM)")
    ax.set_title("Jualan Harian")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_xticks(x_indexes)
    ax.set_xticklabels(label_x, rotation=45, ha="right")
    for i, txt in enumerate(sale):
        ax.text(i, txt + 5, str(txt), ha='center', fontsize=8)

    # Menambah jumlah jualan di bawah graf
    fig.text(0.1, 0.01, f"Total Jualan: RM {jumlah_sale:.2f}", fontsize=12, color='red')

    # Simpan graf sebagai fail
    plt.tight_layout()
    plt.savefig("graf_jualan.png")  # <- baris ini penting untuk GitHub Actions

    # Papar graf (optional)
    plt.show()
